from PyQt5 import QtCore
from PyQt5.QtCore import QObject, QIODevice
from PyQt5.QtSerialPort import QSerialPort
from PyQt5.QtSerialPort import QSerialPortInfo
import time


class SerialWorker(QtCore.QObject):
    """
    Класс для создания отдельного потока считывания данных из
    COM порта
    """
    serial = QSerialPort()

    def __init__(self, port_name='COM1', baudrate=9600):
        QtCore.QObject.__init__(self)
        self.port_name = port_name
        self.baudrate = baudrate

    def task(self):
        while True:
            info = QSerialPortInfo.availablePorts()
            if not self.serial.isOpen():
                for inf in info:
                    if inf.portName() == self.port_name:
                        try:
                            self.serial.setPortName(self.port_name)
                            self.serial.setBaudRate(self.baudrate)
                            self.serial.setParity(QSerialPort.NoParity)
                            self.serial.setDataBits(QSerialPort.Data8)
                            self.serial.setStopBits(QSerialPort.OneStop)
                            self.serial.open(QIODevice.ReadWrite)
                            # self.serial.readyRead.connect(self.on_serial_read)
                        except IOError:
                            print("Cannot connect to device on port {}".format(self.port_name))
            else:
                data = serial.readall()



            time.sleep(1)
