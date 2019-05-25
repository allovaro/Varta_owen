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
# import mplwidget


class mywindow(QtWidgets.QMainWindow):

    tray_icon = None
    etalon_temp = None

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
        self.ui = Ui_Graph_editor()
        self.ui.setupUi(self.window_graph)
        self.ui.MplWidgetGraphEditor.canvas.axes.set_title('Эталон')
        # self.ui.lineEdit.editingFinished.connect(self.update_etalon_graph)
        self.etalon_temp = [100, 200, 300]
        self.etalon_time = [1, 2, 3]
        self.ui.MplWidgetGraphEditor.canvas.axes.clear()
        self.ui.MplWidgetGraphEditor.canvas.axes.plot(self.etalon_time, self.etalon_temp)
        self.ui.MplWidgetGraphEditor.canvas.draw()
        self.window_graph.show()

    def ports_open(self):
        self.window_ports = QtWidgets.QMainWindow()
        self.ui_ports = Ui_Form()
        self.ui_ports.setupUi(self.window_ports)
        for dev in comports():
            self.ui_ports.port_Name_comboBox.addItem(str(dev).split()[0])
        self.ui_ports.port_Name_comboBox.editTextChanged.connect(self.port_name_changed())
        self.window_ports.show()

    def port_name_changed(self):
        print('1111')
        print(self.ui_ports.port_Name_comboBox.currentText())

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
        print(self.ui.lineEdit.text())
        with open('graph.cfg', 'r') as graph_file:
            for graph_text in graph_file:
                graph_text.append(graph_file.readline())
        print(graph_text)

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
        self.ui.MplWidget_1.canvas.axes.plot(t, sinus_signal)
        self.ui.MplWidget_1.canvas.axes.legend(('Реальная', 'Заданная'), loc='upper right')
        self.ui.MplWidget_1.canvas.draw()


def main():
    app = QtWidgets.QApplication([])  # Новый экземпляр QApplication
    application = mywindow()  # Создаём объект класса mywindow
    application.show()  # Показываем окно

    sys.exit(app.exec())  # и запускаем приложение


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()