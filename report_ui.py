# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'report.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Report(object):
    def setupUi(self, Report):
        Report.setObjectName("Report")
        Report.resize(730, 770)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("lines.ico"), QtGui.QIcon.Active, QtGui.QIcon.On)
        Report.setWindowIcon(icon)
        self.widget = QtWidgets.QWidget(Report)
        self.widget.setGeometry(QtCore.QRect(10, 11, 712, 707))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(300, 17, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.filesDialog = QtWidgets.QPushButton(self.widget)
        self.filesDialog.setObjectName("filesDialog")
        self.horizontalLayout.addWidget(self.filesDialog)
        spacerItem1 = QtWidgets.QSpacerItem(300, 17, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.MplWidget = MplWidget(self.widget)
        self.MplWidget.setMinimumSize(QtCore.QSize(710, 639))
        self.MplWidget.setObjectName("MplWidget")
        self.verticalLayout.addWidget(self.MplWidget)

        self.retranslateUi(Report)
        QtCore.QMetaObject.connectSlotsByName(Report)

    def retranslateUi(self, Report):
        _translate = QtCore.QCoreApplication.translate
        Report.setWindowTitle(_translate("Report", "Отчет"))
        self.filesDialog.setText(_translate("Report", "Выбрать файлы"))
        self.label.setText(_translate("Report", "Выберите файлы для добавления их к отчету"))

from mplwidget import MplWidget
