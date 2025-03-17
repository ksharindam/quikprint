#!/usr/bin/env python3
# -- coding: utf-8 --

import sys, os, subprocess
from PyQt5.QtGui import QIcon, QRegExpValidator
from PyQt5.QtWidgets import (QApplication, QDialog, QButtonGroup,
    QMessageBox, QFileDialog)
from PyQt5.QtCore import QProcess, QRegExp, QSettings

sys.path.append(os.path.dirname(__file__))
from ui_window import Ui_Dialog
from __init__ import __version__

fromByteArray = lambda bA : bytes(bA).decode("utf-8")

# lpstat -e -> show list of printers only

# lpstat -v -> view printer name and device uri using. Output -
# device for DeskJet_2130: hp:/usb/DeskJet_2130_series?serial=CN8BK484PD065Z
# device for DCPT420W: usb://Brother/DCP-T420W?serial=E80718H1H136313

# lpstat -a -> show printer names and accepting status. Output -
# DeskJet_2130 accepting requests since Wed 22 Sep 2021 01:14:01 PM IST

# set default printer
# lpoptions -d Printer_Name

# view default printer
# lpstat -d
# system default destination: DeskJet_2130

# View printer specific options by
# lpoptions -p Printer_Name -l


# view all lp command options online
# https://opensource.apple.com/source/cups/cups-30/doc/sum.shtml


