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
        MainWindow.resize(899, 623)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("lines.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setAccessibleName("")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.MplWidget_1 = MplWidget(self.tab)
        self.MplWidget_1.setObjectName("MplWidget_1")
        self.gridLayout_2.addWidget(self.MplWidget_1, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.MplWidget_2 = MplWidget(self.tab_2)
        self.MplWidget_2.setObjectName("MplWidget_2")
        self.gridLayout_3.addWidget(self.MplWidget_2, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.MplWidget_3 = MplWidget(self.tab_3)
        self.MplWidget_3.setObjectName("MplWidget_3")
        self.gridLayout_4.addWidget(self.MplWidget_3, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.tab_4)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.MplWidget_4 = MplWidget(self.tab_4)
        self.MplWidget_4.setObjectName("MplWidget_4")
        self.horizontalLayout.addWidget(self.MplWidget_4)
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.tab_5)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.MplWidget_5 = MplWidget(self.tab_5)
        self.MplWidget_5.setObjectName("MplWidget_5")
        self.gridLayout_5.addWidget(self.MplWidget_5, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_5, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.tab_6)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.MplWidget_6 = MplWidget(self.tab_6)
        self.MplWidget_6.setObjectName("MplWidget_6")
        self.gridLayout_6.addWidget(self.MplWidget_6, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_6, "")
        self.tab_7 = QtWidgets.QWidget()
        self.tab_7.setObjectName("tab_7")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.tab_7)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.MplWidget_7 = MplWidget(self.tab_7)
        self.MplWidget_7.setObjectName("MplWidget_7")
        self.gridLayout_7.addWidget(self.MplWidget_7, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_7, "")
        self.tab_8 = QtWidgets.QWidget()
        self.tab_8.setObjectName("tab_8")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.tab_8)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.MplWidget_8 = MplWidget(self.tab_8)
        self.MplWidget_8.setObjectName("MplWidget_8")
        self.gridLayout_8.addWidget(self.MplWidget_8, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_8, "")
        self.tab_9 = QtWidgets.QWidget()
        self.tab_9.setObjectName("tab_9")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.tab_9)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.MplWidget_9 = MplWidget(self.tab_9)
        self.MplWidget_9.setObjectName("MplWidget_9")
        self.gridLayout_9.addWidget(self.MplWidget_9, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_9, "")
        self.tab_10 = QtWidgets.QWidget()
        self.tab_10.setObjectName("tab_10")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.tab_10)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.MplWidget_10 = MplWidget(self.tab_10)
        self.MplWidget_10.setObjectName("MplWidget_10")
        self.gridLayout_10.addWidget(self.MplWidget_10, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_10, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 899, 21))
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
        self.Parameters.addAction(self.folders)
        self.Parameters.addAction(self.events)
        self.Parameters.addAction(self.graph)
        self.Parameters.addSeparator()
        self.Parameters.addAction(self.exit)
        self.Help.addAction(self.About)
        self.menubar.addAction(self.Parameters.menuAction())
        self.menubar.addAction(self.Help.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Анализатор Варта ТП703"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Печь 1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Печь 2"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Печь 3"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Печь 4"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "Печь 5"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), _translate("MainWindow", "Печь 6"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_7), _translate("MainWindow", "Печь 7"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_8), _translate("MainWindow", "Печь 8"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_9), _translate("MainWindow", "Печь 9"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_10), _translate("MainWindow", "Печь 10"))
        self.Parameters.setTitle(_translate("MainWindow", "Меню"))
        self.Help.setTitle(_translate("MainWindow", "Помощь"))
        self.ports.setText(_translate("MainWindow", "Порты"))
        self.ports.setShortcut(_translate("MainWindow", "Ctrl+Shift+P"))
        self.About.setText(_translate("MainWindow", "О программе"))
        self.folders.setText(_translate("MainWindow", "Папки"))
        self.events.setText(_translate("MainWindow", "Уведомления"))
        self.events.setShortcut(_translate("MainWindow", "Ctrl+U"))
        self.exit.setText(_translate("MainWindow", "Выход"))
        self.exit.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.graph.setText(_translate("MainWindow", "Опорный график"))

from mplwidget import MplWidget
