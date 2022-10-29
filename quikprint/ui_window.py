# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'files/window.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(640, 505)
        self.gridLayout_4 = QtWidgets.QGridLayout(Dialog)
        self.gridLayout_4.setContentsMargins(-1, -1, -1, 2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setObjectName("label_7")
        self.gridLayout_4.addWidget(self.label_7, 0, 0, 1, 1)
        self.printersCombo = QtWidgets.QComboBox(Dialog)
        self.printersCombo.setObjectName("printersCombo")
        self.gridLayout_4.addWidget(self.printersCombo, 0, 1, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)
        self.copiesSpin = QtWidgets.QSpinBox(self.groupBox)
        self.copiesSpin.setAlignment(QtCore.Qt.AlignCenter)
        self.copiesSpin.setMinimum(1)
        self.copiesSpin.setObjectName("copiesSpin")
        self.gridLayout.addWidget(self.copiesSpin, 0, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 3, 0, 1, 1)
        self.pageSetAll = QtWidgets.QRadioButton(self.groupBox)
        self.pageSetAll.setChecked(True)
        self.pageSetAll.setObjectName("pageSetAll")
        self.gridLayout.addWidget(self.pageSetAll, 4, 0, 1, 1)
        self.pageSetOdd = QtWidgets.QRadioButton(self.groupBox)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/odd-page.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pageSetOdd.setIcon(icon)
        self.pageSetOdd.setObjectName("pageSetOdd")
        self.gridLayout.addWidget(self.pageSetOdd, 4, 1, 1, 1)
        self.pageSetEven = QtWidgets.QRadioButton(self.groupBox)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/even-page.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pageSetEven.setIcon(icon1)
        self.pageSetEven.setObjectName("pageSetEven")
        self.gridLayout.addWidget(self.pageSetEven, 4, 2, 1, 1)
        self.pagerangeEdit = QtWidgets.QLineEdit(self.groupBox)
        self.pagerangeEdit.setObjectName("pagerangeEdit")
        self.gridLayout.addWidget(self.pagerangeEdit, 2, 1, 1, 2)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.reverseBtn = QtWidgets.QCheckBox(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.reverseBtn.sizePolicy().hasHeightForWidth())
        self.reverseBtn.setSizePolicy(sizePolicy)
        self.reverseBtn.setObjectName("reverseBtn")
        self.gridLayout.addWidget(self.reverseBtn, 5, 0, 1, 1)
        self.gridLayout_4.addWidget(self.groupBox, 1, 0, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.qualityCombo = QtWidgets.QComboBox(self.groupBox_2)
        self.qualityCombo.setObjectName("qualityCombo")
        self.gridLayout_2.addWidget(self.qualityCombo, 2, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 2, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.paperSizeCombo = QtWidgets.QComboBox(self.groupBox_2)
        self.paperSizeCombo.setObjectName("paperSizeCombo")
        self.gridLayout_2.addWidget(self.paperSizeCombo, 4, 1, 1, 1)
        self.widthSpin = QtWidgets.QSpinBox(self.groupBox_2)
        self.widthSpin.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.widthSpin.setMaximum(400)
        self.widthSpin.setProperty("value", 101)
        self.widthSpin.setObjectName("widthSpin")
        self.gridLayout_2.addWidget(self.widthSpin, 5, 0, 1, 1)
        self.heightSpin = QtWidgets.QSpinBox(self.groupBox_2)
        self.heightSpin.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.heightSpin.setMaximum(400)
        self.heightSpin.setProperty("value", 152)
        self.heightSpin.setObjectName("heightSpin")
        self.gridLayout_2.addWidget(self.heightSpin, 5, 1, 1, 1)
        self.fitToPageBtn = QtWidgets.QCheckBox(self.groupBox_2)
        self.fitToPageBtn.setObjectName("fitToPageBtn")
        self.gridLayout_2.addWidget(self.fitToPageBtn, 6, 0, 1, 2)
        self.label_11 = QtWidgets.QLabel(self.groupBox_2)
        self.label_11.setObjectName("label_11")
        self.gridLayout_2.addWidget(self.label_11, 3, 0, 1, 1)
        self.paperTypeCombo = QtWidgets.QComboBox(self.groupBox_2)
        self.paperTypeCombo.setObjectName("paperTypeCombo")
        self.gridLayout_2.addWidget(self.paperTypeCombo, 3, 1, 1, 1)
        self.colorModeCombo = QtWidgets.QComboBox(self.groupBox_2)
        self.colorModeCombo.setObjectName("colorModeCombo")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/grayscale.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.colorModeCombo.addItem(icon2, "")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/color.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.colorModeCombo.addItem(icon3, "")
        self.gridLayout_2.addWidget(self.colorModeCombo, 0, 1, 1, 1)
        self.gridLayout_4.addWidget(self.groupBox_2, 1, 1, 1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_8 = QtWidgets.QLabel(self.groupBox_3)
        self.label_8.setObjectName("label_8")
        self.gridLayout_3.addWidget(self.label_8, 0, 0, 1, 1)
        self.scalingSpin = QtWidgets.QSpinBox(self.groupBox_3)
        self.scalingSpin.setAlignment(QtCore.Qt.AlignCenter)
        self.scalingSpin.setMinimum(5)
        self.scalingSpin.setMaximum(800)
        self.scalingSpin.setProperty("value", 100)
        self.scalingSpin.setObjectName("scalingSpin")
        self.gridLayout_3.addWidget(self.scalingSpin, 0, 1, 1, 2)
        self.label_9 = QtWidgets.QLabel(self.groupBox_3)
        self.label_9.setObjectName("label_9")
        self.gridLayout_3.addWidget(self.label_9, 0, 3, 1, 1)
        self.positionCombo = QtWidgets.QComboBox(self.groupBox_3)
        self.positionCombo.setObjectName("positionCombo")
        self.positionCombo.addItem("")
        self.positionCombo.addItem("")
        self.positionCombo.addItem("")
        self.gridLayout_3.addWidget(self.positionCombo, 0, 4, 1, 1)
        self.pixelDensityBtn = QtWidgets.QCheckBox(self.groupBox_3)
        self.pixelDensityBtn.setObjectName("pixelDensityBtn")
        self.gridLayout_3.addWidget(self.pixelDensityBtn, 1, 0, 1, 2)
        self.ppiSpin = QtWidgets.QSpinBox(self.groupBox_3)
        self.ppiSpin.setEnabled(False)
        self.ppiSpin.setAlignment(QtCore.Qt.AlignCenter)
        self.ppiSpin.setMinimum(100)
        self.ppiSpin.setMaximum(1200)
        self.ppiSpin.setProperty("value", 300)
        self.ppiSpin.setObjectName("ppiSpin")
        self.gridLayout_3.addWidget(self.ppiSpin, 1, 2, 1, 1)
        self.naturalScalingSpin = QtWidgets.QSpinBox(self.groupBox_3)
        self.naturalScalingSpin.setEnabled(False)
        self.naturalScalingSpin.setAlignment(QtCore.Qt.AlignCenter)
        self.naturalScalingSpin.setMaximum(400)
        self.naturalScalingSpin.setProperty("value", 100)
        self.naturalScalingSpin.setObjectName("naturalScalingSpin")
        self.gridLayout_3.addWidget(self.naturalScalingSpin, 1, 3, 1, 1)
        self.gridLayout_4.addWidget(self.groupBox_3, 2, 0, 1, 2)
        self.groupBox_4 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_4.setObjectName("groupBox_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_2.setSpacing(40)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_5 = QtWidgets.QLabel(self.groupBox_4)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        self.brightnessSpin = QtWidgets.QSpinBox(self.groupBox_4)
        self.brightnessSpin.setAlignment(QtCore.Qt.AlignCenter)
        self.brightnessSpin.setMinimum(10)
        self.brightnessSpin.setMaximum(200)
        self.brightnessSpin.setSingleStep(5)
        self.brightnessSpin.setProperty("value", 100)
        self.brightnessSpin.setObjectName("brightnessSpin")
        self.horizontalLayout_2.addWidget(self.brightnessSpin)
        self.label_10 = QtWidgets.QLabel(self.groupBox_4)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_2.addWidget(self.label_10)
        self.gammaSpin = QtWidgets.QSpinBox(self.groupBox_4)
        self.gammaSpin.setAlignment(QtCore.Qt.AlignCenter)
        self.gammaSpin.setMinimum(250)
        self.gammaSpin.setMaximum(4000)
        self.gammaSpin.setSingleStep(10)
        self.gammaSpin.setProperty("value", 1000)
        self.gammaSpin.setObjectName("gammaSpin")
        self.horizontalLayout_2.addWidget(self.gammaSpin)
        self.gridLayout_4.addWidget(self.groupBox_4, 3, 0, 1, 2)
        self.widget = QtWidgets.QWidget(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.cancelJobsBtn = QtWidgets.QPushButton(self.widget)
        icon = QtGui.QIcon.fromTheme("edit-clear")
        self.cancelJobsBtn.setIcon(icon)
        self.cancelJobsBtn.setIconSize(QtCore.QSize(24, 24))
        self.cancelJobsBtn.setObjectName("cancelJobsBtn")
        self.horizontalLayout.addWidget(self.cancelJobsBtn)
        spacerItem = QtWidgets.QSpacerItem(435, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.quitBtn = QtWidgets.QPushButton(self.widget)
        icon = QtGui.QIcon.fromTheme("process-stop")
        self.quitBtn.setIcon(icon)
        self.quitBtn.setObjectName("quitBtn")
        self.horizontalLayout.addWidget(self.quitBtn)
        self.printBtn = QtWidgets.QPushButton(self.widget)
        icon = QtGui.QIcon.fromTheme("document-print")
        self.printBtn.setIcon(icon)
        self.printBtn.setDefault(True)
        self.printBtn.setObjectName("printBtn")
        self.horizontalLayout.addWidget(self.printBtn)
        self.gridLayout_4.addWidget(self.widget, 4, 0, 1, 2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Quik Print"))
        self.label_7.setText(_translate("Dialog", "Select Printer :"))
        self.groupBox.setTitle(_translate("Dialog", "Job Options"))
        self.label_4.setText(_translate("Dialog", "Copies :"))
        self.label_6.setText(_translate("Dialog", "Page Set :"))
        self.pageSetAll.setText(_translate("Dialog", "All"))
        self.pageSetOdd.setText(_translate("Dialog", "Odd"))
        self.pageSetEven.setText(_translate("Dialog", "Even"))
        self.pagerangeEdit.setPlaceholderText(_translate("Dialog", "e.g. = 1,2,5-9,14"))
        self.label_3.setText(_translate("Dialog", "Page Ranges :"))
        self.reverseBtn.setText(_translate("Dialog", "Reverse"))
        self.groupBox_2.setTitle(_translate("Dialog", "Output"))
        self.label_2.setText(_translate("Dialog", "Quality :"))
        self.label.setText(_translate("Dialog", "Color Mode :"))
        self.widthSpin.setSuffix(_translate("Dialog", " mm W"))
        self.heightSpin.setSuffix(_translate("Dialog", " mm H"))
        self.fitToPageBtn.setText(_translate("Dialog", "Fit to Page"))
        self.label_11.setText(_translate("Dialog", "Paper Type :"))
        self.colorModeCombo.setItemText(0, _translate("Dialog", "Gray"))
        self.colorModeCombo.setItemText(1, _translate("Dialog", "Color"))
        self.groupBox_3.setTitle(_translate("Dialog", "Image Printing"))
        self.label_8.setText(_translate("Dialog", "Scaling :"))
        self.scalingSpin.setSuffix(_translate("Dialog", " % of page"))
        self.label_9.setText(_translate("Dialog", "Position :"))
        self.positionCombo.setItemText(0, _translate("Dialog", "Top"))
        self.positionCombo.setItemText(1, _translate("Dialog", "Center"))
        self.positionCombo.setItemText(2, _translate("Dialog", "Bottom"))
        self.pixelDensityBtn.setText(_translate("Dialog", "Use Pixel Density"))
        self.ppiSpin.setSuffix(_translate("Dialog", " ppi"))
        self.naturalScalingSpin.setSuffix(_translate("Dialog", " %"))
        self.groupBox_4.setTitle(_translate("Dialog", "Lightness"))
        self.label_5.setText(_translate("Dialog", "Brightness :"))
        self.brightnessSpin.setSuffix(_translate("Dialog", " %"))
        self.label_10.setText(_translate("Dialog", "Gamma :"))
        self.cancelJobsBtn.setText(_translate("Dialog", "Cancel Print Jobs"))
        self.quitBtn.setText(_translate("Dialog", "Quit"))
        self.printBtn.setText(_translate("Dialog", "Print"))

import resources_rc
