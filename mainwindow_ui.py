# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(606, 344)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("lines.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap("lines.ico"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        icon.addPixmap(QtGui.QPixmap("lines.ico"), QtGui.QIcon.Disabled, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap("lines.ico"), QtGui.QIcon.Disabled, QtGui.QIcon.On)
        icon.addPixmap(QtGui.QPixmap("lines.ico"), QtGui.QIcon.Active, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap("lines.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        icon.addPixmap(QtGui.QPixmap("lines.ico"), QtGui.QIcon.Selected, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap("lines.ico"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.owenName_1 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.owenName_1.setFont(font)
        self.owenName_1.setObjectName("owenName_1")
        self.verticalLayout.addWidget(self.owenName_1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.portLabel_1 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.portLabel_1.setFont(font)
        self.portLabel_1.setObjectName("portLabel_1")
        self.horizontalLayout.addWidget(self.portLabel_1)
        spacerItem = QtWidgets.QSpacerItem(33, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.portNumber_1 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.portNumber_1.setFont(font)
        self.portNumber_1.setObjectName("portNumber_1")
        self.horizontalLayout.addWidget(self.portNumber_1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.tempNameLable_1 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tempNameLable_1.setFont(font)
        self.tempNameLable_1.setObjectName("tempNameLable_1")
        self.horizontalLayout_3.addWidget(self.tempNameLable_1)
        spacerItem1 = QtWidgets.QSpacerItem(35, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.tempLable_1 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tempLable_1.setFont(font)
        self.tempLable_1.setStyleSheet("")
        self.tempLable_1.setObjectName("tempLable_1")
        self.horizontalLayout_3.addWidget(self.tempLable_1)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.statusNameLabel_1 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.statusNameLabel_1.setFont(font)
        self.statusNameLabel_1.setObjectName("statusNameLabel_1")
        self.horizontalLayout_2.addWidget(self.statusNameLabel_1)
        spacerItem2 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.statusLabel_1 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.statusLabel_1.setFont(font)
        self.statusLabel_1.setStyleSheet("color: rgb(255, 0, 0);")
        self.statusLabel_1.setObjectName("statusLabel_1")
        self.horizontalLayout_2.addWidget(self.statusLabel_1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.reportButton_1 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.reportButton_1.setFont(font)
        self.reportButton_1.setObjectName("reportButton_1")
        self.verticalLayout.addWidget(self.reportButton_1)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.owenName_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.owenName_2.setFont(font)
        self.owenName_2.setObjectName("owenName_2")
        self.verticalLayout_2.addWidget(self.owenName_2)
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.portLabel_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.portLabel_2.setFont(font)
        self.portLabel_2.setObjectName("portLabel_2")
        self.horizontalLayout_17.addWidget(self.portLabel_2)
        spacerItem3 = QtWidgets.QSpacerItem(33, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_17.addItem(spacerItem3)
        self.portNumber_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.portNumber_2.setFont(font)
        self.portNumber_2.setObjectName("portNumber_2")
        self.horizontalLayout_17.addWidget(self.portNumber_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_17)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.tempNameLable_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tempNameLable_2.setFont(font)
        self.tempNameLable_2.setObjectName("tempNameLable_2")
        self.horizontalLayout_12.addWidget(self.tempNameLable_2)
        spacerItem4 = QtWidgets.QSpacerItem(35, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem4)
        self.tempLable_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tempLable_2.setFont(font)
        self.tempLable_2.setStyleSheet("")
        self.tempLable_2.setObjectName("tempLable_2")
        self.horizontalLayout_12.addWidget(self.tempLable_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.statusNameLabel_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.statusNameLabel_2.setFont(font)
        self.statusNameLabel_2.setObjectName("statusNameLabel_2")
        self.horizontalLayout_18.addWidget(self.statusNameLabel_2)
        spacerItem5 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_18.addItem(spacerItem5)
        self.statusLabel_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.statusLabel_2.setFont(font)
        self.statusLabel_2.setStyleSheet("color: rgb(255, 0, 0);")
        self.statusLabel_2.setObjectName("statusLabel_2")
        self.horizontalLayout_18.addWidget(self.statusLabel_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_18)
        self.reportButton_2 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.reportButton_2.setFont(font)
        self.reportButton_2.setObjectName("reportButton_2")
        self.verticalLayout_2.addWidget(self.reportButton_2)
        self.line_8 = QtWidgets.QFrame(self.centralwidget)
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.verticalLayout_2.addWidget(self.line_8)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 1, 2, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.owenName_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.owenName_3.setFont(font)
        self.owenName_3.setObjectName("owenName_3")
        self.verticalLayout_3.addWidget(self.owenName_3)
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.portLabel_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.portLabel_3.setFont(font)
        self.portLabel_3.setObjectName("portLabel_3")
        self.horizontalLayout_19.addWidget(self.portLabel_3)
        spacerItem6 = QtWidgets.QSpacerItem(33, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_19.addItem(spacerItem6)
        self.portNumber_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.portNumber_3.setFont(font)
        self.portNumber_3.setObjectName("portNumber_3")
        self.horizontalLayout_19.addWidget(self.portNumber_3)
        self.verticalLayout_3.addLayout(self.horizontalLayout_19)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.tempNameLable_4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tempNameLable_4.setFont(font)
        self.tempNameLable_4.setObjectName("tempNameLable_4")
        self.horizontalLayout_6.addWidget(self.tempNameLable_4)
        spacerItem7 = QtWidgets.QSpacerItem(35, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem7)
        self.tempLable_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tempLable_3.setFont(font)
        self.tempLable_3.setStyleSheet("")
        self.tempLable_3.setObjectName("tempLable_3")
        self.horizontalLayout_6.addWidget(self.tempLable_3)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.statusNameLabel_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.statusNameLabel_3.setFont(font)
        self.statusNameLabel_3.setObjectName("statusNameLabel_3")
        self.horizontalLayout_20.addWidget(self.statusNameLabel_3)
        spacerItem8 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_20.addItem(spacerItem8)
        self.statusLabel_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.statusLabel_3.setFont(font)
        self.statusLabel_3.setStyleSheet("color: rgb(255, 0, 0);")
        self.statusLabel_3.setObjectName("statusLabel_3")
        self.horizontalLayout_20.addWidget(self.statusLabel_3)
        self.verticalLayout_3.addLayout(self.horizontalLayout_20)
        self.reportButton_3 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.reportButton_3.setFont(font)
        self.reportButton_3.setObjectName("reportButton_3")
        self.verticalLayout_3.addWidget(self.reportButton_3)
        self.line_9 = QtWidgets.QFrame(self.centralwidget)
        self.line_9.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.verticalLayout_3.addWidget(self.line_9)
        self.gridLayout.addLayout(self.verticalLayout_3, 0, 2, 2, 1)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.owenName_4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.owenName_4.setFont(font)
        self.owenName_4.setObjectName("owenName_4")
        self.verticalLayout_4.addWidget(self.owenName_4)
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.portLabel_4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.portLabel_4.setFont(font)
        self.portLabel_4.setObjectName("portLabel_4")
        self.horizontalLayout_21.addWidget(self.portLabel_4)
        spacerItem9 = QtWidgets.QSpacerItem(33, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_21.addItem(spacerItem9)
        self.portNumber_4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.portNumber_4.setFont(font)
        self.portNumber_4.setObjectName("portNumber_4")
        self.horizontalLayout_21.addWidget(self.portNumber_4)
        self.verticalLayout_4.addLayout(self.horizontalLayout_21)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.tempNameLable_5 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tempNameLable_5.setFont(font)
        self.tempNameLable_5.setObjectName("tempNameLable_5")
        self.horizontalLayout_7.addWidget(self.tempNameLable_5)
        spacerItem10 = QtWidgets.QSpacerItem(35, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem10)
        self.tempLable_4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tempLable_4.setFont(font)
        self.tempLable_4.setStyleSheet("")
        self.tempLable_4.setObjectName("tempLable_4")
        self.horizontalLayout_7.addWidget(self.tempLable_4)
        self.verticalLayout_4.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_22 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        self.statusNameLabel_4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.statusNameLabel_4.setFont(font)
        self.statusNameLabel_4.setObjectName("statusNameLabel_4")
        self.horizontalLayout_22.addWidget(self.statusNameLabel_4)
        spacerItem11 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_22.addItem(spacerItem11)
        self.statusLabel_4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.statusLabel_4.setFont(font)
        self.statusLabel_4.setStyleSheet("color: rgb(255, 0, 0);")
        self.statusLabel_4.setObjectName("statusLabel_4")
        self.horizontalLayout_22.addWidget(self.statusLabel_4)
        self.verticalLayout_4.addLayout(self.horizontalLayout_22)
        self.reportButton_4 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.reportButton_4.setFont(font)
        self.reportButton_4.setObjectName("reportButton_4")
        self.verticalLayout_4.addWidget(self.reportButton_4)
        self.line_10 = QtWidgets.QFrame(self.centralwidget)
        self.line_10.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_10.setObjectName("line_10")
        self.verticalLayout_4.addWidget(self.line_10)
        self.gridLayout.addLayout(self.verticalLayout_4, 0, 3, 2, 1)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 1, 0, 1, 1)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.owenName_5 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.owenName_5.setFont(font)
        self.owenName_5.setObjectName("owenName_5")
        self.verticalLayout_5.addWidget(self.owenName_5)
        self.horizontalLayout_23 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_23.setObjectName("horizontalLayout_23")
        self.portLabel_5 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.portLabel_5.setFont(font)
        self.portLabel_5.setObjectName("portLabel_5")
        self.horizontalLayout_23.addWidget(self.portLabel_5)
        spacerItem12 = QtWidgets.QSpacerItem(33, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_23.addItem(spacerItem12)
        self.portNumber_5 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.portNumber_5.setFont(font)
        self.portNumber_5.setObjectName("portNumber_5")
        self.horizontalLayout_23.addWidget(self.portNumber_5)
        self.verticalLayout_5.addLayout(self.horizontalLayout_23)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.tempNameLable_6 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tempNameLable_6.setFont(font)
        self.tempNameLable_6.setObjectName("tempNameLable_6")
        self.horizontalLayout_8.addWidget(self.tempNameLable_6)
        spacerItem13 = QtWidgets.QSpacerItem(35, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem13)
        self.tempLable_5 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tempLable_5.setFont(font)
        self.tempLable_5.setStyleSheet("")
        self.tempLable_5.setObjectName("tempLable_5")
        self.horizontalLayout_8.addWidget(self.tempLable_5)
        self.verticalLayout_5.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_24 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_24.setObjectName("horizontalLayout_24")
        self.statusNameLabel_5 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.statusNameLabel_5.setFont(font)
        self.statusNameLabel_5.setObjectName("statusNameLabel_5")
        self.horizontalLayout_24.addWidget(self.statusNameLabel_5)
        spacerItem14 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_24.addItem(spacerItem14)
        self.statusLabel_5 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.statusLabel_5.setFont(font)
        self.statusLabel_5.setStyleSheet("color: rgb(255, 0, 0);")
        self.statusLabel_5.setObjectName("statusLabel_5")
        self.horizontalLayout_24.addWidget(self.statusLabel_5)
        self.verticalLayout_5.addLayout(self.horizontalLayout_24)
        self.reportButton_5 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.reportButton_5.setFont(font)
        self.reportButton_5.setObjectName("reportButton_5")
        self.verticalLayout_5.addWidget(self.reportButton_5)
        self.gridLayout.addLayout(self.verticalLayout_5, 2, 0, 1, 1)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.owenName_6 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.owenName_6.setFont(font)
        self.owenName_6.setObjectName("owenName_6")
        self.verticalLayout_6.addWidget(self.owenName_6)
        self.horizontalLayout_25 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_25.setObjectName("horizontalLayout_25")
        self.portLabel_6 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.portLabel_6.setFont(font)
        self.portLabel_6.setObjectName("portLabel_6")
        self.horizontalLayout_25.addWidget(self.portLabel_6)
        spacerItem15 = QtWidgets.QSpacerItem(33, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_25.addItem(spacerItem15)
        self.portNumber_6 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.portNumber_6.setFont(font)
        self.portNumber_6.setObjectName("portNumber_6")
        self.horizontalLayout_25.addWidget(self.portNumber_6)
        self.verticalLayout_6.addLayout(self.horizontalLayout_25)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.tempNameLable_7 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tempNameLable_7.setFont(font)
        self.tempNameLable_7.setObjectName("tempNameLable_7")
        self.horizontalLayout_9.addWidget(self.tempNameLable_7)
        spacerItem16 = QtWidgets.QSpacerItem(35, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem16)
        self.tempLable_6 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tempLable_6.setFont(font)
        self.tempLable_6.setStyleSheet("")
        self.tempLable_6.setObjectName("tempLable_6")
        self.horizontalLayout_9.addWidget(self.tempLable_6)
        self.verticalLayout_6.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_26 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_26.setObjectName("horizontalLayout_26")
        self.statusNameLabel_6 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.statusNameLabel_6.setFont(font)
        self.statusNameLabel_6.setObjectName("statusNameLabel_6")
        self.horizontalLayout_26.addWidget(self.statusNameLabel_6)
        spacerItem17 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_26.addItem(spacerItem17)
        self.statusLabel_6 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.statusLabel_6.setFont(font)
        self.statusLabel_6.setStyleSheet("color: rgb(255, 0, 0);")
        self.statusLabel_6.setObjectName("statusLabel_6")
        self.horizontalLayout_26.addWidget(self.statusLabel_6)
        self.verticalLayout_6.addLayout(self.horizontalLayout_26)
        self.reportButton_6 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.reportButton_6.setFont(font)
        self.reportButton_6.setObjectName("reportButton_6")
        self.verticalLayout_6.addWidget(self.reportButton_6)
        self.gridLayout.addLayout(self.verticalLayout_6, 2, 1, 1, 1)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.owenName_7 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.owenName_7.setFont(font)
        self.owenName_7.setObjectName("owenName_7")
        self.verticalLayout_7.addWidget(self.owenName_7)
        self.horizontalLayout_27 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_27.setObjectName("horizontalLayout_27")
        self.portLabel_7 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.portLabel_7.setFont(font)
        self.portLabel_7.setObjectName("portLabel_7")
        self.horizontalLayout_27.addWidget(self.portLabel_7)
        spacerItem18 = QtWidgets.QSpacerItem(33, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_27.addItem(spacerItem18)
        self.portNumber_7 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.portNumber_7.setFont(font)
        self.portNumber_7.setObjectName("portNumber_7")
        self.horizontalLayout_27.addWidget(self.portNumber_7)
        self.verticalLayout_7.addLayout(self.horizontalLayout_27)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.tempNameLable_8 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tempNameLable_8.setFont(font)
        self.tempNameLable_8.setObjectName("tempNameLable_8")
        self.horizontalLayout_10.addWidget(self.tempNameLable_8)
        spacerItem19 = QtWidgets.QSpacerItem(35, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem19)
        self.tempLable_7 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tempLable_7.setFont(font)
        self.tempLable_7.setStyleSheet("")
        self.tempLable_7.setObjectName("tempLable_7")
        self.horizontalLayout_10.addWidget(self.tempLable_7)
        self.verticalLayout_7.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_28 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_28.setObjectName("horizontalLayout_28")
        self.statusNameLabel_7 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.statusNameLabel_7.setFont(font)
        self.statusNameLabel_7.setObjectName("statusNameLabel_7")
        self.horizontalLayout_28.addWidget(self.statusNameLabel_7)
        spacerItem20 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_28.addItem(spacerItem20)
        self.statusLabel_7 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.statusLabel_7.setFont(font)
        self.statusLabel_7.setStyleSheet("color: rgb(255, 0, 0);")
        self.statusLabel_7.setObjectName("statusLabel_7")
        self.horizontalLayout_28.addWidget(self.statusLabel_7)
        self.verticalLayout_7.addLayout(self.horizontalLayout_28)
        self.reportButton_7 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.reportButton_7.setFont(font)
        self.reportButton_7.setObjectName("reportButton_7")
        self.verticalLayout_7.addWidget(self.reportButton_7)
        self.gridLayout.addLayout(self.verticalLayout_7, 2, 2, 1, 1)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.owenName_8 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.owenName_8.setFont(font)
        self.owenName_8.setObjectName("owenName_8")
        self.verticalLayout_8.addWidget(self.owenName_8)
        self.horizontalLayout_29 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_29.setObjectName("horizontalLayout_29")
        self.portLabel_8 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.portLabel_8.setFont(font)
        self.portLabel_8.setObjectName("portLabel_8")
        self.horizontalLayout_29.addWidget(self.portLabel_8)
        spacerItem21 = QtWidgets.QSpacerItem(33, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_29.addItem(spacerItem21)
        self.portNumber_8 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.portNumber_8.setFont(font)
        self.portNumber_8.setObjectName("portNumber_8")
        self.horizontalLayout_29.addWidget(self.portNumber_8)
        self.verticalLayout_8.addLayout(self.horizontalLayout_29)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.tempNameLable_9 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tempNameLable_9.setFont(font)
        self.tempNameLable_9.setObjectName("tempNameLable_9")
        self.horizontalLayout_11.addWidget(self.tempNameLable_9)
        spacerItem22 = QtWidgets.QSpacerItem(35, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem22)
        self.tempLable_8 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tempLable_8.setFont(font)
        self.tempLable_8.setStyleSheet("")
        self.tempLable_8.setObjectName("tempLable_8")
        self.horizontalLayout_11.addWidget(self.tempLable_8)
        self.verticalLayout_8.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_30 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_30.setObjectName("horizontalLayout_30")
        self.statusNameLabel_8 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.statusNameLabel_8.setFont(font)
        self.statusNameLabel_8.setObjectName("statusNameLabel_8")
        self.horizontalLayout_30.addWidget(self.statusNameLabel_8)
        spacerItem23 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_30.addItem(spacerItem23)
        self.statusLabel_8 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.statusLabel_8.setFont(font)
        self.statusLabel_8.setStyleSheet("color: rgb(255, 0, 0);")
        self.statusLabel_8.setObjectName("statusLabel_8")
        self.horizontalLayout_30.addWidget(self.statusLabel_8)
        self.verticalLayout_8.addLayout(self.horizontalLayout_30)
        self.reportButton_8 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.reportButton_8.setFont(font)
        self.reportButton_8.setObjectName("reportButton_8")
        self.verticalLayout_8.addWidget(self.reportButton_8)
        self.gridLayout.addLayout(self.verticalLayout_8, 2, 3, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 606, 21))
        self.menubar.setObjectName("menubar")
        self.Parameters = QtWidgets.QMenu(self.menubar)
        self.Parameters.setObjectName("Parameters")
        self.Help = QtWidgets.QMenu(self.menubar)
        self.Help.setObjectName("Help")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.ports = QtWidgets.QAction(MainWindow)
        self.ports.setObjectName("ports")
        self.About = QtWidgets.QAction(MainWindow)
        self.About.setObjectName("About")
        self.folders = QtWidgets.QAction(MainWindow)
        self.folders.setObjectName("folders")
        self.events = QtWidgets.QAction(MainWindow)
        self.events.setObjectName("events")
        self.exit = QtWidgets.QAction(MainWindow)
        self.exit.setObjectName("exit")
        self.graph = QtWidgets.QAction(MainWindow)
        self.graph.setObjectName("graph")
        self.Parameters.addAction(self.ports)
        self.Parameters.addAction(self.events)
        self.Parameters.addAction(self.graph)
        self.Parameters.addSeparator()
        self.Parameters.addAction(self.exit)
        self.Help.addAction(self.About)
        self.menubar.addAction(self.Parameters.menuAction())
        self.menubar.addAction(self.Help.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Анализатор Варта ТП703"))
        self.owenName_1.setText(_translate("MainWindow", "Печь 1"))
        self.portLabel_1.setText(_translate("MainWindow", "Порт:"))
        self.portNumber_1.setText(_translate("MainWindow", "1"))
        self.tempNameLable_1.setText(_translate("MainWindow", "t °C"))
        self.tempLable_1.setText(_translate("MainWindow", "-1"))
        self.statusNameLabel_1.setText(_translate("MainWindow", "Состояние:"))
        self.statusLabel_1.setText(_translate("MainWindow", "Закрыт"))
        self.reportButton_1.setText(_translate("MainWindow", "Отчет"))
        self.owenName_2.setText(_translate("MainWindow", "Печь 2"))
        self.portLabel_2.setText(_translate("MainWindow", "Порт:"))
        self.portNumber_2.setText(_translate("MainWindow", "1"))
        self.tempNameLable_2.setText(_translate("MainWindow", "t °C"))
        self.tempLable_2.setText(_translate("MainWindow", "-1"))
        self.statusNameLabel_2.setText(_translate("MainWindow", "Состояние:"))
        self.statusLabel_2.setText(_translate("MainWindow", "Закрыт"))
        self.reportButton_2.setText(_translate("MainWindow", "Отчет"))
        self.owenName_3.setText(_translate("MainWindow", "Печь 3"))
        self.portLabel_3.setText(_translate("MainWindow", "Порт:"))
        self.portNumber_3.setText(_translate("MainWindow", "1"))
        self.tempNameLable_4.setText(_translate("MainWindow", "t °C"))
        self.tempLable_3.setText(_translate("MainWindow", "-1"))
        self.statusNameLabel_3.setText(_translate("MainWindow", "Состояние:"))
        self.statusLabel_3.setText(_translate("MainWindow", "Закрыт"))
        self.reportButton_3.setText(_translate("MainWindow", "Отчет"))
        self.owenName_4.setText(_translate("MainWindow", "Печь 4"))
        self.portLabel_4.setText(_translate("MainWindow", "Порт:"))
        self.portNumber_4.setText(_translate("MainWindow", "1"))
        self.tempNameLable_5.setText(_translate("MainWindow", "t °C"))
        self.tempLable_4.setText(_translate("MainWindow", "-1"))
        self.statusNameLabel_4.setText(_translate("MainWindow", "Состояние:"))
        self.statusLabel_4.setText(_translate("MainWindow", "Закрыт"))
        self.reportButton_4.setText(_translate("MainWindow", "Отчет"))
        self.owenName_5.setText(_translate("MainWindow", "Печь 5"))
        self.portLabel_5.setText(_translate("MainWindow", "Порт:"))
        self.portNumber_5.setText(_translate("MainWindow", "1"))
        self.tempNameLable_6.setText(_translate("MainWindow", "t °C"))
        self.tempLable_5.setText(_translate("MainWindow", "-1"))
        self.statusNameLabel_5.setText(_translate("MainWindow", "Состояние:"))
        self.statusLabel_5.setText(_translate("MainWindow", "Закрыт"))
        self.reportButton_5.setText(_translate("MainWindow", "Отчет"))
        self.owenName_6.setText(_translate("MainWindow", "Печь 6"))
        self.portLabel_6.setText(_translate("MainWindow", "Порт:"))
        self.portNumber_6.setText(_translate("MainWindow", "1"))
        self.tempNameLable_7.setText(_translate("MainWindow", "t °C"))
        self.tempLable_6.setText(_translate("MainWindow", "-1"))
        self.statusNameLabel_6.setText(_translate("MainWindow", "Состояние:"))
        self.statusLabel_6.setText(_translate("MainWindow", "Закрыт"))
        self.reportButton_6.setText(_translate("MainWindow", "Отчет"))
        self.owenName_7.setText(_translate("MainWindow", "Печь 7"))
        self.portLabel_7.setText(_translate("MainWindow", "Порт:"))
        self.portNumber_7.setText(_translate("MainWindow", "1"))
        self.tempNameLable_8.setText(_translate("MainWindow", "t °C"))
        self.tempLable_7.setText(_translate("MainWindow", "-1"))
        self.statusNameLabel_7.setText(_translate("MainWindow", "Состояние:"))
        self.statusLabel_7.setText(_translate("MainWindow", "Закрыт"))
        self.reportButton_7.setText(_translate("MainWindow", "Отчет"))
        self.owenName_8.setText(_translate("MainWindow", "Печь 8"))
        self.portLabel_8.setText(_translate("MainWindow", "Порт:"))
        self.portNumber_8.setText(_translate("MainWindow", "1"))
        self.tempNameLable_9.setText(_translate("MainWindow", "t °C"))
        self.tempLable_8.setText(_translate("MainWindow", "-1"))
        self.statusNameLabel_8.setText(_translate("MainWindow", "Состояние:"))
        self.statusLabel_8.setText(_translate("MainWindow", "Закрыт"))
        self.reportButton_8.setText(_translate("MainWindow", "Отчет"))
        self.Parameters.setTitle(_translate("MainWindow", "Меню"))
        self.Help.setTitle(_translate("MainWindow", "Помощь"))
        self.ports.setText(_translate("MainWindow", "Порты"))
        self.ports.setShortcut(_translate("MainWindow", "Ctrl+Shift+P"))
        self.About.setText(_translate("MainWindow", "О программе"))
        self.folders.setText(_translate("MainWindow", "Папки"))
        self.folders.setShortcut(_translate("MainWindow", "Ctrl+Shift+F"))
        self.events.setText(_translate("MainWindow", "Уведомления"))
        self.events.setShortcut(_translate("MainWindow", "Ctrl+U"))
        self.exit.setText(_translate("MainWindow", "Выход"))
        self.exit.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.graph.setText(_translate("MainWindow", "Опорный график"))
        self.graph.setShortcut(_translate("MainWindow", "Ctrl+G"))

