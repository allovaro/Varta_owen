# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'port_parameters.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(236, 164)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("lines.png"), QtGui.QIcon.Active, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.gridLayout_3 = QtWidgets.QGridLayout(Form)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.gridLayout_2.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 1, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setObjectName("comboBox")
        self.gridLayout.addWidget(self.comboBox, 0, 0, 1, 1)
        self.comboBox_2 = QtWidgets.QComboBox(Form)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.gridLayout.addWidget(self.comboBox_2, 1, 0, 1, 1)
        self.comboBox_3 = QtWidgets.QComboBox(Form)
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.gridLayout.addWidget(self.comboBox_3, 2, 0, 1, 1)
        self.comboBox_4 = QtWidgets.QComboBox(Form)
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.gridLayout.addWidget(self.comboBox_4, 3, 0, 1, 1)
        self.comboBox_5 = QtWidgets.QComboBox(Form)
        self.comboBox_5.setObjectName("comboBox_5")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.gridLayout.addWidget(self.comboBox_5, 4, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 2, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Настройки портов"))
        self.label.setText(_translate("Form", "Порт:"))
        self.label_2.setText(_translate("Form", "Скорость:"))
        self.label_3.setText(_translate("Form", "Четность:"))
        self.label_4.setText(_translate("Form", "Кол-во бит:"))
        self.label_5.setText(_translate("Form", "Стоп бит:"))
        self.comboBox_2.setItemText(0, _translate("Form", "1200"))
        self.comboBox_2.setItemText(1, _translate("Form", "2400"))
        self.comboBox_2.setItemText(2, _translate("Form", "4800"))
        self.comboBox_2.setItemText(3, _translate("Form", "7200"))
        self.comboBox_2.setItemText(4, _translate("Form", "9600"))
        self.comboBox_2.setItemText(5, _translate("Form", "14400"))
        self.comboBox_2.setItemText(6, _translate("Form", "19200"))
        self.comboBox_2.setItemText(7, _translate("Form", "38400"))
        self.comboBox_2.setItemText(8, _translate("Form", "57600"))
        self.comboBox_2.setItemText(9, _translate("Form", "115200"))
        self.comboBox_3.setItemText(0, _translate("Form", "Нет"))
        self.comboBox_3.setItemText(1, _translate("Form", "Четный"))
        self.comboBox_3.setItemText(2, _translate("Form", "Не четный"))
        self.comboBox_4.setItemText(0, _translate("Form", "7"))
        self.comboBox_4.setItemText(1, _translate("Form", "8"))
        self.comboBox_5.setItemText(0, _translate("Form", "1"))
        self.comboBox_5.setItemText(1, _translate("Form", "2"))