class Window(QDialog, Ui_Dialog):
    def __init__(self):
        QDialog.__init__(self)
        QIcon.setThemeName("Adwaita")
        self.setWindowIcon(QIcon.fromTheme("document-print"))
        self.setupUi(self)
        self.resize(640, 460)
        self.setWindowTitle("QuikPrint  " + __version__)
        self.settings = QSettings(self)
        # Create and setup widgets
        self.widthSpin.setHidden(True)
        self.heightSpin.setHidden(True)
        rangeValidator = QRegExpValidator(self.pagerangeEdit)
        rangeValidator.setRegExp(QRegExp('([0-9,-])*')) # TODO : check validity of whole string
        self.pagerangeEdit.setValidator(rangeValidator)
        # Set values
        printers = self.getPrinters()
        if printers == []:
            QMessageBox.critical(self, 'Error !', 'No Printers added', QMessageBox.Close)
            return QDialog.accept(self)
        self.printersCombo.addItems(printers)
        # select default printer options
        default_printer = get_default_printer()
        selected_index = 0
        for i,printer in enumerate(printers):
            if printer == default_printer:
                selected_index = i
                break
        self.printersCombo.setCurrentIndex(selected_index)
        self.selectPrinter(selected_index)
        # get printer independent options
        fit_to_page = self.settings.value("FitToPage", "false")=='true'
        self.fitToPageBtn.setChecked(fit_to_page)
        gamma = int(self.settings.value("Gamma", 1000))
        ppi = int(self.settings.value("PPI", 300))
        natural_scaling = int(self.settings.value("NaturalScaling", 100))
        scaling = int(self.settings.value("Scaling", 100))
        paper_w = int(self.settings.value("PaperW", 100))
        paper_h = int(self.settings.value("PaperH", 100))
        self.gammaSpin.setValue(gamma)
        self.ppiSpin.setValue(ppi)
        self.naturalScalingSpin.setValue(natural_scaling)
        self.scalingSpin.setValue(scaling)
        self.widthSpin.setValue(paper_w)
        self.heightSpin.setValue(paper_h)
        # Connect Signals
        self.printersCombo.currentIndexChanged.connect(self.selectPrinter)
        self.paperSizeCombo.currentIndexChanged.connect(self.onPaperSizeChange)
        self.pixelDensityBtn.clicked.connect(self.onDensityBtnClick)
        self.printBtn.clicked.connect(self.accept)
        self.quitBtn.clicked.connect(self.reject)
        self.cancelJobsBtn.clicked.connect(self.cancelPrintJobs)

    def selectPrinter(self, index):
        printer_name = self.printersCombo.itemText(index)
        printer = printer_from_name(printer_name)
        if not printer.getOptions():
            QMessageBox.critical(self, 'Error !', 'Could not get Printer options', QMessageBox.Close)
            return QDialog.accept(self)

        self.qualityCombo.clear()
        self.paperTypeCombo.clear()
        self.paperSizeCombo.clear()
        # add supported items
        self.qualityCombo.addItems(printer.quality_names)
        self.paperTypeCombo.addItems(printer.papertype_names)
        self.paperSizeCombo.addItems(printer.papersize_names)
        # set default values
        self.colorModeCombo.setCurrentIndex(printer.colormode_index)
        self.qualityCombo.setCurrentIndex(printer.quality_index)
        self.paperTypeCombo.setCurrentIndex(printer.papertype_index)
        self.paperSizeCombo.setCurrentIndex(printer.papersize_index)

    def onPaperSizeChange(self, index):
        hide_custom = self.paperSizeCombo.currentText()!="Custom"
        self.widthSpin.setHidden(hide_custom)
        self.heightSpin.setHidden(hide_custom)

    def onDensityBtnClick(self, checked):
        self.ppiSpin.setEnabled(checked)
        self.naturalScalingSpin.setEnabled(checked)

    def accept(self):
        if self.printersCombo.count()==0:
            return
        # get filenames from commandline args, if not then get from file chooser
        filenames = []
        if len(sys.argv)>1 :
            for each in sys.argv[1:]:
                if os.path.exists(each):
                    filenames.append(os.path.abspath(each))
        if filenames == []:
            files, _filter = QFileDialog.getOpenFileNames(self, 'Select Files to Print')
            if list(files) == [] : return
            for each in files:
                filenames.append(each)

        ext = os.path.splitext(filenames[0])[1].lower()
        image_printing = ext==".jpg" or ext==".jpeg"

        # set printer specific options
        printer_name = self.printersCombo.currentText()
        run_command("lpoptions", ["-d", printer_name])
        printer = printer_from_name(printer_name)
        colormode_index = self.colorModeCombo.currentIndex()
        quality_index = self.qualityCombo.currentIndex()
        papertype_index = self.paperTypeCombo.currentIndex()
        papersize_index = self.paperSizeCombo.currentIndex()
        custom_size = [self.widthSpin.value(), self.heightSpin.value()]# in millimeter
        if not printer.setOptions(colormode_index, quality_index, papertype_index, papersize_index, custom_size):
            QMessageBox.critical(self, 'Error !', 'Could not set printer options', QMessageBox.Close)
            return QDialog.accept(self)
        # get printing options
        lp_args = ['-d', printer_name]

        # General options
        copies = self.copiesSpin.value()
        if copies>1 :
            lp_args += ['-n', str(copies), '-o', 'collate=true']
        # removed -o brightness=100 option, as epson printers do not support
        lp_args += ['-o', 'gamma=%i'%self.gammaSpin.value()]
        # Image printing options
        if image_printing:
            if self.pixelDensityBtn.isChecked():
                lp_args += ['-o', 'ppi=%i'%self.ppiSpin.value(), '-o', 'natural-scaling=%i'%self.naturalScalingSpin.value()]
            else:
                lp_args += ['-o', 'scaling=%i'%self.scalingSpin.value()]
            # position is always left aligned
            positions = ['top', 'center', 'bottom']
            lp_args += ['-o', 'position='+positions[self.positionCombo.currentIndex()]]
        else :
            # Document printing options
            if not self.pageSetAll.isChecked():
                page_set = 'odd' if self.pageSetOdd.isChecked() else 'even'
                lp_args += ['-o', 'page-set='+page_set]
            if self.pagerangeEdit.text()!="":
                lp_args += ['-o', 'page-ranges='+self.pagerangeEdit.text()]
            # reverse pages so that first page will be on top
            if self.reverseBtn.isChecked() or self.pageSetAll.isChecked() and self.pagerangeEdit.text()=="":
                lp_args += ["-o", "outputorder=reverse"]
            # scale page to fit inside print margin
            if self.fitToPageBtn.isChecked():
                lp_args += ['-o', 'fit-to-page']
        # call printing command
        print('lp', ' '.join(lp_args))
        ret = QProcess.execute('lp', lp_args + ['--'] + filenames)
        if ret<0:
            QMessageBox.critical(self, 'Error !', 'Error : Could not execute lp', QMessageBox.Close)
        self.saveSettings()
        QDialog.accept(self)

    def getPrinters(self):
        ''' Get the list of available printers '''
        output = run_command('lpstat', ['-a'])
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
        output = run_command('lpstat', ['-o'])
        if output == '': return
        lines = output.split('\n')
        for line in lines:
            job_id = line.split(' ')[0]
            subprocess.Popen(['cancel', job_id])

    def saveSettings(self):
        self.settings.setValue("FitToPage", self.fitToPageBtn.isChecked())
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
        option, values = line.split(':')
        option = option.split('/')[0]
        values = values.split()
        for value in values:
            if value.startswith('*'):
                value_dict[option] = value[1:]
    return value_dict

# return the index of value in supported_values
# if value not in supported_values return 0
def getValueIndex(options, supported_values, key):
    if not key in options:
        return 0
    val = options[key]
    if val in supported_values:
        return supported_values.index(val)
    return 0


class DummyPrinter:
    def __init__(self, printer_device):
        self.printer = printer_device
        self.color_modes = ['Gray', 'Color']
        self.quality_modes = ['Normal']
        self.paper_types = ['Plain'] # MediaType
        self.paper_sizes = ['A4', 'A5', 'Letter', 'Legal'] # PageSize
        # following values are used by the main dialog
        self.quality_names = ['Normal']
        self.papertype_names = ["Plain"]
        self.papersize_names = ['A4', 'A5', 'Letter', 'Legal']
        self.colormode_index = 0
        self.quality_index = 0
        self.papertype_index = 0
        self.papersize_index = 0
        print("using dummy printer")

    @staticmethod
    def supportsDevice(device_name, uri):
        return True

    def getOptions(self):
        return True

    def setOptions(self, color_print, quality_index, papersize_index, custom_size=[]):
        return True


class HP_DeskJet:
    ''' Handles HP Inkjet printer specific options '''
    def __init__(self, printer_device):
        self.printer = printer_device
        self.color_modes = ['KGray', 'RGB']  # ColorModel
        self.quality_modes = ['FastDraft', 'Normal', 'Best', 'Photo'] # OutputMode
        self.paper_types = ['Plain', 'Glossy'] # MediaType
        self.paper_sizes = ['A4', 'A5', 'A6', 'Letter', 'Legal', 'Custom.WIDTHxHEIGHT'] # PageSize
        # following values are used by the main dialog
        self.quality_names = ['Eco', 'Normal', 'Fine', 'Photo']
        self.papertype_names = ["Plain", "Photo"]
        self.papersize_names = ['A4', 'A5', 'A6', 'Letter', 'Legal', 'Custom']
        self.colormode_index = 0
        self.quality_index = 0
        self.papertype_index = 0
        self.papersize_index = 0

    @staticmethod
    def supportsDevice(device_name, uri):
        # in debian 10, hp:/usb/DeskJet_2130_series?serial=CN8BK484PD065Z
        # in debian 12, usb://HP/DeskJet%202130%20series?serial=CN8BK484PD065Z&interface=1
        return "DeskJet" in uri

    def getOptions(self):
        #print('lpoptions -p %s -l'%self.printer)
        output = run_command('lpoptions', ['-p', self.printer, '-l'])
        if output == "" :
            return False
        try:
            options = parseOptions(output)
            self.colormode_index = getValueIndex(options, self.color_modes, "ColorModel")
            self.quality_index = getValueIndex(options, self.quality_modes, 'OutputMode')
            # commented out, to always use plain paper when startup
            # self.papertype_index = getValueIndex(options, self.paper_types, 'MediaType')
            self.papersize_index = getValueIndex(options, self.paper_sizes, 'PageSize')
        except:
            return False
        return True

    def setOptions(self, colormode_index, quality_index, papertype_index, papersize_index, custom_size=[]):
        color_mode = self.color_modes[colormode_index]
        quality = self.quality_modes[quality_index]
        paper_type = self.paper_types[papertype_index]
        paper_size = self.paper_sizes[papersize_index]

        if paper_size == 'Custom.WIDTHxHEIGHT':
            paper_size = 'Custom.%ix%imm'%(custom_size[0], custom_size[1])

        lpoptions_args = ['-p', self.printer,
                        '-o', 'ColorModel='+color_mode, '-o', 'OutputMode='+quality,
                        '-o', "MediaType="+paper_type, '-o', 'PageSize='+paper_size]

        print('lpoptions', ' '.join(lpoptions_args))
        process = QProcess()
        process.start('lpoptions', lpoptions_args)
        if not process.waitForFinished():
            print("Error : Could not execute lpoptions")
            return False
        return True


class Brother_Inktank:
    ''' Handles printer specific options '''
    def __init__(self, printer_device):
        self.printer = printer_device
        self.color_modes = ['Mono', 'FullColor'] # BRMonoColor
        self.quality_modes = ['Draft', 'Normal', 'Fine'] # BRResolution
        self.paper_types = ['Plain', 'Glossy', 'Inkjet'] # BRMediaType
        self.paper_sizes = ['A4', 'A5', 'Letter', 'Legal', 'BrPostC4x6_S', 'BrPostC4x6_B', 'BrA4_B'] # # PageSize
        # following values are displayed by dialog
        self.quality_names = ['Eco', 'Normal', 'Fine']
        self.papertype_names = ["Plain", "Photo", "Inkjet"]
        self.papersize_names = ['A4', 'A5', 'Letter', 'Legal', '4R', '4R (Borderless)', 'A4 (Borderless)']
        self.colormode_index = 0
        self.quality_index = 0
        self.papertype_index = 0
        self.papersize_index = 0

    @staticmethod
    def supportsDevice(device_name, uri):
        # usb://Brother/DCP-T420W?serial=E80718H1H136313
        # ipp://BrotherT420W.local:631/ipp/print (except IPP Everywhere driver)
        if "://Brother" in uri:
            return True
        return False


    def getOptions(self):
        #print('lpoptions -p %s -l'%self.printer)
        output = run_command('lpoptions', ['-p', self.printer, '-l'])
        if output == "" :
            return False
        try:
            options = parseOptions(output)
            self.colormode_index = getValueIndex(options, self.color_modes, "BRMonoColor")
            self.quality_index = getValueIndex(options, self.quality_modes, 'BRResolution')
            # commented out, to always use plain paper when startup
            #self.papertype_index = getValueIndex(options, self.paper_types, 'BRMediaType')
            self.papersize_index = getValueIndex(options, self.paper_sizes, 'PageSize')
        except:
            return False
        return True

    def setOptions(self, colormode_index, quality_index, papertype_index, papersize_index, custom_size=[]):
        color_mode = self.color_modes[colormode_index]
        quality = self.quality_modes[quality_index]
        paper_type = self.paper_types[papertype_index]
        paper_size = self.paper_sizes[papersize_index]

        lpoptions_args = ['-p', self.printer,
                        '-o', 'BRMonoColor='+color_mode, '-o', 'BRResolution='+quality,
                        '-o', "BRMediaType="+paper_type, '-o', 'PageSize='+paper_size]

        print('lpoptions', ' '.join(lpoptions_args))
        process = QProcess()
        process.start('lpoptions', lpoptions_args)
        if not process.waitForFinished():
            print("Error : Could not execute lpoptions")
            return False
        return True



class Canon_Inktank:
    ''' Handles printer specific options '''
    def __init__(self, printer_device):
        self.printer = printer_device
        self.color_modes = ['True', 'False'] # CNGrayscale
        self.quality_modes = ['Normal']
        self.paper_types = ['plain', 'photopaper', 'matte'] # MediaType
        self.paper_sizes = ['A4', 'A5', 'Letter', 'legal', '4x6', '4x6.bl', 'A4.bl'] # # PageSize
        # following values are displayed by dialog
        self.quality_names = ['Normal']
        self.papertype_names = ["Plain", "Photo Paper", "Matte"]
        self.papersize_names = ['A4', 'A5', 'Letter', 'Legal', '4R', '4R (Borderless)', 'A4 (Borderless)']
        self.colormode_index = 0
        self.quality_index = 0
        self.papertype_index = 0
        self.papersize_index = 0

    @staticmethod
    def supportsDevice(device_name, uri):
        # usb://Canon/G3010%20series?serial=221C89&interface=1
        # ipps://Canon%20G3010%20series._ipps._tcp.local/
        if "://Canon" in uri:
            return True
        return False


    def getOptions(self):
        #print('lpoptions -p %s -l'%self.printer)
        output = run_command('lpoptions', ['-p', self.printer, '-l'])
        if output == "" :
            return False
        try:
            options = parseOptions(output)
            self.colormode_index = getValueIndex(options, self.color_modes, "CNGrayscale")
            #self.quality_index = 0
            # commented out, to always use plain paper when startup
            #self.papertype_index = getValueIndex(options, self.paper_types, 'MediaType')
            self.papersize_index = getValueIndex(options, self.paper_sizes, 'PageSize')
        except:
            return False
        return True

    def setOptions(self, colormode_index, quality_index, papertype_index, papersize_index, custom_size=[]):
        color_mode = self.color_modes[colormode_index]
        #quality = self.quality_modes[quality_index]
        paper_type = self.paper_types[papertype_index]
        paper_size = self.paper_sizes[papersize_index]

        lpoptions_args = ['-p', self.printer,
                        '-o', 'CNGrayscale='+color_mode,
                        '-o', "MediaType="+paper_type, '-o', 'PageSize='+paper_size]

        print('lpoptions', ' '.join(lpoptions_args))
        process = QProcess()
        process.start('lpoptions', lpoptions_args)
        if not process.waitForFinished():
            print("Error : Could not execute lpoptions")
            return False
        return True




class Epson_Ecotank:
    ''' Handles printer specific options (Handles both USB and WiFi)'''
    def __init__(self, printer_device):
        self.printer = printer_device
        self.color_modes = ['MONO', 'COLOR'] # Ink
        self.media_types = ['PLAIN_HIGH', 'PLAIN_NORMAL', # Plain Paper
                            'SFINE_HIGH', 'SFINE_NORMAL', # Epson Photo Quality Ink Jet
                            'PMMATT_HIGH', 'PMMATT_NORMAL', # Epson Matte
                            'PLATINA_HIGH', 'PLATINA_NORMAL', # Epson Ultra Glossy
                            'PMPHOTO_HIGH', 'PMPHOTO_NORMAL', # Epson Premium Glossy
                            'PSGLOS_HIGH', 'PSGLOS_NORMAL', # Epson Premium Semigloss
                            'LCPP_HIGH', 'LCPP_NORMAL', # Photo Paper Glossy
                            'ENV_HIGH', 'ENV_NORMAL', # Envelop
        ]
        self.paper_sizes = ['A4', 'A5', 'A6', 'Letter', 'Legal', '4X6FULL', 'T4X6FULL'] # PageSize
        # following values are used by dialog
        self.quality_names = ['High', 'Normal']
        self.papertype_names = ["Plain", "InkJet", "Matte", "Ultra Glossy",
                                "Premium Glossy", "Premium Semigloss", "Photo", "Envelop"]
        self.papersize_names = ['A4', 'A5', 'A6', 'Letter', 'Legal', '4R', '4R (Borderless)']
        self.colormode_index = 0
        self.quality_index = 0
        self.papertype_index = 0
        self.papersize_index = 0

    @staticmethod
    def supportsDevice(device_name, uri):
        return "://EPSON" in uri


    def getOptions(self):
        #print('lpoptions -p %s -l'%self.printer)
        output = run_command('lpoptions', ['-p', self.printer, '-l'])
        if output == "" :
            return False
        try:
            options = parseOptions(output)
            self.colormode_index = getValueIndex(options, self.color_modes, "Ink")
            mediatype_index = getValueIndex(options, self.media_types, 'MediaType')
            self.quality_index = mediatype_index%2
            # commented out, to always use plain paper when startup
            #self.papertype_index = mediatype_index//2
            self.papersize_index = getValueIndex(options, self.paper_sizes, 'PageSize')
        except:
            return False
        return True

    def setOptions(self, colormode_index, quality_index, papertype_index, papersize_index, custom_size=[]):
        color_mode = self.color_modes[colormode_index]
        media_type = self.media_types[papertype_index*2 + quality_index]
        paper_size = self.paper_sizes[papersize_index]

        lpoptions_args = ['-p', self.printer,
                        '-o', 'Ink='+color_mode,
                        '-o', "MediaType="+media_type, '-o', 'PageSize='+paper_size]

        print('lpoptions', ' '.join(lpoptions_args))
        process = QProcess()
        process.start('lpoptions', lpoptions_args)
        if not process.waitForFinished():
            print("Error : Could not execute lpoptions")
            return False
        return True



def printer_from_name(name):
    # output is like -
    # "device for DeskJet_2130: hp:/usb/DeskJet_2130_series?serial=CN8BK484PD065Z"
    output = run_command('lpstat', ['-v', name])
    if output == "" :
        return DummyPrinter(name)
    uri = output.split()[-1]
    for printer_class in (HP_DeskJet, Brother_Inktank, Epson_Ecotank, Canon_Inktank):
        if printer_class.supportsDevice(name, uri):
            return printer_class(name)
    return DummyPrinter(name)


def run_command(cmd, args):
    process = QProcess()
    process.start(cmd, args)
    if not process.waitForFinished():
        return ""
    output = process.readAllStandardOutput()
    return fromByteArray(output).strip()

def get_default_printer():
    output = run_command("lpstat", ["-d"])
    if output.startswith("system default destination:"):
        return output.split(":")[1].strip()
    return ""

def main():
    app = QApplication(sys.argv)
    app.setOrganizationName("quikprint")
    app.setApplicationName("quikprint")
    win = Window()
    win.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

