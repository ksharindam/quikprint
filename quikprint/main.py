#!/usr/bin/env python
# -- coding: utf-8 --

import sys, os, subprocess
from PyQt4.QtGui import QApplication, QDialog, QButtonGroup, QRegExpValidator, QMessageBox
from PyQt4.QtCore import QString, QProcess, QRegExp, QSettings
from ui_window import Ui_Dialog


class Window(QDialog, Ui_Dialog):
    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)
        self.quality = ['FastDraft', 'Normal', 'Best', 'Photo']
        self.paper_sizes = ['A4', 'A5', 'Letter', 'Custom']
        self.settings = QSettings(self)
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
        self.process = QProcess(self)
        printers = self.getPrinters()
        self.printersCombo.addItems(printers)
        color_mode, quality, paper_size = self.getPrinterConfig()
        if color_mode == 'color': self.colorBtn.setChecked(True)
        else : self.grayBtn.setChecked(True)
        self.qualityCombo.setCurrentIndex(self.quality.index(quality))
        self.papersizeCombo.setCurrentIndex(self.paper_sizes.index(paper_size))
        fit_to_page = True if self.settings.value("FitToPage", "false")=='true' else False
        self.fitToPageBtn.setChecked(fit_to_page)
        brightness = int(self.settings.value("Brightness", 100).toString())
        gamma = int(self.settings.value("Gamma", 1000).toString())
        ppi = int(self.settings.value("PPI", 300).toString())
        natural_scaling = int(self.settings.value("NaturalScaling", 100).toString())
        scaling = int(self.settings.value("Scaling", 100).toString())
        paper_w = int(self.settings.value("PaperW", 100).toString())
        paper_h = int(self.settings.value("PaperH", 100).toString())
        self.brightnessSpin.setValue(brightness)
        self.gammaSpin.setValue(gamma)
        self.ppiSpin.setValue(ppi)
        self.naturalScalingSpin.setValue(natural_scaling)
        self.scalingSpin.setValue(scaling)
        self.widthSpin.setValue(paper_w)
        self.heightSpin.setValue(paper_h)

    def onPaperSizeChange(self, index):
        self.widthSpin.setHidden(not index==3)
        self.heightSpin.setHidden(not index==3)

    def onPageRangeChange(self, btn):
        self.pagerangeEdit.setEnabled(btn is self.rangeBtn)

    def onDensityBtnClick(self, checked):
        self.ppiSpin.setEnabled(checked)
        self.naturalScalingSpin.setEnabled(checked)

    def accept(self):
        if self.pagerangeEdit.text() == '' : return
        printer = str(self.printersCombo.currentText())
        color_model = 'RGB' if self.colorBtn.isChecked() else 'KGray'
        quality = self.quality[self.qualityCombo.currentIndex()]
        page_size = self.paper_sizes[self.papersizeCombo.currentIndex()]
        if page_size == 'Custom':
            page_size = 'Custom.%ix%imm'%(self.widthSpin.value(), self.heightSpin.value())
        lpoptions_args = ['-p', printer, '-o', 'ColorModel='+color_model, '-o', 'OutputMode='+quality,
                          '-o', 'PageSize='+page_size]
        self.process.start('lpoptions', lpoptions_args)
        if not self.process.waitForFinished():
            QMessageBox.critical(self, 'Error !', 'Error : Could not execute lpoptions', 'Close')
            return QDialog.accept(self)
        # get printing options
        copies = str(self.copiesSpin.value())
        lp_args = ['-d', printer, '-n', copies]
        if not self.pageSetAll.isChecked():
            page_set = 'odd' if self.pageSetOdd.isChecked() else 'even'
            lp_args += ['-o', 'page-set='+page_set]
        if not self.allPagesBtn.isChecked():
            lp_args += ['-o', 'page-ranges='+str(self.pagerangeEdit.text())]
        if self.fitToPageBtn.isChecked():
            lp_args += ['-o', 'fit-to-page']
        lp_args += ['-o', 'brightness=%i'%self.brightnessSpin.value()]
        lp_args += ['-o', 'gamma=%i'%self.gammaSpin.value()]
        if self.pixelDensityBtn.isChecked():
            lp_args += ['-o', 'ppi=%i'%self.ppiSpin.value(), '-o', 'natural-scaling=%i'%self.naturalScalingSpin.value()]
        else:
            lp_args += ['-o', 'scaling=%i'%self.scalingSpin.value()]
        positions = ['top', 'center', 'bottom']
        lp_args += ['-o', 'position='+positions[self.positionCombo.currentIndex()]]
        print ' '.join(lp_args)
        filenames = []
        if len(sys.argv)>1 :
            for each in sys.argv[1:]:
                if os.path.exists(each):
                    filenames.append(each.decode('utf8'))
        if filenames != []:
            self.process.start('lp', lp_args + ['--'] + filenames)
            if not self.process.waitForFinished():
                QMessageBox.critical(self, 'Error !', 'Error : Could not execute lp', 'Close')
        self.saveSettings()
        QDialog.accept(self)

    def getPrinterConfig(self):
        self.process.start('lpoptions', ['-l'])
        if not self.process.waitForFinished():
            QMessageBox.critical(self, 'Error !', 'Error : Could not execute lpoptions', 'Close')
            return 'color', 'FastDraft', 'A4'
        data = self.process.readAllStandardOutput()
        output = str(QString.fromUtf8(data)).strip()
        values = parseOptions(output)
        #print output            elif line.startswith('ColorModel'):
        color_mode = 'color' if values['ColorModel']=='RGB' else 'gray'
        quality = values['OutputMode']
        page_size = values['PageSize'] if values['PageSize'] in ['A5', 'Letter'] else 'A4'
        return color_mode, quality, page_size

    def getPrinters(self):
        ''' Get the list of available printers '''
        self.process.start('lpstat', ['-a'])
        if not self.process.waitForFinished():
            print 'Error : could not execute lpstat'
            return
        data = self.process.readAllStandardOutput()
        output = str(QString.fromUtf8(data)).strip()
        if output == '' : return []
        lines = output.split('\n')
        printers = []
        for line in lines:
            printer = line.split(' ')[0]
            printers.append(printer)
        return printers

    def cancelPrintJobs(self):
        self.process.start('lpstat', ['-o'])
        if not self.process.waitForFinished():
            QMessageBox.critical(self, 'Error !', 'Error : Could not execute lpstat', 'Close')
        data = self.process.readAllStandardOutput()
        output = str(QString.fromUtf8(data)).strip()
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
    for line in lines:
        option, values = line.split('/')
        values = values.split(':')[1].split()
        for value in values:
            if value.startswith('*'):
                value_dict[option] = value[1:]
    return value_dict

def main():
    app = QApplication(sys.argv)
    app.setOrganizationName("quikprint")
    app.setApplicationName("quikprint")
    win = Window()
    win.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

