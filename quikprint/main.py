#!/usr/bin/env python3
# -- coding: utf-8 --

import sys, os, subprocess
from PyQt4.QtGui import (QApplication, QDialog, QButtonGroup, QRegExpValidator,
    QMessageBox, QFileDialog, QIcon)
from PyQt4.QtCore import QProcess, QRegExp, QSettings

sys.path.append(os.path.dirname(__file__))
from ui_window import Ui_Dialog
from __init__ import __version__

fromByteArray = lambda bA : bytes(bA).decode("utf-8")

class Window(QDialog, Ui_Dialog):
    def __init__(self):
        QDialog.__init__(self)
        QIcon.setThemeName("Adwaita")
        self.setupUi(self)
        self.resize(640, 480)
        self.setWindowTitle("QuikPrint  " + __version__)
        self.settings = QSettings(self)
        self.process = QProcess(self)
        # Create and setup widgets
        self.widthSpin.setHidden(True)
        self.heightSpin.setHidden(True)
        self.pageSetGroup = QButtonGroup(self)
        self.pageSetGroup.addButton(self.allPagesBtn)
        self.pageSetGroup.addButton(self.rangeBtn)
        self.allPagesBtn.setChecked(True)
        rangeValidator = QRegExpValidator(self.pagerangeEdit)
        rangeValidator.setRegExp(QRegExp('([0-9,-])*')) # TODO : check validity of whole string
        self.pagerangeEdit.setValidator(rangeValidator)
        # Connect Signals
        self.pageSetGroup.buttonClicked.connect(self.onPageRangeChange)
        self.papersizeCombo.currentIndexChanged.connect(self.onPaperSizeChange)
        self.pixelDensityBtn.clicked.connect(self.onDensityBtnClick)
        self.printBtn.clicked.connect(self.accept)
        self.quitBtn.clicked.connect(self.reject)
        self.cancelJobsBtn.clicked.connect(self.cancelPrintJobs)
        # Set values
        printers = self.getPrinters()
        if printers == []:
            QMessageBox.critical(self, 'Error !', 'No Printers added', 'Close')
            return QDialog.accept(self)
        self.printersCombo.addItems(printers)
        # get first selected printer options
        printer = Deskjet_2130(printers[0])
        if not printer.getOptions():
            QMessageBox.critical(self, 'Error !', 'Could not get Printer options', 'Close')
            return QDialog.accept(self)
        self.colorBtn.setChecked(printer.color_print)
        self.grayBtn.setChecked(not printer.color_print)
        self.qualityCombo.setCurrentIndex(printer.quality_index)
        self.papersizeCombo.setCurrentIndex(printer.papersize_index)
        # get printer independent options
        fit_to_page = True if self.settings.value("FitToPage", "false")=='true' else False
        self.fitToPageBtn.setChecked(fit_to_page)
        brightness = int(self.settings.value("Brightness", 100))
        gamma = int(self.settings.value("Gamma", 1000))
        ppi = int(self.settings.value("PPI", 300))
        natural_scaling = int(self.settings.value("NaturalScaling", 100))
        scaling = int(self.settings.value("Scaling", 100))
        paper_w = int(self.settings.value("PaperW", 100))
        paper_h = int(self.settings.value("PaperH", 100))
        self.brightnessSpin.setValue(brightness)
        self.gammaSpin.setValue(gamma)
        self.ppiSpin.setValue(ppi)
        self.naturalScalingSpin.setValue(natural_scaling)
        self.scalingSpin.setValue(scaling)
        self.widthSpin.setValue(paper_w)
        self.heightSpin.setValue(paper_h)

    def onPaperSizeChange(self, index):
        hide_custom = self.papersizeCombo.currentText()!="Custom"
        self.widthSpin.setHidden(hide_custom)
        self.heightSpin.setHidden(hide_custom)

    def onPageRangeChange(self, btn):
        self.pagerangeEdit.setEnabled(btn is self.rangeBtn)
        self.pagerangeEdit.setFocus()

    def onDensityBtnClick(self, checked):
        self.ppiSpin.setEnabled(checked)
        self.naturalScalingSpin.setEnabled(checked)

    def accept(self):
        filenames = []
        if len(sys.argv)>1 :
            for each in sys.argv[1:]:
                if os.path.exists(each):
                    filenames.append(os.path.abspath(each))
        if filenames == []:
            files = QFileDialog.getOpenFileNames(self, 'Select Files to Print')
            if list(files) == [] : return
            for each in files:
                filenames.append(each)
        if self.rangeBtn.isChecked() and self.pagerangeEdit.text() == '' : return
        device = self.printersCombo.currentText()
        printer = Deskjet_2130(device)
        color_print = self.colorBtn.isChecked()
        quality_index = self.qualityCombo.currentIndex()
        papersize_index = self.papersizeCombo.currentIndex()
        custom_size = [self.widthSpin.value(), self.heightSpin.value()]
        if not printer.setOptions(color_print, quality_index, papersize_index, custom_size):
            QMessageBox.critical(self, 'Error !', 'Could not set printer options', 'Close')
            return QDialog.accept(self)
        # get printing options
        lp_args = ['-d', device]
        copies = self.copiesSpin.value()
        if copies>1 :
            lp_args += ['-n', str(copies), '-o', 'collate=true']
        if not self.pageSetAll.isChecked():
            page_set = 'odd' if self.pageSetOdd.isChecked() else 'even'
            lp_args += ['-o', 'page-set='+page_set]
        if not self.allPagesBtn.isChecked():
            lp_args += ['-o', 'page-ranges='+self.pagerangeEdit.text()]
        # reverse pages so that first page will be on top
        if self.allPagesBtn.isChecked() and self.pageSetAll.isChecked():
            lp_args += ["-o", "outputorder=reverse"]
        # scale page to fit inside print margin
        if self.fitToPageBtn.isChecked():
            lp_args += ['-o', 'fit-to-page']
        lp_args += ['-o', 'brightness=%i'%self.brightnessSpin.value()]
        lp_args += ['-o', 'gamma=%i'%self.gammaSpin.value()]
        if self.pixelDensityBtn.isChecked():
            lp_args += ['-o', 'ppi=%i'%self.ppiSpin.value(), '-o', 'natural-scaling=%i'%self.naturalScalingSpin.value()]
        else:
            lp_args += ['-o', 'scaling=%i'%self.scalingSpin.value()]
        # position is always left aligned
        positions = ['top', 'center', 'bottom']
        lp_args += ['-o', 'position='+positions[self.positionCombo.currentIndex()]]
        print('lp', ' '.join(lp_args))
        self.process.start('lp', lp_args + ['--'] + filenames)
        if not self.process.waitForFinished():
            QMessageBox.critical(self, 'Error !', 'Error : Could not execute lp', 'Close')
        self.saveSettings()
        QDialog.accept(self)

    def getPrinters(self):
        ''' Get the list of available printers '''
        self.process.start('lpstat', ['-a'])
        if not self.process.waitForFinished():
            print('Error : could not execute lpstat')
            return
        data = self.process.readAllStandardOutput()
        output = fromByteArray(data).strip()
        if output == '' : return []
        lines = output.split('\n')
        printers = []
        # each line is like
        # 'DeskJet_2130 accepting requests since Mon 12 Aug 2019 09:08:12 AM IST\n'
        for line in lines:
            printer = line.split(' ')[0]
            printers.append(printer)
        return printers

    def cancelPrintJobs(self):
        self.process.start('lpstat', ['-o'])
        if not self.process.waitForFinished():
            QMessageBox.critical(self, 'Error !', 'Error : Could not execute lpstat', 'Close')
        data = self.process.readAllStandardOutput()
        output = fromByteArray(data).strip()
        if output == '': return
        lines = output.split('\n')
        for line in lines:
            job_id = line.split(' ')[0]
            subprocess.Popen(['cancel', job_id])

    def saveSettings(self):
        self.settings.setValue("FItToPage", self.fitToPageBtn.isChecked())
        self.settings.setValue("Brightness", self.brightnessSpin.value())
        self.settings.setValue("Gamma", self.gammaSpin.value())
        self.settings.setValue("PPI", self.ppiSpin.value())
        self.settings.setValue("NaturalScaling", self.naturalScalingSpin.value())
        self.settings.setValue("Scaling", self.scalingSpin.value())
        self.settings.setValue("PaperW", self.widthSpin.value())
        self.settings.setValue("PaperH", self.heightSpin.value())

