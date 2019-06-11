from PyQt5 import QtCore
from PyQt5.QtCore import QObject, QIODevice
import serial
from PyQt5.QtSerialPort import QSerialPortInfo
import time


class SerialWorker(QtCore.QObject):
    """
    Класс для создания отдельного потока считывания данных из
    COM порта
    """
    serial_port = serial.Serial()

    def __init__(self, port_name='COM1', baudrate=9600):
        QtCore.QObject.__init__(self)
        self.port_name = port_name
        self.baudrate = baudrate

    def task(self):
        while True:
            info = QSerialPortInfo.availablePorts()
            if self.serial_port.isOpen():
                data = serial_port.readall()
                print(data)
            else:
                for inf in info:
                    if inf.portName() == self.port_name:
                        print('Inf.portName = {}, config_port_name = {}'.format(inf.portName(), self.port_name))
                        if not self.serial_port.isOpen():
                            try:
                                self.serial_port.port = self.port_name
                                self.serial_port.baudrate = self.baudrate
                                self.serial_port.bytesize = serial.EIGHTBITS  # number of bits per bytes
                                self.serial_port.parity = serial.PARITY_NONE  # set parity check: no parity
                                self.serial_port.stopbits = serial.STOPBITS_ONE  # number of stop bits
                                self.serial_port.open()


                                # self.serial.readyRead.connect(self.on_serial_read)
                            except IOError:
                                print("Cannot connect to device on port {}".format(inf.portName()))
                            except:
                                print("Something else goes wrong")
            time.sleep(1)
