from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import QtCore
from PyQt5.QtSerialPort import QSerialPort
from PyQt5.QtCore import QThread, QRegExp
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtWidgets import QSystemTrayIcon, QStyle, QAction, QMenu, qApp, QFileDialog
from mainwindow_ui import Ui_MainWindow  # импорт нашего сгенерированного файла
from port_parameters_ui import Ui_Form
from about_ui import Ui_About
from graph_ui import Ui_Graph_editor
from report_ui import Ui_Report
import sys, glob, os, csv
import time as tm
import datetime as dt
import serial
from serial.tools.list_ports_windows import comports
from SerialClass import SerialWorker
import matplotlib.dates as md
from matplotlib.backends.backend_qt5agg import (NavigationToolbar2QT as NavigationToolbar)
import numpy as np
import random


class mywindow(QtWidgets.QMainWindow):
    tray_icon = None
    etalon_temp = None
    prev_tab_index = 0
    time_line = []
    temp_line = []
    port_lines = []
    time_line_current_tab = []
    temp_line_current_tab = []
    # serial_1 = QSerialPort(self)
    # myThread = SerialReadThread()

    thread1 = QtCore.QThread()
    thread2 = QtCore.QThread()
    thread3 = QtCore.QThread()
    thread4 = QtCore.QThread()
    thread5 = QtCore.QThread()
    thread6 = QtCore.QThread()
    thread7 = QtCore.QThread()
    thread8 = QtCore.QThread()
    # thread9 = QtCore.QThread()
    # thread10 = QtCore.QThread()

    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Соединения кнопок меню
        self.ui.exit.triggered.connect(qApp.quit)
        self.ui.ports.triggered.connect(self.ports_open)
        self.ui.graph.triggered.connect(self.graph_open)
        self.ui.About.triggered.connect(self.about_open)
        self.ui.reportButton_1.clicked.connect(self.report_open)
        self.ui.reportButton_2.clicked.connect(self.report_open)
        self.ui.reportButton_3.clicked.connect(self.report_open)
        self.ui.reportButton_4.clicked.connect(self.report_open)
        self.ui.reportButton_5.clicked.connect(self.report_open)
        self.ui.reportButton_6.clicked.connect(self.report_open)
        self.ui.reportButton_7.clicked.connect(self.report_open)
        self.ui.reportButton_8.clicked.connect(self.report_open)

        # Инициализируем QSystemTrayIcon
        self.tray_icon = QSystemTrayIcon(self)
        self.tray_icon.setIcon(QtGui.QIcon('lines.png'))
        show_action = QAction("Показать", self)
        quit_action = QAction("Выход", self)
        hide_action = QAction("Спрятать", self)
        show_action.triggered.connect(self.show)
        hide_action.triggered.connect(self.hide)
        quit_action.triggered.connect(qApp.quit)
        tray_menu = QMenu()
        tray_menu.addAction(show_action)
        tray_menu.addAction(hide_action)
        tray_menu.addAction(quit_action)
        self.tray_icon.setContextMenu(tray_menu)
        self.tray_icon.show()

        # QThreads for serial port
        try:
            with open('port_configuration.cfg', 'r') as f:
                lines = f.readlines()
                f.close()
        except FileNotFoundError:
            print('File port_configuration.cfg not found')
        self.worker1 = SerialWorker(1, lines[0][:-1], lines[1][:-1])
        self.worker2 = SerialWorker(2, lines[5][:-1], lines[6][:-1])
        self.worker3 = SerialWorker(3, lines[10][:-1], lines[11][:-1])
        self.worker4 = SerialWorker(4, lines[15][:-1], lines[16][:-1])
        self.worker5 = SerialWorker(5, lines[20][:-1], lines[21][:-1])
        self.worker6 = SerialWorker(6, lines[25][:-1], lines[26][:-1])
        self.worker7 = SerialWorker(7, lines[30][:-1], lines[31][:-1])
        self.worker8 = SerialWorker(8, lines[35][:-1], lines[36][:-1])
        # self.worker9 = SerialWorker(9, lines[40][:-1], lines[41][:-1])
        # self.worker10 = SerialWorker(10, lines[45][:-1], lines[46][:-1])

        self.worker1.moveToThread(self.thread1)
        self.worker1.port_opened.connect(self.change_port_view)
        self.worker1.currTemp.connect(self.change_temp_in_mainwindow)
        self.ui.portNumber_1.setText(lines[0][:-1])
        self.thread1.started.connect(self.worker1.task)
        self.thread1.start()

        self.worker2.moveToThread(self.thread2)
        self.worker2.port_opened.connect(self.change_port_view)
        self.worker2.currTemp.connect(self.change_temp_in_mainwindow)
        self.ui.portNumber_2.setText(lines[5][:-1])
        self.thread2.started.connect(self.worker2.task)
        self.thread2.start()

        self.worker3.moveToThread(self.thread3)
        self.worker3.port_opened.connect(self.change_port_view)
        self.worker3.currTemp.connect(self.change_temp_in_mainwindow)
        self.ui.portNumber_3.setText(lines[10][:-1])
        self.thread3.started.connect(self.worker3.task)
        self.thread3.start()

        self.worker4.moveToThread(self.thread4)
        self.worker4.port_opened.connect(self.change_port_view)
        self.worker4.currTemp.connect(self.change_temp_in_mainwindow)
        self.ui.portNumber_4.setText(lines[15][:-1])
        self.thread4.started.connect(self.worker4.task)
        self.thread4.start()

        self.worker5.moveToThread(self.thread5)
        self.worker5.port_opened.connect(self.change_port_view)
        self.worker5.currTemp.connect(self.change_temp_in_mainwindow)
        self.ui.portNumber_5.setText(lines[20][:-1])
        self.thread5.started.connect(self.worker5.task)
        self.thread5.start()

        self.worker6.moveToThread(self.thread6)
        self.worker6.port_opened.connect(self.change_port_view)
        self.worker6.currTemp.connect(self.change_temp_in_mainwindow)
        self.ui.portNumber_6.setText(lines[25][:-1])
        self.thread6.started.connect(self.worker6.task)
        self.thread6.start()

        self.worker7.moveToThread(self.thread7)
        self.worker7.port_opened.connect(self.change_port_view)
        self.worker7.currTemp.connect(self.change_temp_in_mainwindow)
        self.ui.portNumber_7.setText(lines[30][:-1])
        self.thread7.started.connect(self.worker7.task)
        self.thread7.start()

        self.worker8.moveToThread(self.thread8)
        self.worker8.port_opened.connect(self.change_port_view)
        self.worker8.currTemp.connect(self.change_temp_in_mainwindow)
        self.ui.portNumber_8.setText(lines[35][:-1])
        self.thread8.started.connect(self.worker8.task)
        self.thread8.start()

        # self.worker9.moveToThread(self.thread9)
        # self.worker9.port_opened.connect(self.change_port_view)
        # self.thread9.start()
        #
        # self.worker10.moveToThread(self.thread10)
        # self.thread10.started.connect(self.worker10.task)
        # self.thread10.start()

    def change_port_view(self, text):
        if text == 'open':
            # Выставляем надпись и меняем цвет открыт порт или нет
            if self.sender().owen_num == '1':
                self.ui.statusLabel_1.setText('Открыт')
                self.ui.statusLabel_1.setStyleSheet('color: green')
            # Выставляем надпись и меняем цвет открыт порт или нет
            elif self.sender().owen_num == '2':
                self.ui.statusLabel_2.setText('Открыт')
                self.ui.statusLabel_2.setStyleSheet('color: green')
            # Выставляем надпись и меняем цвет открыт порт или нет
            elif self.sender().owen_num == '3':
                self.ui.statusLabel_3.setText('Открыт')
                self.ui.statusLabel_3.setStyleSheet('color: green')
            # Выставляем надпись и меняем цвет открыт порт или нет
            elif self.sender().owen_num == '4':
                self.ui.statusLabel_4.setText('Открыт')
                self.ui.statusLabel_4.setStyleSheet('color: green')
            # Выставляем надпись и меняем цвет открыт порт или нет
            elif self.sender().owen_num == '5':
                self.ui.statusLabel_5.setText('Открыт')
                self.ui.statusLabel_5.setStyleSheet('color: green')
            # Выставляем надпись и меняем цвет открыт порт или нет
            elif self.sender().owen_num == '6':
                self.ui.statusLabel_6.setText('Открыт')
                self.ui.statusLabel_6.setStyleSheet('color: green')
            # Выставляем надпись и меняем цвет открыт порт или нет
            elif self.sender().owen_num == '7':
                self.ui.statusLabel_7.setText('Открыт')
                self.ui.statusLabel_7.setStyleSheet('color: green')
            # Выставляем надпись и меняем цвет открыт порт или нет
            elif self.sender().owen_num == '8':
                self.ui.statusLabel_8.setText('Открыт')
                self.ui.statusLabel_8.setStyleSheet('color: green')
        if text == 'close':
            if self.sender().owen_num == '1':
                self.ui.statusLabel_1.setText('Закрыт')
                self.ui.statusLabel_1.setStyleSheet('color: red')

            if self.sender().owen_num == '2':
                self.ui.statusLabel_2.setText('Закрыт')
                self.ui.statusLabel_2.setStyleSheet('color: red')
            if self.sender().owen_num == '3':
                self.ui.statusLabel_3.setText('Закрыт')
                self.ui.statusLabel_3.setStyleSheet('color: red')
            if self.sender().owen_num == '4':
                self.ui.statusLabel_4.setText('Закрыт')
                self.ui.statusLabel_4.setStyleSheet('color: red')
            if self.sender().owen_num == '5':
                self.ui.statusLabel_5.setText('Закрыт')
                self.ui.statusLabel_5.setStyleSheet('color: red')
            if self.sender().owen_num == '6':
                self.ui.statusLabel_6.setText('Закрыт')
                self.ui.statusLabel_6.setStyleSheet('color: red')
            if self.sender().owen_num == '7':
                self.ui.statusLabel_7.setText('Закрыт')
                self.ui.statusLabel_7.setStyleSheet('color: red')
            if self.sender().owen_num == '8':
                self.ui.statusLabel_8.setText('Закрыт')
                self.ui.statusLabel_8.setStyleSheet('color: red')

    def change_temp_in_mainwindow(self, text):
        if self.sender().owen_num == '1':
            self.ui.tempLable_1.setText(text)
        if self.sender().owen_num == '2':
            self.ui.tempLable_2.setText(text)
        if self.sender().owen_num == '3':
            self.ui.tempLable_3.setText(text)
        if self.sender().owen_num == '4':
            self.ui.tempLable_4.setText(text)
        if self.sender().owen_num == '5':
            self.ui.tempLable_5.setText(text)
        if self.sender().owen_num == '6':
            self.ui.tempLable_6.setText(text)
        if self.sender().owen_num == '7':
            self.ui.tempLable_7.setText(text)
        if self.sender().owen_num == '8':
            self.ui.tempLable_8.setText(text)

    def closeEvent(self, event):
        event.ignore()
        self.hide()
        print('Close event')
        self.tray_icon.showMessage(
            "Анализатор Варта ТП703",
            "Приложение было свернуто в трей",
            QSystemTrayIcon.Information,
            2000
        )

    def graph_open(self):
        self.window_graph = QtWidgets.QMainWindow()
        self.ui_graph = Ui_Graph_editor()
        self.ui_graph.setupUi(self.window_graph)
        self.ui_graph.MplWidgetGraphEditor.canvas.axes.set_title('Эталон')
        self.ui_graph.comboBoxOwen.activated[str].connect(self.change_etalon_graph)
        self.ui_graph.lineEditTemp1.editingFinished.connect(self.update_etalon_graph)
        self.ui_graph.lineEditTemp2.editingFinished.connect(self.update_etalon_graph)
        self.ui_graph.lineEditTemp3.editingFinished.connect(self.update_etalon_graph)
        self.ui_graph.lineEditTemp4.editingFinished.connect(self.update_etalon_graph)
        self.ui_graph.lineEditTemp5.editingFinished.connect(self.update_etalon_graph)
        self.ui_graph.lineEditTemp6.editingFinished.connect(self.update_etalon_graph)
        self.ui_graph.lineEditTemp7.editingFinished.connect(self.update_etalon_graph)
        self.ui_graph.lineEditTemp8.editingFinished.connect(self.update_etalon_graph)
        self.ui_graph.lineEditTemp9.editingFinished.connect(self.update_etalon_graph)
        self.ui_graph.lineEditTemp10.editingFinished.connect(self.update_etalon_graph)
        self.ui_graph.lineEditTemp11.editingFinished.connect(self.update_etalon_graph)
        self.ui_graph.lineEditTemp12.editingFinished.connect(self.update_etalon_graph)
        self.ui_graph.lineEditTemp13.editingFinished.connect(self.update_etalon_graph)
        self.ui_graph.lineEditTemp14.editingFinished.connect(self.update_etalon_graph)
        self.ui_graph.lineEditTemp15.editingFinished.connect(self.update_etalon_graph)
        self.ui_graph.lineEditTemp16.editingFinished.connect(self.update_etalon_graph)
        self.ui_graph.lineEditTemp17.editingFinished.connect(self.update_etalon_graph)
        self.ui_graph.lineEditTemp18.editingFinished.connect(self.update_etalon_graph)
        self.ui_graph.lineEditTemp19.editingFinished.connect(self.update_etalon_graph)
        self.ui_graph.lineEditTemp20.editingFinished.connect(self.update_etalon_graph)
        self.ui_graph.lineEditTemp21.editingFinished.connect(self.update_etalon_graph)
        self.ui_graph.lineEditTemp22.editingFinished.connect(self.update_etalon_graph)
        self.ui_graph.lineEditTemp23.editingFinished.connect(self.update_etalon_graph)
        self.ui_graph.lineEditTemp24.editingFinished.connect(self.update_etalon_graph)
        self.ui_graph.lineEditTime1.editingFinished.connect(self.update_etalon_graph)
        self.ui_graph.lineEditTime2.editingFinished.connect(self.update_etalon_graph)
        self.ui_graph.lineEditTime3.editingFinished.connect(self.update_etalon_graph)
        self.ui_graph.lineEditTime4.editingFinished.connect(self.update_etalon_graph)
        self.ui_graph.lineEditTime5.editingFinished.connect(self.update_etalon_graph)
        self.ui_graph.lineEditTime6.editingFinished.connect(self.update_etalon_graph)
        self.ui_graph.lineEditTime7.editingFinished.connect(self.update_etalon_graph)
        self.ui_graph.lineEditTime8.editingFinished.connect(self.update_etalon_graph)
        self.ui_graph.lineEditTime9.editingFinished.connect(self.update_etalon_graph)
        self.ui_graph.lineEditTime10.editingFinished.connect(self.update_etalon_graph)
        self.ui_graph.lineEditTime11.editingFinished.connect(self.update_etalon_graph)
        self.ui_graph.lineEditTime12.editingFinished.connect(self.update_etalon_graph)
        self.ui_graph.lineEditTime13.editingFinished.connect(self.update_etalon_graph)
        self.ui_graph.lineEditTime14.editingFinished.connect(self.update_etalon_graph)
        self.ui_graph.lineEditTime15.editingFinished.connect(self.update_etalon_graph)
        self.ui_graph.lineEditTime16.editingFinished.connect(self.update_etalon_graph)
        self.ui_graph.lineEditTime17.editingFinished.connect(self.update_etalon_graph)
        self.ui_graph.lineEditTime18.editingFinished.connect(self.update_etalon_graph)
        self.ui_graph.lineEditTime19.editingFinished.connect(self.update_etalon_graph)
        self.ui_graph.lineEditTime20.editingFinished.connect(self.update_etalon_graph)
        self.ui_graph.lineEditTime21.editingFinished.connect(self.update_etalon_graph)
        self.ui_graph.lineEditTime22.editingFinished.connect(self.update_etalon_graph)
        self.ui_graph.lineEditTime23.editingFinished.connect(self.update_etalon_graph)
        self.ui_graph.lineEditTime24.editingFinished.connect(self.update_etalon_graph)

        timeRange = "(?:[0-1]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])"  # Part of the regular expression
        # Regulare expression
        timeRegex = QRegExp("^" + timeRange + "\\." + timeRange + "$")
        tempRegex = QRegExp("^\d{1,4}$")
        timeValidator = QRegExpValidator(timeRegex, self)
        tempValidator = QRegExpValidator(tempRegex, self)
        self.ui_graph.lineEditTime1.setValidator(timeValidator)
        self.ui_graph.lineEditTemp1.setValidator(tempValidator)
        self.ui_graph.lineEditTime2.setValidator(timeValidator)
        self.ui_graph.lineEditTemp2.setValidator(tempValidator)
        self.ui_graph.lineEditTime3.setValidator(timeValidator)
        self.ui_graph.lineEditTemp3.setValidator(tempValidator)
        self.ui_graph.lineEditTime4.setValidator(timeValidator)
        self.ui_graph.lineEditTemp4.setValidator(tempValidator)
        self.ui_graph.lineEditTime5.setValidator(timeValidator)
        self.ui_graph.lineEditTemp5.setValidator(tempValidator)
        self.ui_graph.lineEditTime6.setValidator(timeValidator)
        self.ui_graph.lineEditTemp6.setValidator(tempValidator)
        self.ui_graph.lineEditTime7.setValidator(timeValidator)
        self.ui_graph.lineEditTemp7.setValidator(tempValidator)
        self.ui_graph.lineEditTime8.setValidator(timeValidator)
        self.ui_graph.lineEditTemp8.setValidator(tempValidator)
        self.ui_graph.lineEditTime9.setValidator(timeValidator)
        self.ui_graph.lineEditTemp9.setValidator(tempValidator)
        self.ui_graph.lineEditTime10.setValidator(timeValidator)
        self.ui_graph.lineEditTemp10.setValidator(tempValidator)
        self.ui_graph.lineEditTime11.setValidator(timeValidator)
        self.ui_graph.lineEditTemp11.setValidator(tempValidator)
        self.ui_graph.lineEditTime12.setValidator(timeValidator)
        self.ui_graph.lineEditTemp12.setValidator(tempValidator)
        self.ui_graph.lineEditTime13.setValidator(timeValidator)
        self.ui_graph.lineEditTemp13.setValidator(tempValidator)
        self.ui_graph.lineEditTime14.setValidator(timeValidator)
        self.ui_graph.lineEditTemp14.setValidator(tempValidator)
        self.ui_graph.lineEditTime15.setValidator(timeValidator)
        self.ui_graph.lineEditTemp15.setValidator(tempValidator)
        self.ui_graph.lineEditTime16.setValidator(timeValidator)
        self.ui_graph.lineEditTemp16.setValidator(tempValidator)
        self.ui_graph.lineEditTime17.setValidator(timeValidator)
        self.ui_graph.lineEditTemp17.setValidator(tempValidator)
        self.ui_graph.lineEditTime18.setValidator(timeValidator)
        self.ui_graph.lineEditTemp18.setValidator(tempValidator)
        self.ui_graph.lineEditTime19.setValidator(timeValidator)
        self.ui_graph.lineEditTemp19.setValidator(tempValidator)
        self.ui_graph.lineEditTime20.setValidator(timeValidator)
        self.ui_graph.lineEditTemp20.setValidator(tempValidator)
        self.ui_graph.lineEditTime21.setValidator(timeValidator)
        self.ui_graph.lineEditTemp21.setValidator(tempValidator)
        self.ui_graph.lineEditTime22.setValidator(timeValidator)
        self.ui_graph.lineEditTemp22.setValidator(tempValidator)
        self.ui_graph.lineEditTime23.setValidator(timeValidator)
        self.ui_graph.lineEditTemp23.setValidator(tempValidator)
        self.ui_graph.lineEditTime24.setValidator(timeValidator)
        self.ui_graph.lineEditTemp24.setValidator(tempValidator)
        try:
            with open('graph.cfg', 'r') as fr:
                lines = fr.readlines()
                self.temp_line = lines[0].split()
                self.temp_line = list(map(float, self.temp_line))
                # line = fr.readline()
                self.time_line = lines[1].split()
                self.time_line = list(map(float, self.time_line))
                fr.close()
        except FileNotFoundError:
            print('File graph.cfg not found')
            with open('graph.cfg', 'w') as fr:
                for i in range(20):
                    fr.write('\n')
                fr.close()
        self.update_lines_graph()
        self.update_etalon_draw()
        self.window_graph.show()

    def ports_open(self):
        self.window_ports = QtWidgets.QMainWindow()
        self.ui_ports = Ui_Form()
        self.ui_ports.setupUi(self.window_ports)
        for dev in comports():
            self.ui_ports.port_Name_comboBox.addItem(str(dev).split()[0])
        self.ui_ports.owenName_comboBox.currentIndexChanged.connect(self.update_port_settings)
        self.ui_ports.port_Name_comboBox.currentIndexChanged.connect(self.update_port_Name_settings)
        self.ui_ports.speed_comboBox.currentIndexChanged.connect(self.update_speed_settings)
        self.ui_ports.parity_comboBox.currentIndexChanged.connect(self.update_parity_settings)
        self.ui_ports.bits_comboBox.currentIndexChanged.connect(self.update_bits_settings)
        self.ui_ports.stop_bits_comboBox.currentIndexChanged.connect(self.update_stop_bits_settings)
        self.window_ports.show()
        try:
            with open('port_configuration.cfg', 'r') as fr:
                self.port_lines = fr.readlines()
                fr.close()
                self.update_port_settings(0)
        except FileNotFoundError:
            print('File port_configuration.cfg not found')
            with open('port_configuration.cfg', 'w') as fr:
                for i in range(50):
                    fr.write('\n')
                fr.close()

    def about_open(self):
        self.window_about = QtWidgets.QMainWindow()
        self.ui_about = Ui_About()
        self.ui_about.setupUi(self.window_about)
        self.window_about.show()

    def report_open(self):
        self.window_report = QtWidgets.QMainWindow()
        self.ui_report = Ui_Report()
        self.ui_report.setupUi(self.window_report)
        owen_num = self.detect_report_owen(self.sender())
        self.ui_report.filesDialog.clicked.connect(lambda: self.show_file_dialog(owen_num))
        self.change_etalon_graph1(owen_num, dt.datetime.today())
        title = 'Генератор отчета Печи №{}'.format(owen_num)
        self.window_report.setWindowTitle(title)
        self.window_report.addToolBar(QtCore.Qt.BottomToolBarArea,
                                      NavigationToolbar(self.ui_report.MplWidget.canvas, self))

        # self.ui_report.MplWidget.canvas.axes.clear()
        # # self.ui_report.MplWidget.canvas.axes.plot(self.time_line, self.temp_line, lw=2)
        # time1 = [dt.datetime(2019, 10, 30, 16, 8, 1), dt.datetime(2019, 10, 30, 16, 15, 1), dt.datetime(2019, 10, 30, 16, 35, 1)]
        # # time2 = [dt.datetime(2019, 10, 30, 16, 1), dt.datetime(2019, 10, 30, 16, 5), dt.datetime(2019, 10, 30, 16, 59)]
        # value = [1, 45, 39]
        # # value2 = [10, 46, 100]
        # self.ui_report.MplWidget.canvas.axes.plot_date(time1, value, '-')
        # # self.ui_report.MplWidget.canvas.axes.plot_date(time2, value2, '-')
        # self.ui_report.MplWidget.canvas.axes.set_ylabel('Градусы, °С')
        # self.ui_report.MplWidget.canvas.axes.set_xlabel('Время, ч')
        # self.ui_report.MplWidget.canvas.axes.legend(u'Программа', loc='lower center')
        # self.ui_report.MplWidget.canvas.draw()
        self.time_line = self.change_etalon_graph1(owen_num, dt.datetime.today())
        time1 = [dt.datetime(2019, 10, 30, 7, 4, 1), dt.datetime(2019, 10, 30, 16, 15, 1),
                 dt.datetime(2019, 10, 30, 17, 35, 1), dt.datetime(2019, 10, 30, 17, 48, 1),
                 dt.datetime(2019, 10, 30, 18, 0, 1)]
        value1 = [12, 154, 256, 345, 777]
        self.ui_report.MplWidget.canvas.axes.clear()
        self.ui_report.MplWidget.canvas.axes.plot_date(time1, value1, '-')
        self.ui_report.MplWidget.canvas.axes.set_ylabel('Градусы, °С')
        self.ui_report.MplWidget.canvas.axes.set_xlabel('Время, ч')
        self.ui_report.MplWidget.canvas.axes.xaxis.set_major_formatter(md.DateFormatter('%H:%M:%S'))
        # self.ui_report.MplWidget.canvas.axes.autofmt_xdate()
        # self.ui_report.MplWidget.canvas.get_xaxis().set_major_locator(mdates.MonthLocator(interval=4))
        self.ui_report.MplWidget.canvas.axes.legend('Программа', loc='lower center')
        self.ui_report.MplWidget.canvas.draw()
        self.window_report.show()

    def detect_report_owen(self, obj):
        if obj.objectName() == 'reportButton_1':
            return 1
        if obj.objectName() == 'reportButton_2':
            return 2
        if obj.objectName() == 'reportButton_3':
            return 3
        if obj.objectName() == 'reportButton_4':
            return 4
        if obj.objectName() == 'reportButton_5':
            return 5
        if obj.objectName() == 'reportButton_6':
            return 6
        if obj.objectName() == 'reportButton_7':
            return 7
        if obj.objectName() == 'reportButton_8':
            return 8

    def show_file_dialog(self, num):
        dialogSelectFiles = QFileDialog()
        dialogSelectFiles.setFileMode(QFileDialog.ExistingFiles)      # включение множественного выбора
        dialogSelectFiles.exec_()
        data = dialogSelectFiles.selectedFiles()
        if data:
            x, y = self.get_last_graph_points2(data)
            # print(x)
            self.change_etalon_graph1(num, dt.datetime.today())
            self.update_report_graph(x, y)


    def update_port_settings(self, index):
        try:
            with open('port_configuration.cfg', 'r') as fr:
                self.port_lines = fr.readlines()
                port_ind = self.ui_ports.port_Name_comboBox.findText(self.port_lines[index * 5][:-1],
                                                                     QtCore.Qt.MatchFixedString)
                if port_ind >= 0:
                    self.ui_ports.port_Name_comboBox.setCurrentIndex(port_ind)

                speed_ind = self.ui_ports.speed_comboBox.findText(self.port_lines[index * 5 + 1][:-1],
                                                                  QtCore.Qt.MatchFixedString)
                if speed_ind >= 0:
                    self.ui_ports.speed_comboBox.setCurrentIndex(speed_ind)
                # --------------------------------------------------
                parity_ind = self.ui_ports.parity_comboBox.findText(self.port_lines[index * 5 + 2][:-1],
                                                                  QtCore.Qt.MatchFixedString)
                if parity_ind >= 0:
                    self.ui_ports.parity_comboBox.setCurrentIndex(parity_ind)
                # --------------------------------------------------
                bits_ind = self.ui_ports.bits_comboBox.findText(self.port_lines[index * 5 + 3][:-1],
                                                                    QtCore.Qt.MatchFixedString)
                if bits_ind >= 0:
                    self.ui_ports.bits_comboBox.setCurrentIndex(bits_ind)
                # --------------------------------------------------
                stop_bits_ind = self.ui_ports.stop_bits_comboBox.findText(self.port_lines[index * 5 + 4][:-1],
                                                                  QtCore.Qt.MatchFixedString)
                if stop_bits_ind >= 0:
                    self.ui_ports.stop_bits_comboBox.setCurrentIndex(stop_bits_ind)
                fr.close()
        except FileNotFoundError:
            print('File port_configuration.cfg not found')

    def update_port_Name_settings(self, index):
        owen_index = self.ui_ports.owenName_comboBox.currentIndex()
        try:
            with open('port_configuration.cfg', 'r') as f:
                self.port_lines = f.readlines()
                f.close()
        except FileNotFoundError:
            print('File port_configuration.cfg not found')
        try:
            with open('port_configuration.cfg', 'w') as f:
                self.port_lines[owen_index * 5] = self.ui_ports.port_Name_comboBox.currentText() + '\n'
                f.writelines(self.port_lines)
                f.close()
        except FileNotFoundError:
            print('File port_configuration.cfg not found')

    def update_speed_settings(self, index):
        owen_index = self.ui_ports.owenName_comboBox.currentIndex()
        try:
            with open('port_configuration.cfg', 'r') as f:
                self.port_lines = f.readlines()
                f.close()
        except FileNotFoundError:
            print('File port_configuration.cfg not found')
        try:
            with open('port_configuration.cfg', 'w') as f:
                self.port_lines[owen_index * 5 + 1] = str(self.ui_ports.speed_comboBox.currentText()) + '\n'
                f.writelines(self.port_lines)
                f.close()
        except FileNotFoundError:
            print('File port_configuration.cfg not found')

    def update_parity_settings(self, index):
        owen_index = self.ui_ports.owenName_comboBox.currentIndex()
        try:
            with open('port_configuration.cfg', 'r') as f:
                self.port_lines = f.readlines()
                f.close()
        except FileNotFoundError:
            print('File port_configuration.cfg not found')
        try:
            with open('port_configuration.cfg', 'w') as f:
                self.port_lines[owen_index * 5 + 2] = str(self.ui_ports.parity_comboBox.currentText()) + '\n'
                f.writelines(self.port_lines)
                f.close()
        except FileNotFoundError:
            print('File port_configuration.cfg not found')

    def update_bits_settings(self, index):
        owen_index = self.ui_ports.owenName_comboBox.currentIndex()
        try:
            with open('port_configuration.cfg', 'r') as f:
                self.port_lines = f.readlines()
                f.close()
        except FileNotFoundError:
            print('File port_configuration.cfg not found')
        try:
            with open('port_configuration.cfg', 'w') as f:
                self.port_lines[owen_index * 5 + 3] = str(self.ui_ports.bits_comboBox.currentText()) + '\n'
                f.writelines(self.port_lines)
                f.close()
        except FileNotFoundError:
            print('File port_configuration.cfg not found')

    def update_stop_bits_settings(self, index):
        owen_index = self.ui_ports.owenName_comboBox.currentIndex()
        try:
            with open('port_configuration.cfg', 'r') as f:
                self.port_lines = f.readlines()
                f.close()
        except FileNotFoundError:
            print('File port_configuration.cfg not found')
        try:
            with open('port_configuration.cfg', 'w') as f:
                self.port_lines[owen_index * 5 + 4] = str(self.ui_ports.stop_bits_comboBox.currentText()) + '\n'
                f.writelines(self.port_lines)
                f.close()
        except FileNotFoundError:
            print('File port_configuration.cfg not found')

    def update_etalon_graph(self):
        self.time_line = []
        self.temp_line = []

        if self.ui_graph.lineEditTime1.text():
            if self.ui_graph.lineEditTime1.text():
                self.temp_line.append(float(self.ui_graph.lineEditTemp1.text()))
                self.time_line.append(float(self.ui_graph.lineEditTime1.text()))
        if self.ui_graph.lineEditTime2.text():
            if self.ui_graph.lineEditTemp2.text():
                self.temp_line.append(float(self.ui_graph.lineEditTemp2.text()))
                self.time_line.append(float(self.ui_graph.lineEditTime2.text()))
        if self.ui_graph.lineEditTime3.text():
            if self.ui_graph.lineEditTemp3.text():
                self.temp_line.append(float(self.ui_graph.lineEditTemp3.text()))
                self.time_line.append(float(self.ui_graph.lineEditTime3.text()))
        if self.ui_graph.lineEditTime4.text():
            if self.ui_graph.lineEditTemp4.text():
                self.temp_line.append(float(self.ui_graph.lineEditTemp4.text()))
                self.time_line.append(float(self.ui_graph.lineEditTime4.text()))
        if self.ui_graph.lineEditTime5.text():
            if self.ui_graph.lineEditTemp5.text():
                self.temp_line.append(float(self.ui_graph.lineEditTemp5.text()))
                self.time_line.append(float(self.ui_graph.lineEditTime5.text()))
        if self.ui_graph.lineEditTime6.text():
            if self.ui_graph.lineEditTemp6.text():
                self.temp_line.append(float(self.ui_graph.lineEditTemp6.text()))
                self.time_line.append(float(self.ui_graph.lineEditTime6.text()))
        if self.ui_graph.lineEditTime7.text():
            if self.ui_graph.lineEditTemp7.text():
                self.temp_line.append(float(self.ui_graph.lineEditTemp7.text()))
                self.time_line.append(float(self.ui_graph.lineEditTime7.text()))
        if self.ui_graph.lineEditTime8.text():
            if self.ui_graph.lineEditTemp8.text():
                self.temp_line.append(float(self.ui_graph.lineEditTemp8.text()))
                self.time_line.append(float(self.ui_graph.lineEditTime8.text()))
        if self.ui_graph.lineEditTime9.text():
            if self.ui_graph.lineEditTemp9.text():
                self.temp_line.append(float(self.ui_graph.lineEditTemp9.text()))
                self.time_line.append(float(self.ui_graph.lineEditTime9.text()))
        if self.ui_graph.lineEditTime10.text():
            if self.ui_graph.lineEditTemp10.text():
                self.temp_line.append(float(self.ui_graph.lineEditTemp10.text()))
                self.time_line.append(float(self.ui_graph.lineEditTime10.text()))
        if self.ui_graph.lineEditTime11.text():
            if self.ui_graph.lineEditTemp11.text():
                self.temp_line.append(float(self.ui_graph.lineEditTemp11.text()))
                self.time_line.append(float(self.ui_graph.lineEditTime11.text()))
        if self.ui_graph.lineEditTime12.text():
            if self.ui_graph.lineEditTemp12.text():
                self.temp_line.append(float(self.ui_graph.lineEditTemp12.text()))
                self.time_line.append(float(self.ui_graph.lineEditTime12.text()))
        if self.ui_graph.lineEditTime13.text():
            if self.ui_graph.lineEditTemp13.text():
                self.temp_line.append(float(self.ui_graph.lineEditTemp13.text()))
                self.time_line.append(float(self.ui_graph.lineEditTime13.text()))
        if self.ui_graph.lineEditTime14.text():
            if self.ui_graph.lineEditTemp14.text():
                self.temp_line.append(float(self.ui_graph.lineEditTemp14.text()))
                self.time_line.append(float(self.ui_graph.lineEditTime14.text()))
        if self.ui_graph.lineEditTime15.text():
            if self.ui_graph.lineEditTemp15.text():
                self.temp_line.append(float(self.ui_graph.lineEditTemp15.text()))
                self.time_line.append(float(self.ui_graph.lineEditTime15.text()))
        if self.ui_graph.lineEditTime16.text():
            if self.ui_graph.lineEditTemp16.text():
                self.temp_line.append(float(self.ui_graph.lineEditTemp16.text()))
                self.time_line.append(float(self.ui_graph.lineEditTime16.text()))
        if self.ui_graph.lineEditTime17.text():
            if self.ui_graph.lineEditTemp17.text():
                self.temp_line.append(float(self.ui_graph.lineEditTemp17.text()))
                self.time_line.append(float(self.ui_graph.lineEditTime17.text()))
        if self.ui_graph.lineEditTime18.text():
            if self.ui_graph.lineEditTemp18.text():
                self.temp_line.append(float(self.ui_graph.lineEditTemp18.text()))
                self.time_line.append(float(self.ui_graph.lineEditTime18.text()))
        if self.ui_graph.lineEditTime19.text():
            if self.ui_graph.lineEditTemp19.text():
                self.temp_line.append(float(self.ui_graph.lineEditTemp19.text()))
                self.time_line.append(float(self.ui_graph.lineEditTime19.text()))
        if self.ui_graph.lineEditTime20.text():
            if self.ui_graph.lineEditTemp20.text():
                self.temp_line.append(float(self.ui_graph.lineEditTemp20.text()))
                self.time_line.append(float(self.ui_graph.lineEditTime20.text()))
        if self.ui_graph.lineEditTime21.text():
            if self.ui_graph.lineEditTemp21.text():
                self.temp_line.append(float(self.ui_graph.lineEditTemp21.text()))
                self.time_line.append(float(self.ui_graph.lineEditTime21.text()))
        if self.ui_graph.lineEditTime22.text():
            if self.ui_graph.lineEditTemp22.text():
                self.temp_line.append(float(self.ui_graph.lineEditTemp22.text()))
                self.time_line.append(float(self.ui_graph.lineEditTime22.text()))
        if self.ui_graph.lineEditTime23.text():
            if self.ui_graph.lineEditTemp23.text():
                self.temp_line.append(float(self.ui_graph.lineEditTemp23.text()))
                self.time_line.append(float(self.ui_graph.lineEditTime23.text()))
        if self.ui_graph.lineEditTime24.text():
            if self.ui_graph.lineEditTemp24.text():
                self.temp_line.append(float(self.ui_graph.lineEditTemp24.text()))
                self.time_line.append(float(self.ui_graph.lineEditTime24.text()))
        try:
            with open('graph.cfg', 'r') as file:
                lines = file.readlines()
                lines_len = len(lines)
        except FileNotFoundError:
            print('File graph.cfg not found')

        with open('graph.cfg', 'w') as graph_file:
            if self.ui_graph.comboBoxOwen.currentText() == 'Печь 1':
                lines[0] = " ".join(map(str, self.temp_line)) + '\n'
                lines[1] = " ".join(map(str, self.time_line)) + '\n'
            if self.ui_graph.comboBoxOwen.currentText() == 'Печь 2':
                lines[2] = " ".join(map(str, self.temp_line)) + '\n'
                lines[3] = " ".join(map(str, self.time_line)) + '\n'
            if self.ui_graph.comboBoxOwen.currentText() == 'Печь 3':
                lines[4] = " ".join(map(str, self.temp_line)) + '\n'
                lines[5] = " ".join(map(str, self.time_line)) + '\n'
            if self.ui_graph.comboBoxOwen.currentText() == 'Печь 4':
                lines[6] = " ".join(map(str, self.temp_line)) + '\n'
                lines[7] = " ".join(map(str, self.time_line)) + '\n'
            if self.ui_graph.comboBoxOwen.currentText() == 'Печь 5':
                lines[8] = " ".join(map(str, self.temp_line)) + '\n'
                lines[9] = " ".join(map(str, self.time_line)) + '\n'
            if self.ui_graph.comboBoxOwen.currentText() == 'Печь 6':
                lines[10] = " ".join(map(str, self.temp_line)) + '\n'
                lines[11] = " ".join(map(str, self.time_line)) + '\n'
            if self.ui_graph.comboBoxOwen.currentText() == 'Печь 7':
                lines[12] = " ".join(map(str, self.temp_line)) + '\n'
                lines[13] = " ".join(map(str, self.time_line)) + '\n'
            if self.ui_graph.comboBoxOwen.currentText() == 'Печь 8':
                lines[14] = " ".join(map(str, self.temp_line)) + '\n'
                lines[15] = " ".join(map(str, self.time_line)) + '\n'
            if self.ui_graph.comboBoxOwen.currentText() == 'Печь 9':
                lines[16] = " ".join(map(str, self.temp_line)) + '\n'
                lines[17] = " ".join(map(str, self.time_line)) + '\n'
            if self.ui_graph.comboBoxOwen.currentText() == 'Печь 10':
                lines[18] = " ".join(map(str, self.temp_line)) + '\n'
                lines[19] = " ".join(map(str, self.time_line)) + '\n'
            graph_file.writelines(lines)
            graph_file.close()
        self.update_etalon_draw()

    def update_etalon_draw(self):
        self.ui_graph.MplWidgetGraphEditor.canvas.axes.clear()
        self.ui_graph.MplWidgetGraphEditor.canvas.axes.plot(self.time_line, self.temp_line, lw=2)
        self.ui_graph.MplWidgetGraphEditor.canvas.axes.set_ylabel('Градусы, °С')
        self.ui_graph.MplWidgetGraphEditor.canvas.axes.set_xlabel('Время, ч')
        self.ui_graph.MplWidgetGraphEditor.canvas.axes.legend(u'Эталон', loc='lower center')
        self.ui_graph.MplWidgetGraphEditor.canvas.draw()

    def change_etalon_graph1(self, owen_num, dtime):
        try:
            with open('graph.cfg', 'r') as fr:
                lines = fr.readlines()
                self.temp_line = lines[owen_num * 2 - 2].split()
                self.temp_line = list(map(float, self.temp_line))
                time_line1 = lines[owen_num * 2 - 1].split()
                time_line = []
                for one_line in time_line1:
                    if one_line.find('.') != -1:
                        line = dt.datetime(dtime.year, dtime.month, dtime.day,
                                               int(one_line.split('.')[0]), int(one_line.split('.')[1]))
                        time_line.append(line)
                    else:
                        line = dt.datetime(dtime.year, dtime.month, dtime.day,
                                               int(one_line[0]), 0)
                        time_line.append(line)
                # self.time_line = list(map(float, self.time_line))
                fr.close()
                # print(self.time_line.year)
                return time_line
        except FileNotFoundError:
            print('File graph.cfg not found')


    def change_etalon_graph(self, text):
        if text == 'Печь 1':
            try:
                with open('graph.cfg', 'r') as fr:
                    lines = fr.readlines()
                    self.temp_line = lines[0].split()
                    self.temp_line = list(map(float, self.temp_line))
                    self.time_line = lines[1].split()
                    self.time_line = list(map(float, self.time_line))
                    fr.close()
            except FileNotFoundError:
                print('File graph.cfg not found')
            self.update_lines_graph()
            self.update_etalon_draw()
        if text == 'Печь 2':
            try:
                with open('graph.cfg', 'r') as fr:
                    lines = fr.readlines()
                    self.temp_line = lines[2].split()
                    self.temp_line = list(map(float, self.temp_line))
                    self.time_line = lines[3].split()
                    self.time_line = list(map(float, self.time_line))
                    fr.close()
            except FileNotFoundError:
                print('File graph.cfg not found')
            self.update_lines_graph()
            self.update_etalon_draw()
        if text == 'Печь 3':
            try:
                with open('graph.cfg', 'r') as fr:
                    lines = fr.readlines()
                    self.temp_line = lines[4].split()
                    self.temp_line = list(map(float, self.temp_line))
                    self.time_line = lines[5].split()
                    self.time_line = list(map(float, self.time_line))
                    fr.close()
            except FileNotFoundError:
                print('File graph.cfg not found')
            self.update_lines_graph()
            self.update_etalon_draw()
        if text == 'Печь 4':
            try:
                with open('graph.cfg', 'r') as fr:
                    lines = fr.readlines()
                    self.temp_line = lines[6].split()
                    self.temp_line = list(map(float, self.temp_line))
                    self.time_line = lines[7].split()
                    self.time_line = list(map(float, self.time_line))
                    fr.close()
            except FileNotFoundError:
                print('File graph.cfg not found')
            self.update_lines_graph()
            self.update_etalon_draw()
        if text == 'Печь 5':
            try:
                with open('graph.cfg', 'r') as fr:
                    lines = fr.readlines()
                    self.temp_line = lines[8].split()
                    self.temp_line = list(map(float, self.temp_line))
                    self.time_line = lines[9].split()
                    self.time_line = list(map(float, self.time_line))
                    fr.close()
            except FileNotFoundError:
                print('File graph.cfg not found')
            self.update_lines_graph()
            self.update_etalon_draw()
        if text == 'Печь 6':
            try:
                with open('graph.cfg', 'r') as fr:
                    lines = fr.readlines()
                    self.temp_line = lines[10].split()
                    self.temp_line = list(map(float, self.temp_line))
                    self.time_line = lines[11].split()
                    self.time_line = list(map(float, self.time_line))
                    fr.close()
            except FileNotFoundError:
                print('File graph.cfg not found')
            self.update_lines_graph()
            self.update_etalon_draw()
        if text == 'Печь 7':
            try:
                with open('graph.cfg', 'r') as fr:
                    lines = fr.readlines()
                    self.temp_line = lines[12].split()
                    self.temp_line = list(map(float, self.temp_line))
                    self.time_line = lines[13].split()
                    self.time_line = list(map(float, self.time_line))
                    fr.close()
            except FileNotFoundError:
                print('File graph.cfg not found')
            self.update_lines_graph()
            self.update_etalon_draw()
        if text == 'Печь 8':
            try:
                with open('graph.cfg', 'r') as fr:
                    lines = fr.readlines()
                    self.temp_line = lines[14].split()
                    self.temp_line = list(map(float, self.temp_line))
                    self.time_line = lines[15].split()
                    self.time_line = list(map(float, self.time_line))
                    fr.close()
            except FileNotFoundError:
                print('File graph.cfg not found')
            self.update_lines_graph()
            self.update_etalon_draw()
        if text == 'Печь 9':
            try:
                with open('graph.cfg', 'r') as fr:
                    lines = fr.readlines()
                    self.temp_line = lines[16].split()
                    self.temp_line = list(map(float, self.temp_line))
                    self.time_line = lines[17].split()
                    self.time_line = list(map(float, self.time_line))
                    fr.close()
            except FileNotFoundError:
                print('File graph.cfg not found')
            self.update_lines_graph()
            self.update_etalon_draw()
        if text == 'Печь 10':
            try:
                with open('graph.cfg', 'r') as fr:
                    lines = fr.readlines()
                    self.temp_line = lines[18].split()
                    self.temp_line = list(map(float, self.temp_line))
                    self.time_line = lines[19].split()
                    self.time_line = list(map(float, self.time_line))
                    fr.close()
            except FileNotFoundError:
                print('File graph.cfg not found')
            self.update_lines_graph()
            self.update_etalon_draw()

    def update_lines_graph(self):
        if len(self.temp_line) >= 1:
            self.ui_graph.lineEditTemp1.setText(str(self.temp_line[0]))
        else:
            self.ui_graph.lineEditTemp1.setText('')
        if len(self.temp_line) >= 2:
            self.ui_graph.lineEditTemp2.setText(str(self.temp_line[1]))
        else:
            self.ui_graph.lineEditTemp2.setText('')
        if len(self.temp_line) >= 3:
            self.ui_graph.lineEditTemp3.setText(str(self.temp_line[2]))
        else:
            self.ui_graph.lineEditTemp3.setText('')
        if len(self.temp_line) >= 4:
            self.ui_graph.lineEditTemp4.setText(str(self.temp_line[3]))
        else:
            self.ui_graph.lineEditTemp4.setText('')
        if len(self.temp_line) >= 5:
            self.ui_graph.lineEditTemp5.setText(str(self.temp_line[4]))
        else:
            self.ui_graph.lineEditTemp5.setText('')
        if len(self.temp_line) >= 6:
            self.ui_graph.lineEditTemp6.setText(str(self.temp_line[5]))
        else:
            self.ui_graph.lineEditTemp6.setText('')
        if len(self.temp_line) >= 7:
            self.ui_graph.lineEditTemp7.setText(str(self.temp_line[6]))
        else:
            self.ui_graph.lineEditTemp7.setText('')
        if len(self.temp_line) >= 8:
            self.ui_graph.lineEditTemp8.setText(str(self.temp_line[7]))
        else:
            self.ui_graph.lineEditTemp8.setText('')
        if len(self.temp_line) >= 9:
            self.ui_graph.lineEditTemp9.setText(str(self.temp_line[8]))
        else:
            self.ui_graph.lineEditTemp9.setText('')
        if len(self.temp_line) >= 10:
            self.ui_graph.lineEditTemp10.setText(str(self.temp_line[9]))
        else:
            self.ui_graph.lineEditTemp10.setText('')
        if len(self.temp_line) >= 11:
            self.ui_graph.lineEditTemp11.setText(str(self.temp_line[10]))
        else:
            self.ui_graph.lineEditTemp11.setText('')
        if len(self.temp_line) >= 12:
            self.ui_graph.lineEditTemp12.setText(str(self.temp_line[11]))
        else:
            self.ui_graph.lineEditTemp12.setText('')
        if len(self.temp_line) >= 13:
            self.ui_graph.lineEditTemp13.setText(str(self.temp_line[12]))
        else:
            self.ui_graph.lineEditTemp13.setText('')
        if len(self.temp_line) >= 14:
            self.ui_graph.lineEditTemp14.setText(str(self.temp_line[13]))
        else:
            self.ui_graph.lineEditTemp14.setText('')
        if len(self.temp_line) >= 15:
            self.ui_graph.lineEditTemp15.setText(str(self.temp_line[14]))
        else:
            self.ui_graph.lineEditTemp15.setText('')
        if len(self.temp_line) >= 16:
            self.ui_graph.lineEditTemp16.setText(str(self.temp_line[15]))
        else:
            self.ui_graph.lineEditTemp16.setText('')
        if len(self.temp_line) >= 17:
            self.ui_graph.lineEditTemp17.setText(str(self.temp_line[16]))
        else:
            self.ui_graph.lineEditTemp17.setText('')
        if len(self.temp_line) >= 18:
            self.ui_graph.lineEditTemp18.setText(str(self.temp_line[17]))
        else:
            self.ui_graph.lineEditTemp18.setText('')
        if len(self.temp_line) >= 19:
            self.ui_graph.lineEditTemp19.setText(str(self.temp_line[18]))
        else:
            self.ui_graph.lineEditTemp19.setText('')
        if len(self.temp_line) >= 20:
            self.ui_graph.lineEditTemp20.setText(str(self.temp_line[19]))
        else:
            self.ui_graph.lineEditTemp20.setText('')
        if len(self.temp_line) >= 21:
            self.ui_graph.lineEditTemp21.setText(str(self.temp_line[20]))
        else:
            self.ui_graph.lineEditTemp21.setText('')
        if len(self.temp_line) >= 22:
            self.ui_graph.lineEditTemp22.setText(str(self.temp_line[21]))
        else:
            self.ui_graph.lineEditTemp22.setText('')
        if len(self.temp_line) >= 23:
            self.ui_graph.lineEditTemp23.setText(str(self.temp_line[22]))
        else:
            self.ui_graph.lineEditTemp23.setText('')
        if len(self.temp_line) >= 24:
            self.ui_graph.lineEditTemp24.setText(str(self.temp_line[23]))
        else:
            self.ui_graph.lineEditTemp24.setText('')

        if len(self.time_line) >= 1:
            self.ui_graph.lineEditTime1.setText(str(self.time_line[0]))
        else:
            self.ui_graph.lineEditTime1.setText('')
        if len(self.time_line) >= 2:
            self.ui_graph.lineEditTime2.setText(str(self.time_line[1]))
        else:
            self.ui_graph.lineEditTime2.setText('')
        if len(self.time_line) >= 3:
            self.ui_graph.lineEditTime3.setText(str(self.time_line[2]))
        else:
            self.ui_graph.lineEditTime3.setText('')
        if len(self.time_line) >= 4:
            self.ui_graph.lineEditTime4.setText(str(self.time_line[3]))
        else:
            self.ui_graph.lineEditTime4.setText('')
        if len(self.time_line) >= 5:
            self.ui_graph.lineEditTime5.setText(str(self.time_line[4]))
        else:
            self.ui_graph.lineEditTime5.setText('')
        if len(self.time_line) >= 6:
            self.ui_graph.lineEditTime6.setText(str(self.time_line[5]))
        else:
            self.ui_graph.lineEditTime6.setText('')
        if len(self.time_line) >= 7:
            self.ui_graph.lineEditTime7.setText(str(self.time_line[6]))
        else:
            self.ui_graph.lineEditTime7.setText('')
        if len(self.time_line) >= 8:
            self.ui_graph.lineEditTime8.setText(str(self.time_line[7]))
        else:
            self.ui_graph.lineEditTime8.setText('')
        if len(self.time_line) >= 9:
            self.ui_graph.lineEditTime9.setText(str(self.time_line[8]))
        else:
            self.ui_graph.lineEditTime9.setText('')
        if len(self.time_line) >= 10:
            self.ui_graph.lineEditTime10.setText(str(self.time_line[9]))
        else:
            self.ui_graph.lineEditTime10.setText('')
        if len(self.time_line) >= 11:
            self.ui_graph.lineEditTime11.setText(str(self.time_line[10]))
        else:
            self.ui_graph.lineEditTime11.setText('')
        if len(self.time_line) >= 12:
            self.ui_graph.lineEditTime12.setText(str(self.time_line[11]))
        else:
            self.ui_graph.lineEditTime12.setText('')
        if len(self.time_line) >= 13:
            self.ui_graph.lineEditTime13.setText(str(self.time_line[12]))
        else:
            self.ui_graph.lineEditTime13.setText('')
        if len(self.time_line) >= 14:
            self.ui_graph.lineEditTime14.setText(str(self.time_line[13]))
        else:
            self.ui_graph.lineEditTime14.setText('')
        if len(self.time_line) >= 15:
            self.ui_graph.lineEditTime15.setText(str(self.time_line[14]))
        else:
            self.ui_graph.lineEditTime15.setText('')
        if len(self.time_line) >= 16:
            self.ui_graph.lineEditTime16.setText(str(self.time_line[15]))
        else:
            self.ui_graph.lineEditTime16.setText('')
        if len(self.time_line) >= 17:
            self.ui_graph.lineEditTime17.setText(str(self.time_line[16]))
        else:
            self.ui_graph.lineEditTime17.setText('')
        if len(self.time_line) >= 18:
            self.ui_graph.lineEditTime18.setText(str(self.time_line[17]))
        else:
            self.ui_graph.lineEditTime18.setText('')
        if len(self.time_line) >= 19:
            self.ui_graph.lineEditTime19.setText(str(self.time_line[18]))
        else:
            self.ui_graph.lineEditTime19.setText('')
        if len(self.time_line) >= 20:
            self.ui_graph.lineEditTime20.setText(str(self.time_line[19]))
        else:
            self.ui_graph.lineEditTime21.setText('')
        if len(self.time_line) >= 21:
            self.ui_graph.lineEditTime21.setText(str(self.time_line[20]))
        else:
            self.ui_graph.lineEditTime21.setText('')
        if len(self.time_line) >= 22:
            self.ui_graph.lineEditTime22.setText(str(self.time_line[21]))
        else:
            self.ui_graph.lineEditTime22.setText('')
        if len(self.time_line) >= 23:
            self.ui_graph.lineEditTime23.setText(str(self.time_line[22]))
        else:
            self.ui_graph.lineEditTime23.setText('')
        if len(self.time_line) >= 24:
            self.ui_graph.lineEditTime24.setText(str(self.time_line[23]))
        else:
            self.ui_graph.lineEditTime24.setText('')

    def update_graph(self):
        fs = 500
        f = random.randint(1, 100)
        ts = 1 / fs
        length_of_signal = 100
        t = np.linspace(0, 1, length_of_signal)

        cosinus_signal = np.cos(2 * np.pi * f * t)
        sinus_signal = np.sin(2 * np.pi * f * t)
        self.ui.MplWidget_1.canvas.axes.clear()
        self.ui.MplWidget_1.canvas.axes.plot(t, cosinus_signal)
        self.ui.MplWidget_1.canvas.axes.legend(('Реальная', 'Заданная'), loc='upper right')
        self.ui.MplWidget_1.canvas.draw()

        self.ui.MplWidget_2.canvas.axes.clear()
        self.ui.MplWidget_2.canvas.axes.plot(t, cosinus_signal)
        self.ui.MplWidget_2.canvas.axes.plot(t, sinus_signal)
        self.ui.MplWidget_2.canvas.axes.legend(('Реальная', 'Заданная'), loc='upper right')
        self.ui.MplWidget_2.canvas.draw()

    def update_report_graph(self, x, y):
        self.ui_report.MplWidget.canvas.axes.clear()
        self.ui_report.MplWidget.canvas.axes.plot_date(self.time_line, self.temp_line, '-')
        self.ui_report.MplWidget.canvas.axes.plot_date(x, y, '-')
        self.ui_report.MplWidget.canvas.axes.set_ylabel('Градусы, °С')
        self.ui_report.MplWidget.canvas.axes.set_xlabel('Время, ч')
        self.ui_report.MplWidget.canvas.axes.legend('Программа', 'Факт', loc='lower center')
        self.ui_report.MplWidget.canvas.draw()

    def update_tab_graph(self, index):
        # Считываем значения из файла 'graph.cfg'
        try:
            with open('graph.cfg', 'r') as fr:
                lines = fr.readlines()
                self.temp_line_current_tab = lines[index * 2].split()
                # self.temp_line_current_tab = list(map(float, self.temp_line_current_tab))
                self.time_line_current_tab = lines[index * 2 + 1].split()
                # self.time_line_current_tab = list(map(float, self.time_line_current_tab))
                fr.close()
        except FileNotFoundError:
            print('File graph.cfg not found')
        self.plots[index].canvas.axes.clear()
        self.plots[index].canvas.axes.set_title('Печь №' + str(index + 1))
        # self.plots[index].canvas.axes.plot_date(self.time_line_current_tab, self.temp_line_current_tab, '-')
        x, y = self.get_last_graph_points(index + 1)
        self.plots[index].canvas.axes.plot_date(x, y, '-')
        print(self.get_last_graph_points(index + 1))
        self.plots[index].canvas.axes.legend(('Заданная', 'Реальная'), loc='upper left')
        self.plots[index].canvas.axes.grid()
        self.plots[index].canvas.draw()


    def convert_time(self, my_time, dtime):
        if my_time:
            time = my_time.split('.')
            return dt.datetime(dtime.year, dtime.month, dtime.day, time[0], time[1])
        return 0


    def get_last_graph_points2(self, files):
        realtime_data_timeline = []
        realtime_data_temperature = []
        if files:
            for file in files:
                with open(file, 'r', newline='') as fp:
                    reader = csv.reader(fp, delimiter=';')
                    if reader:
                        for row in reader:
                            # timeline = time.strftime("%H.%M", time.localtime(int(row[0])))
                            # data = [int(row[1]), float(timeline)]
                            realtime_data_timeline.append(dt.datetime.fromtimestamp(int(row[0])))
                            realtime_data_temperature.append(int(row[1]))
                    else:
                        return [[]]
            return realtime_data_timeline, realtime_data_temperature
        else:
            return [[]]


    def get_last_graph_points1(self, files):
        realtime_data_timeline = []
        realtime_data_temperature = []
        if files:
            for file in files:
                with open(file, 'r', newline='') as fp:
                    reader = csv.reader(fp, delimiter=';')
                    if reader:
                        for row in reader:
                            # timeline = time.strftime("%H.%M", time.localtime(int(row[0])))
                            # data = [int(row[1]), float(timeline)]
                            realtime_data_timeline.append(row[0])
                            realtime_data_temperature.append(int(row[1]))
                    else:
                        return [[]]
            return realtime_data_timeline, realtime_data_temperature
        else:
            return [[]]

    def get_last_graph_points(self, num):
        # Извлекаем текущий месяц для проверки существует ли такая папка
        time_current = time.strftime("%Y,%m,%d,%H,%M,%S")
        t = time_current.split(',')
        numbers = [int(x) for x in t]
        # Проверяем есть ли такая папка если нет, то создаем ее
        if os.path.isdir(r'.\dat' + '\\' + str(numbers[1]) + '\\' + str(numbers[2])):
            path = r'.\dat' + '\\' + str(numbers[1]) + '\\' + str(numbers[2])
        else:
            os.makedirs(r'.\dat' + '\\' + str(numbers[1]) + '\\' + str(numbers[2]))
            path = r'.\dat' + '\\' + str(numbers[1]) + '\\' + str(numbers[2])

        file_names = glob.glob1(path, "owen" + str(num) + "*")
        print('Files count:{}', len(file_names))
        realtime_data_timeline = []
        realtime_data_temperature = []

        if file_names:
            for file in file_names:
                with open(path + '\\' + file, 'r', newline='') as fp:
                    reader = csv.reader(fp, delimiter=';')
                    if reader:
                        for row in reader:
                            # timeline = time.strftime("%H.%M", time.localtime(int(row[0])))
                            # data = [int(row[1]), float(timeline)]
                            realtime_data_timeline.append(row[0])
                            realtime_data_temperature.append(int(row[1]))
                    else:
                        return []
            return realtime_data_timeline, realtime_data_temperature
        else:
            return []


        # преобразование временной метки в часы,минуты
        # time.strftime("%H,%M", time.localtime(int("1560878283")))
        # print(realtime_data[-1][0])
        # print(realtime_data[-1][1])


def main():
    app = QtWidgets.QApplication([])  # Новый экземпляр QApplication
    application = mywindow()  # Создаём объект класса mywindow
    application.show()  # Показываем окно
    sys.exit(app.exec())  # и запускаем приложение


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()