def parseOptions(text):
    ''' Returns a dictionary with options and arguments'''
    value_dict = {}
    lines = text.split('\n')
    # each line is like "ColorModel/Output Mode: CMYGray *KGray RGB"
    # * marked value is the selected value
    for line in lines:
        option, values = line.split('/')
        values = values.split(':')[1].split()
        for value in values:
            if value.startswith('*'):
                value_dict[option] = value[1:]
    return value_dict


class Deskjet_2130:
    ''' Handles printer specific options '''
    def __init__(self, printer_device):
        self.printer = printer_device
        self.quality = ['FastDraft', 'Normal', 'Best', 'Photo']
        self.paper_sizes = ['A4', 'A5', 'Letter', 'Legal', 'Custom.WIDTHxHEIGHT']
        self.process = QProcess()
        self.color_print = False
        self.quality_index = 0
        self.papersize_index = 0

    def getOptions(self):
        print('lpoptions -p %s -l'%self.printer)
        self.process.start('lpoptions', ['-p', self.printer, '-l'])
        if not self.process.waitForFinished():
            return False
        data = self.process.readAllStandardOutput()
        output = fromByteArray(data).strip()
        if output == "" :
            return False
        values = parseOptions(output)
        self.color_print = True if values['ColorModel']=='RGB' else False
        self.quality_index = self.quality.index(values['OutputMode'])
        if values['PageSize'] in self.paper_sizes :
            self.papersize_index = self.paper_sizes.index(values['PageSize'])
        return True

    def setOptions(self, color_print, quality_index, papersize_index, custom_size=[]):
        color_model = 'RGB' if color_print else 'KGray'
        quality = self.quality[quality_index]
        page_size = self.paper_sizes[papersize_index]
        if page_size == 'Custom.WIDTHxHEIGHT':
            page_size = 'Custom.%ix%imm'%(custom_size[0], custom_size[1])

        lpoptions_args = ['-p', self.printer, '-o', 'ColorModel='+color_model,
                    '-o', 'OutputMode='+quality, '-o', 'PageSize='+page_size]
        print('lpoptions', ' '.join(lpoptions_args))
        self.process.start('lpoptions', lpoptions_args)
        if not self.process.waitForFinished():
            print("Error : Could not execute lpoptions")
            return False
        return True


def main():
    app = QApplication(sys.argv)
    app.setOrganizationName("quikprint")
    app.setApplicationName("quikprint")
    win = Window()
    win.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

