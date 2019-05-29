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
        with open('graph.cfg', 'r') as fr:
            line = fr.readline()
            self.temp_line = line.split()
            self.temp_line = list(map(float, self.temp_line))
            line = fr.readline()
            self.time_line = line.split()
            self.time_line = list(map(float, self.time_line))
            fr.close()
        print('temp_line[0]:')
        # print(self.temp_line[0])
        if len(self.temp_line) >= 1:
            self.ui_graph.lineEditTemp1.setText(str(self.temp_line[0]))
        if len(self.temp_line) >= 2:
            self.ui_graph.lineEditTemp2.setText(str(self.temp_line[1]))
        if len(self.temp_line) >= 3:
            self.ui_graph.lineEditTemp3.setText(str(self.temp_line[2]))
        if len(self.temp_line) >= 4:
            self.ui_graph.lineEditTemp4.setText(str(self.temp_line[3]))
        if len(self.temp_line) >= 5:
            self.ui_graph.lineEditTemp5.setText(str(self.temp_line[4]))
        if len(self.temp_line) >= 6:
            self.ui_graph.lineEditTemp6.setText(str(self.temp_line[5]))
        if len(self.temp_line) >= 7:
            self.ui_graph.lineEditTemp7.setText(str(self.temp_line[6]))
        if len(self.temp_line) >= 8:
            self.ui_graph.lineEditTemp8.setText(str(self.temp_line[7]))
        if len(self.temp_line) >= 9:
            self.ui_graph.lineEditTemp9.setText(str(self.temp_line[8]))
        if len(self.temp_line) >= 10:
            self.ui_graph.lineEditTemp10.setText(str(self.temp_line[9]))
        if len(self.temp_line) >= 11:
            self.ui_graph.lineEditTemp11.setText(str(self.temp_line[10]))
        if len(self.temp_line) >= 12:
            self.ui_graph.lineEditTemp12.setText(str(self.temp_line[11]))
        if len(self.temp_line) >= 13:
            self.ui_graph.lineEditTemp13.setText(str(self.temp_line[12]))
        if len(self.temp_line) >= 14:
            self.ui_graph.lineEditTemp14.setText(str(self.temp_line[13]))
        if len(self.temp_line) >= 15:
            self.ui_graph.lineEditTemp15.setText(str(self.temp_line[14]))
        if len(self.temp_line) >= 16:
            self.ui_graph.lineEditTemp16.setText(str(self.temp_line[15]))
        if len(self.temp_line) >= 17:
            self.ui_graph.lineEditTemp17.setText(str(self.temp_line[16]))
        if len(self.temp_line) >= 18:
            self.ui_graph.lineEditTemp18.setText(str(self.temp_line[17]))
        if len(self.temp_line) >= 19:
            self.ui_graph.lineEditTemp19.setText(str(self.temp_line[18]))
        if len(self.temp_line) >= 20:
            self.ui_graph.lineEditTemp20.setText(str(self.temp_line[19]))
        if len(self.temp_line) >= 21:
            self.ui_graph.lineEditTemp21.setText(str(self.temp_line[20]))
        if len(self.temp_line) >= 22:
            self.ui_graph.lineEditTemp22.setText(str(self.temp_line[21]))
        if len(self.temp_line) >= 23:
            self.ui_graph.lineEditTemp23.setText(str(self.temp_line[22]))
        if len(self.temp_line) >= 24:
            self.ui_graph.lineEditTemp24.setText(str(self.temp_line[23]))

        if len(self.time_line) >= 1:
            self.ui_graph.lineEditTime1.setText(str(self.time_line[0]))
        if len(self.time_line) >= 2:
            self.ui_graph.lineEditTime2.setText(str(self.time_line[1]))
        if len(self.time_line) >= 3:
            self.ui_graph.lineEditTime3.setText(str(self.time_line[2]))
        if len(self.time_line) >= 4:
            self.ui_graph.lineEditTime4.setText(str(self.time_line[3]))
        if len(self.time_line) >= 5:
            self.ui_graph.lineEditTime5.setText(str(self.time_line[4]))
        if len(self.time_line) >= 6:
            self.ui_graph.lineEditTime6.setText(str(self.time_line[5]))
        if len(self.time_line) >= 7:
            self.ui_graph.lineEditTime7.setText(str(self.time_line[6]))
        if len(self.time_line) >= 8:
            self.ui_graph.lineEditTime8.setText(str(self.time_line[7]))
        if len(self.time_line) >= 9:
            self.ui_graph.lineEditTime9.setText(str(self.time_line[8]))
        if len(self.time_line) >= 10:
            self.ui_graph.lineEditTime10.setText(str(self.time_line[9]))
        if len(self.time_line) >= 11:
            self.ui_graph.lineEditTime11.setText(str(self.time_line[10]))
        if len(self.time_line) >= 12:
            self.ui_graph.lineEditTime12.setText(str(self.time_line[11]))
        if len(self.time_line) >= 13:
            self.ui_graph.lineEditTime13.setText(str(self.time_line[12]))
        if len(self.time_line) >= 14:
            self.ui_graph.lineEditTime14.setText(str(self.time_line[13]))
        if len(self.time_line) >= 15:
            self.ui_graph.lineEditTime15.setText(str(self.time_line[14]))
        if len(self.time_line) >= 16:
            self.ui_graph.lineEditTime16.setText(str(self.time_line[15]))
        if len(self.time_line) >= 17:
            self.ui_graph.lineEditTime17.setText(str(self.time_line[16]))
        if len(self.time_line) >= 18:
            self.ui_graph.lineEditTime18.setText(str(self.time_line[17]))
        if len(self.time_line) >= 19:
            self.ui_graph.lineEditTime19.setText(str(self.time_line[18]))
        if len(self.time_line) >= 20:
            self.ui_graph.lineEditTime20.setText(str(self.time_line[19]))
        if len(self.time_line) >= 21:
            self.ui_graph.lineEditTime21.setText(str(self.time_line[20]))
        if len(self.time_line) >= 22:
            self.ui_graph.lineEditTime22.setText(str(self.time_line[21]))
        if len(self.time_line) >= 23:
            self.ui_graph.lineEditTime23.setText(str(self.time_line[22]))
        if len(self.time_line) >= 24:
            self.ui_graph.lineEditTime24.setText(str(self.time_line[23]))

        self.ui_graph.MplWidgetGraphEditor.canvas.axes.clear()
        self.ui_graph.MplWidgetGraphEditor.canvas.axes.plot(self.time_line, self.temp_line, lw=2)
        self.ui_graph.MplWidgetGraphEditor.canvas.axes.set_ylabel('Градусы, °С')
        self.ui_graph.MplWidgetGraphEditor.canvas.axes.set_xlabel('Время, ч')
        self.ui_graph.MplWidgetGraphEditor.canvas.axes.legend(u'Эталон', loc='lower center')
        self.ui_graph.MplWidgetGraphEditor.canvas.draw()

        self.window_graph.show()

    def ports_open(self):
        self.window_ports = QtWidgets.QMainWindow()
        self.ui_ports = Ui_Form()
        self.ui_ports.setupUi(self.window_ports)
        for dev in comports():
            self.ui_ports.port_Name_comboBox.addItem(str(dev).split()[0])
        self.ui_ports.port_Name_comboBox.editTextChanged.connect(self.port_name_changed)
        self.window_ports.show()

    def port_name_changed(self):
        print('1111')
        # print(self.ui_ports.port_Name_comboBox.currentText())

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
        # with open('graph.cfg', 'r') as file:
        #     line = file.readline()
        #     line2 = line.split()
        #     print(line2[1])
        #     print(line2[0])
        with open('graph.cfg', 'w') as graph_file:
            # for graph_text in graph_file:
            #     graph_text.append(graph_file.readline())
            graph_file.write(" ".join(map(str, self.temp_line)))
            graph_file.write('\n')
            graph_file.write(" ".join(map(str, self.time_line)))
            graph_file.close()
        self.ui_graph.MplWidgetGraphEditor.canvas.axes.clear()
        self.ui_graph.MplWidgetGraphEditor.canvas.axes.plot(self.time_line, self.temp_line, lw=2)
        self.ui_graph.MplWidgetGraphEditor.canvas.axes.set_ylabel('Градусы, °С')
        self.ui_graph.MplWidgetGraphEditor.canvas.axes.set_xlabel('Время, ч')
        self.ui_graph.MplWidgetGraphEditor.canvas.axes.legend(u'Эталон', loc='lower center')
        self.ui_graph.MplWidgetGraphEditor.canvas.draw()

        print(self.temp_line)
        print(self.time_line)

    def update_graph(self):
        fs = 500
        f = random.randint(1, 100)
        ts = 1 / fs
        length_of_signal = 100
        t = np.linspace(0, 1, length_of_signal)

        cosinus_signal = np.cos(2 * np.pi * f * t)
        sinus_signal = np.sin(2 * np.pi * f * t)
        # print('t')
        # print(t)
        # print('cosinus')
        # print(cosinus_signal)
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
