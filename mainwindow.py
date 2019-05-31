from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5.QtWidgets import QSystemTrayIcon, QStyle, QAction, QMenu, qApp
from mainwindow_ui import Ui_MainWindow  # импорт нашего сгенерированного файла
from port_parameters_ui import Ui_Form
from graph_ui import Ui_Graph_editor
import sys
import serial
from serial.tools.list_ports_windows import comports

from matplotlib.backends.backend_qt5agg import (NavigationToolbar2QT as NavigationToolbar)
import numpy as np
import random


class mywindow(QtWidgets.QMainWindow):
    tray_icon = None
    etalon_temp = None
    
    time_line = []
    temp_line = []

    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Соединения кнопок меню
        self.ui.exit.triggered.connect(qApp.quit)
        self.ui.ports.triggered.connect(self.ports_open)
        self.ui.graph.triggered.connect(self.graph_open)

        # Настройка графиков
        self.ui.MplWidget_1.canvas.axes.set_title('Печь №1')
        self.ui.MplWidget_2.canvas.axes.set_title('Печь №2')
        self.ui.MplWidget_3.canvas.axes.set_title('Печь №3')
        self.ui.MplWidget_4.canvas.axes.set_title('Печь №4')
        self.ui.MplWidget_5.canvas.axes.set_title('Печь №5')
        self.ui.MplWidget_6.canvas.axes.set_title('Печь №6')
        self.ui.MplWidget_7.canvas.axes.set_title('Печь №7')
        self.ui.MplWidget_8.canvas.axes.set_title('Печь №8')
        self.ui.MplWidget_9.canvas.axes.set_title('Печь №9')
        self.ui.MplWidget_10.canvas.axes.set_title('Печь №10')

        self.update_graph()

        # Инициализируем QSystemTrayIcon

        self.tray_icon = QSystemTrayIcon(self)
        self.tray_icon.setIcon(QtGui.QIcon('lines.png'))
        # self.tray_icon.setIcon(self.style().standardIcon(QStyle.SP_ComputerIcon))
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

    def closeEvent(self, event):
        event.ignore()
        self.hide()
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
        self.ui_ports.port_Name_comboBox.editTextChanged.connect(self.port_name_changed)
        self.window_ports.show()
        try:
            with open('port_configuration.cfg', 'r') as fr:
                lines = fr.readlines()
                self.temp_line = lines[0].split()
                self.temp_line = list(map(float, self.temp_line))
                # line = fr.readline()
                self.time_line = lines[1].split()
                self.time_line = list(map(float, self.time_line))
                fr.close()
        except FileNotFoundError:
            print('File port_configuration.cfg not found')
            with open('port_configuration.cfg', 'w') as fr:
                for i in range(50):
                    fr.write('\n')
                fr.close()

    def port_name_changed(self):
        # print('1111')
        print(self.ui_ports.port_Name_comboBox.currentText())
        print(self.ui_ports.owenName_comboBox.currentText())
        # ser = serial.Serial()  # open serial port
        # ser.baudrate = 9600
        # ser.stopbits = 1
        # ser.parity = 'N'
        # ser.port = 'COM12'
        # ser.open()
        # print(ser.read(6))
        # ser.close()
        # global window2
        # if window2 is None:
        # window2 = port_parameters_ui.Ui_Form()
        # window2.show()
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
        self.ui.MplWidget_1.canvas.axes.plot([1, 2, 3], [1, 2, 1])
        self.ui.MplWidget_1.canvas.axes.legend(('Реальная', 'Заданная'), loc='upper right')
        self.ui.MplWidget_1.canvas.draw()

        self.ui.MplWidget_2.canvas.axes.clear()
        self.ui.MplWidget_2.canvas.axes.plot(t, cosinus_signal)
        self.ui.MplWidget_2.canvas.axes.plot(t, sinus_signal)
        self.ui.MplWidget_2.canvas.axes.legend(('Реальная', 'Заданная'), loc='upper right')
        self.ui.MplWidget_2.canvas.draw()


def main():
    app = QtWidgets.QApplication([])  # Новый экземпляр QApplication
    application = mywindow()  # Создаём объект класса mywindow
    application.show()  # Показываем окно

    sys.exit(app.exec())  # и запускаем приложение


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()
