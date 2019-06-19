from PyQt5.QtCore import Qt
from PyQt5.QtCore import QThread
import serial
import sys

class SerialReadThread(QThread):

    def __init__(self, serial):
        QThread.__init__(self)
        self.cond = QWaitCondition()
        self._status = False
        self.mutex = QMutex()
        self.serial = serial

    def __del__(self):
        self.wait()

    def run(self):
        """

        :return:
        """
        while True: