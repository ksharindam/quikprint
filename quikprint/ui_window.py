# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'files/window.ui'
#
# Created by: PyQt4 UI code generator 4.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(640, 516)
        self.gridLayout_4 = QtGui.QGridLayout(Dialog)
        self.gridLayout_4.setContentsMargins(-1, -1, -1, 2)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.label_7 = QtGui.QLabel(Dialog)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout_4.addWidget(self.label_7, 0, 0, 1, 1)
        self.printersCombo = QtGui.QComboBox(Dialog)
        self.printersCombo.setObjectName(_fromUtf8("printersCombo"))
        self.gridLayout_4.addWidget(self.printersCombo, 0, 1, 1, 1)
        self.groupBox = QtGui.QGroupBox(Dialog)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout = QtGui.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)
        self.copiesSpin = QtGui.QSpinBox(self.groupBox)
        self.copiesSpin.setAlignment(QtCore.Qt.AlignCenter)
        self.copiesSpin.setMinimum(1)
        self.copiesSpin.setObjectName(_fromUtf8("copiesSpin"))
        self.gridLayout.addWidget(self.copiesSpin, 0, 1, 1, 1)
        self.label_6 = QtGui.QLabel(self.groupBox)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 4, 0, 1, 1)
        self.pageSetAll = QtGui.QRadioButton(self.groupBox)
        self.pageSetAll.setChecked(True)
        self.pageSetAll.setObjectName(_fromUtf8("pageSetAll"))
        self.gridLayout.addWidget(self.pageSetAll, 5, 0, 1, 1)
        self.pageSetOdd = QtGui.QRadioButton(self.groupBox)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/odd-page.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pageSetOdd.setIcon(icon)
        self.pageSetOdd.setObjectName(_fromUtf8("pageSetOdd"))
        self.gridLayout.addWidget(self.pageSetOdd, 5, 1, 1, 1)
        self.pageSetEven = QtGui.QRadioButton(self.groupBox)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/even-page.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pageSetEven.setIcon(icon1)
        self.pageSetEven.setObjectName(_fromUtf8("pageSetEven"))
        self.gridLayout.addWidget(self.pageSetEven, 5, 2, 1, 1)
        self.pagerangeEdit = QtGui.QLineEdit(self.groupBox)
        self.pagerangeEdit.setEnabled(False)
        self.pagerangeEdit.setObjectName(_fromUtf8("pagerangeEdit"))
        self.gridLayout.addWidget(self.pagerangeEdit, 3, 1, 1, 2)
        self.allPagesBtn = QtGui.QRadioButton(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.allPagesBtn.sizePolicy().hasHeightForWidth())
        self.allPagesBtn.setSizePolicy(sizePolicy)
        self.allPagesBtn.setObjectName(_fromUtf8("allPagesBtn"))
        self.gridLayout.addWidget(self.allPagesBtn, 1, 0, 1, 1)
        self.rangeBtn = QtGui.QRadioButton(self.groupBox)
        self.rangeBtn.setObjectName(_fromUtf8("rangeBtn"))
        self.gridLayout.addWidget(self.rangeBtn, 3, 0, 1, 1)
        self.gridLayout_4.addWidget(self.groupBox, 1, 0, 1, 1)
        self.groupBox_2 = QtGui.QGroupBox(Dialog)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.qualityCombo = QtGui.QComboBox(self.groupBox_2)
        self.qualityCombo.setObjectName(_fromUtf8("qualityCombo"))
        self.gridLayout_2.addWidget(self.qualityCombo, 2, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.groupBox_2)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_2.addWidget(self.label_2, 2, 0, 1, 1)
        self.label = QtGui.QLabel(self.groupBox_2)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.paperSizeCombo = QtGui.QComboBox(self.groupBox_2)
        self.paperSizeCombo.setObjectName(_fromUtf8("paperSizeCombo"))
        self.gridLayout_2.addWidget(self.paperSizeCombo, 4, 1, 1, 1)
        self.widthSpin = QtGui.QSpinBox(self.groupBox_2)
        self.widthSpin.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.widthSpin.setMaximum(400)
        self.widthSpin.setProperty("value", 101)
        self.widthSpin.setObjectName(_fromUtf8("widthSpin"))
        self.gridLayout_2.addWidget(self.widthSpin, 5, 0, 1, 1)
        self.heightSpin = QtGui.QSpinBox(self.groupBox_2)
        self.heightSpin.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.heightSpin.setMaximum(400)
        self.heightSpin.setProperty("value", 152)
        self.heightSpin.setObjectName(_fromUtf8("heightSpin"))
        self.gridLayout_2.addWidget(self.heightSpin, 5, 1, 1, 1)
        self.fitToPageBtn = QtGui.QCheckBox(self.groupBox_2)
        self.fitToPageBtn.setObjectName(_fromUtf8("fitToPageBtn"))
        self.gridLayout_2.addWidget(self.fitToPageBtn, 6, 0, 1, 2)
        self.label_11 = QtGui.QLabel(self.groupBox_2)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.gridLayout_2.addWidget(self.label_11, 3, 0, 1, 1)
        self.paperTypeCombo = QtGui.QComboBox(self.groupBox_2)
        self.paperTypeCombo.setObjectName(_fromUtf8("paperTypeCombo"))
        self.gridLayout_2.addWidget(self.paperTypeCombo, 3, 1, 1, 1)
        self.colorModeCombo = QtGui.QComboBox(self.groupBox_2)
        self.colorModeCombo.setObjectName(_fromUtf8("colorModeCombo"))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/grayscale.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.colorModeCombo.addItem(icon2, _fromUtf8(""))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/color.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.colorModeCombo.addItem(icon3, _fromUtf8(""))
        self.gridLayout_2.addWidget(self.colorModeCombo, 0, 1, 1, 1)
        self.gridLayout_4.addWidget(self.groupBox_2, 1, 1, 1, 1)
        self.groupBox_3 = QtGui.QGroupBox(Dialog)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.gridLayout_3 = QtGui.QGridLayout(self.groupBox_3)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.label_8 = QtGui.QLabel(self.groupBox_3)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout_3.addWidget(self.label_8, 0, 0, 1, 1)
        self.scalingSpin = QtGui.QSpinBox(self.groupBox_3)
        self.scalingSpin.setAlignment(QtCore.Qt.AlignCenter)
        self.scalingSpin.setMinimum(5)
        self.scalingSpin.setMaximum(800)
        self.scalingSpin.setProperty("value", 100)
        self.scalingSpin.setObjectName(_fromUtf8("scalingSpin"))
        self.gridLayout_3.addWidget(self.scalingSpin, 0, 1, 1, 2)
        self.label_9 = QtGui.QLabel(self.groupBox_3)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout_3.addWidget(self.label_9, 0, 3, 1, 1)
        self.positionCombo = QtGui.QComboBox(self.groupBox_3)
        self.positionCombo.setObjectName(_fromUtf8("positionCombo"))
        self.positionCombo.addItem(_fromUtf8(""))
        self.positionCombo.addItem(_fromUtf8(""))
        self.positionCombo.addItem(_fromUtf8(""))
        self.gridLayout_3.addWidget(self.positionCombo, 0, 4, 1, 1)
        self.pixelDensityBtn = QtGui.QCheckBox(self.groupBox_3)
        self.pixelDensityBtn.setObjectName(_fromUtf8("pixelDensityBtn"))
        self.gridLayout_3.addWidget(self.pixelDensityBtn, 1, 0, 1, 2)
        self.ppiSpin = QtGui.QSpinBox(self.groupBox_3)
        self.ppiSpin.setEnabled(False)
        self.ppiSpin.setAlignment(QtCore.Qt.AlignCenter)
        self.ppiSpin.setMinimum(100)
        self.ppiSpin.setMaximum(1200)
        self.ppiSpin.setProperty("value", 300)
        self.ppiSpin.setObjectName(_fromUtf8("ppiSpin"))
        self.gridLayout_3.addWidget(self.ppiSpin, 1, 2, 1, 1)
        self.naturalScalingSpin = QtGui.QSpinBox(self.groupBox_3)
        self.naturalScalingSpin.setEnabled(False)
        self.naturalScalingSpin.setAlignment(QtCore.Qt.AlignCenter)
        self.naturalScalingSpin.setMaximum(400)
        self.naturalScalingSpin.setProperty("value", 100)
        self.naturalScalingSpin.setObjectName(_fromUtf8("naturalScalingSpin"))
        self.gridLayout_3.addWidget(self.naturalScalingSpin, 1, 3, 1, 1)
        self.gridLayout_4.addWidget(self.groupBox_3, 2, 0, 1, 2)
        self.groupBox_4 = QtGui.QGroupBox(Dialog)
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_2.setSpacing(40)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_5 = QtGui.QLabel(self.groupBox_4)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_2.addWidget(self.label_5)
        self.brightnessSpin = QtGui.QSpinBox(self.groupBox_4)
        self.brightnessSpin.setAlignment(QtCore.Qt.AlignCenter)
        self.brightnessSpin.setMinimum(10)
        self.brightnessSpin.setMaximum(200)
        self.brightnessSpin.setSingleStep(5)
        self.brightnessSpin.setProperty("value", 100)
        self.brightnessSpin.setObjectName(_fromUtf8("brightnessSpin"))
        self.horizontalLayout_2.addWidget(self.brightnessSpin)
        self.label_10 = QtGui.QLabel(self.groupBox_4)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.horizontalLayout_2.addWidget(self.label_10)
        self.gammaSpin = QtGui.QSpinBox(self.groupBox_4)
        self.gammaSpin.setAlignment(QtCore.Qt.AlignCenter)
        self.gammaSpin.setMinimum(250)
        self.gammaSpin.setMaximum(4000)
        self.gammaSpin.setSingleStep(10)
        self.gammaSpin.setProperty("value", 1000)
        self.gammaSpin.setObjectName(_fromUtf8("gammaSpin"))
        self.horizontalLayout_2.addWidget(self.gammaSpin)
        self.gridLayout_4.addWidget(self.groupBox_4, 3, 0, 1, 2)
        self.widget = QtGui.QWidget(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.cancelJobsBtn = QtGui.QPushButton(self.widget)
        icon = QtGui.QIcon.fromTheme(_fromUtf8("edit-clear"))
        self.cancelJobsBtn.setIcon(icon)
        self.cancelJobsBtn.setIconSize(QtCore.QSize(24, 24))
        self.cancelJobsBtn.setObjectName(_fromUtf8("cancelJobsBtn"))
        self.horizontalLayout.addWidget(self.cancelJobsBtn)
        spacerItem = QtGui.QSpacerItem(435, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.quitBtn = QtGui.QPushButton(self.widget)
        icon = QtGui.QIcon.fromTheme(_fromUtf8("process-stop"))
        self.quitBtn.setIcon(icon)
        self.quitBtn.setObjectName(_fromUtf8("quitBtn"))
        self.horizontalLayout.addWidget(self.quitBtn)
        self.printBtn = QtGui.QPushButton(self.widget)
        icon = QtGui.QIcon.fromTheme(_fromUtf8("document-print"))
        self.printBtn.setIcon(icon)
        self.printBtn.setDefault(True)
        self.printBtn.setObjectName(_fromUtf8("printBtn"))
        self.horizontalLayout.addWidget(self.printBtn)
        self.gridLayout_4.addWidget(self.widget, 4, 0, 1, 2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Quik Print", None))
        self.label_7.setText(_translate("Dialog", "Select Printer :", None))
        self.groupBox.setTitle(_translate("Dialog", "Job Options", None))
        self.label_4.setText(_translate("Dialog", "Copies :", None))
        self.label_6.setText(_translate("Dialog", "Page Set :", None))
        self.pageSetAll.setText(_translate("Dialog", "All", None))
        self.pageSetOdd.setText(_translate("Dialog", "Odd", None))
        self.pageSetEven.setText(_translate("Dialog", "Even", None))
        self.pagerangeEdit.setPlaceholderText(_translate("Dialog", "e.g. = 1,2,5-9,14", None))
        self.allPagesBtn.setText(_translate("Dialog", "All Pages", None))
        self.rangeBtn.setText(_translate("Dialog", "Range", None))
        self.groupBox_2.setTitle(_translate("Dialog", "Output", None))
        self.label_2.setText(_translate("Dialog", "Quality :", None))
        self.label.setText(_translate("Dialog", "Color Mode :", None))
        self.widthSpin.setSuffix(_translate("Dialog", " mm W", None))
        self.heightSpin.setSuffix(_translate("Dialog", " mm H", None))
        self.fitToPageBtn.setText(_translate("Dialog", "Fit to Page", None))
        self.label_11.setText(_translate("Dialog", "Paper Type :", None))
        self.colorModeCombo.setItemText(0, _translate("Dialog", "Gray", None))
        self.colorModeCombo.setItemText(1, _translate("Dialog", "Color", None))
        self.groupBox_3.setTitle(_translate("Dialog", "Image Printing", None))
        self.label_8.setText(_translate("Dialog", "Scaling :", None))
        self.scalingSpin.setSuffix(_translate("Dialog", " % of page", None))
        self.label_9.setText(_translate("Dialog", "Position :", None))
        self.positionCombo.setItemText(0, _translate("Dialog", "Top", None))
        self.positionCombo.setItemText(1, _translate("Dialog", "Center", None))
        self.positionCombo.setItemText(2, _translate("Dialog", "Bottom", None))
        self.pixelDensityBtn.setText(_translate("Dialog", "Use Pixel Density", None))
        self.ppiSpin.setSuffix(_translate("Dialog", " ppi", None))
        self.naturalScalingSpin.setSuffix(_translate("Dialog", " %", None))
        self.groupBox_4.setTitle(_translate("Dialog", "Lightness", None))
        self.label_5.setText(_translate("Dialog", "Brightness :", None))
        self.brightnessSpin.setSuffix(_translate("Dialog", " %", None))
        self.label_10.setText(_translate("Dialog", "Gamma :", None))
        self.cancelJobsBtn.setText(_translate("Dialog", "Cancel Print Jobs", None))
        self.quitBtn.setText(_translate("Dialog", "Quit", None))
        self.printBtn.setText(_translate("Dialog", "Print", None))

import resources_rc
