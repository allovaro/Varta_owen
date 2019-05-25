# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'graph.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Graph_editor(object):
    def setupUi(self, Graph_editor):
        Graph_editor.setObjectName("Graph_editor")
        Graph_editor.resize(400, 300)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("lines.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        Graph_editor.setWindowIcon(icon)

        self.retranslateUi(Graph_editor)
        QtCore.QMetaObject.connectSlotsByName(Graph_editor)

    def retranslateUi(self, Graph_editor):
        _translate = QtCore.QCoreApplication.translate
        Graph_editor.setWindowTitle(_translate("Graph_editor", "Редактор опорных графиков"))

