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
        Report.resize(769, 891)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("lines.ico"), QtGui.QIcon.Active, QtGui.QIcon.On)
        Report.setWindowIcon(icon)
        self.MplWidget = MplWidget(Report)
        self.MplWidget.setGeometry(QtCore.QRect(10, 130, 751, 520))
        self.MplWidget.setObjectName("MplWidget")

        self.retranslateUi(Report)
        QtCore.QMetaObject.connectSlotsByName(Report)

    def retranslateUi(self, Report):
        _translate = QtCore.QCoreApplication.translate
        Report.setWindowTitle(_translate("Report", "Отчет"))

from mplwidget import MplWidget
