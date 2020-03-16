from PyQt5 import QtCore
from PyQt5.QtCore import QObject, QIODevice
from PyQt5.QtCore import (Qt, pyqtSignal)
import serial
from PyQt5.QtSerialPort import QSerialPortInfo
import time
import os
import csv
import datetime as dt
from temp_analyzer import *
from smsc_api import *
import logging


class SerialWorker(QtCore.QObject):
    """
    Класс для создания отдельного потока считывания данных из
    COM порта
    """
    port_opened = pyqtSignal(str)
    currTemp = pyqtSignal(str)
    smsc = SMSC()
    analyzer = Analyzer()
    logger = None
    prev_cycle_temp = 0

    def __init__(self, owen_num, port_name='', baudrate=9600):
        QtCore.QObject.__init__(self)
        self.port_name = port_name
        self.baudrate = baudrate
        self.serial_port = serial.Serial()
        self.owen_num = str(owen_num)
        self.init_logging()

    def task(self):
        """
        Основная задача по считыванию данных из порта и записи в файл. Каждая задача
        пишет температуру в отдельный файл. разбивает по месяцам и дням.
        :return:
        """
        # if self.owen_num == '1':
            # print(self.smsc.get_balance())
            # self.smsc.send_sms("79064168910", "Привет от варты", sender="sms")
        prev_status = 'EMPTY'
        port_status = False
        while True:
            time.sleep(1)
            info = QSerialPortInfo.availablePorts()
            if self.serial_port.isOpen():
                self.port_opened.emit('open')
                if not port_status:
                    self.logger.info(f'Порт {self.port_name} открыт')
                port_status = True
                try:
                    data = self.serial_port.readline().decode("ascii")
                    data = data.rstrip()
                    if self.check_temperature(data):
                        self.currTemp.emit(data)
                except serial.SerialException:
                    self.serial_port.close()
                    self.port_opened.emit('close')
                    port_status = False
                    self.logger.info(f'Порт {self.port_name} закрыт')
                    self.currTemp.emit('-1')
                    # print('Port {} error'.format(self.port_name))

                work_path = self.check_dir_path()  # Проверяем существует ли папка с текущим днем если нет, то создаем
                file_name = self.last_file_name(600, work_path, self.owen_num)
                if file_name == '-1':  # Проверка есть ли файл старше 15 минут
                    self.create_new_file(work_path)
                else:
                    try:
                        if self.check_temperature(data):
                            data_int = int(data)
                            print(data_int)
                            if data_int != self.prev_cycle_temp:
                                self.prev_cycle_temp = data_int
                                self.add_new_data(work_path + '\\' + file_name, data_int)
                                self.analyzer.execute_analysis(self.owen_num, data_int)
                                status = self.analyzer.tracking_status
                                if prev_status != status:
                                    self.logger.info(f'Статус отслеживания температуры {self.analyzer.tracking_status}')
                                prev_status = status
                    except:
                        return False
            else:
                self.port_opened.emit('close')
                for inf in info:
                    if inf.portName() == self.port_name:
                        # print('Inf.portName = {}, config_port_name = {}'.format(inf.portName(), self.port_name))
                        if not self.serial_port.isOpen():
                            try:
                                self.serial_port.port = self.port_name
                                self.serial_port.timeout = None
                                self.serial_port.baudrate = self.baudrate
                                self.serial_port.bytesize = serial.EIGHTBITS  # number of bits per bytes
                                self.serial_port.parity = serial.PARITY_NONE  # set parity check: no parity
                                self.serial_port.stopbits = serial.STOPBITS_ONE  # number of stop bits
                                self.serial_port.open()
                            except IOError:
                                self.logger.error("Cannot connect to device on port {}".format(inf.portName()))
                                print("Cannot connect to device on port {}".format(inf.portName()))
                            except:
                                self.logger.error("Something else goes wrong")
                                print("Something else goes wrong")

    def check_dir_path(self):
        """
        Проверка наличия папки месяца и дня, если нужных папок нет, то они будут созданы
        :return:
        Возвращает путь к файлам
        """
        # Извлекаем текущий месяц для проверки существует ли такая папка
        numbers = self.current_time()
        # Проверяем есть ли такая папка если нет, то создаем ее
        if os.path.isdir(r'.\dat' + '\\' + str(numbers[1]) + '\\' + str(numbers[2])):
            return r'.\dat' + '\\' + str(numbers[1]) + '\\' + str(numbers[2])
        else:
            os.makedirs(r'.\dat' + '\\' + str(numbers[1]) + '\\' + str(numbers[2]))
            return r'.\dat' + '\\' + str(numbers[1]) + '\\' + str(numbers[2])

    def current_time(self):
        time_current = time.strftime("%Y,%m,%d,%H,%M,%S")
        t = time_current.split(',')
        return [int(x) for x in t]

    def last_file_name(self, interval_secs, path, num):
        """
        Проверка наличия файла для записи файла или создание нового
        :return:
        Возвращает название последнего файла для дозаписи
        """
        numbers = self.current_time()
        files = os.listdir(path)
        if len(files) != 0:
            for file in reversed(files):
                if file.rfind('owen' + num) != -1:
                    hour = int(file[-8:-6])
                    min = int(file[-6:-4])
                    sec_file = hour * 3600 + min * 60
                    sec_time = numbers[3] * 3600 + numbers[4] * 60
                    # print('Minus{}', sec_time - sec_file)
                    # print('sec_file{}; sec_time{}', sec_file, sec_time)
                    if sec_file > sec_time - interval_secs:
                        return file
        return '-1'

    def create_new_file(self, path):
        """
        Создание нового файла
        :return:
        """
        numbers = self.current_time()
        if path[-1] == '\\':
            name = 'owen' + self.owen_num + '_' + str(numbers[0])
        else:
            name = '\\' + 'owen' + self.owen_num + '_' + str(numbers[0])
        if numbers[1] < 10:
            name = name + '0' + str(numbers[1])
        else:
            name += str(numbers[1])
        if numbers[2] < 10:
            name += '0' + str(numbers[2])
        else:
            name += str(numbers[2])
        name += '_'
        if numbers[3] < 10:
            name += '0' + str(numbers[3])
        else:
            name += str(numbers[3])
        if numbers[4] < 10:
            name += '0' + str(numbers[4])
        else:
            name += str(numbers[4])
        name += '.csv'
        f = open(path + name, 'w')
        self.logger.info(f'Создан новый файл {path + name}')
        f.close()

    @staticmethod
    def add_new_data(file, num):
        with open(file, 'a', newline='') as fp:
            writer = csv.writer(fp, delimiter=';')
            # writer.writerow([int(time.time()), num])  # write header
            # writer.writerow([datetime.datetime.today(), num])
            writer.writerow([int(time.time()), num])
            # writer.writerow([time.strftime("%H.%M:%S", time.localtime(int(time.time()))), num])

    def init_logging(self):
        self.logger = logging.getLogger('SerialWorker' + str(self.owen_num))
        self.logger.setLevel(logging.INFO)
        # create the logging file handler
        fh = logging.FileHandler('logs.log')

        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        self.logger.addHandler(fh)

    @staticmethod
    def check_temperature(data):
        if len(data) == 4 and data != '9999':
            return True
        else:
            return False
    # def execute_analysis(self, obj, act_temperature):
    #     obj.add_new_value(act_temperature)  # Добавляем текущее значение температуры в буффер
    #     print(obj.temperature_memory)
    #     if len(obj.temperature_memory) >= 14:
    #         aver1 = (obj.temperature_memory[0] + obj.temperature_memory[1] + obj.temperature_memory[2]) / 3
    #         aver2 = (obj.temperature_memory[-1] + obj.temperature_memory[-2] + obj.temperature_memory[-3]) / 3
    #         if aver1 > aver2:   # Определяем направление температуры нагрев или остывание
    #             obj.temperature_direction = 'DOWN'
    #         else:
    #             obj.temperature_direction = 'UP'
    #         print(obj.in_range)
    #         if not obj.in_range:
    #             obj.in_range = True
    #             points = obj.find_points('graph.cfg', int(self.owen_num), act_temperature)
    #
    #         if obj.in_range:
    #             prediction = obj.get_prediction()
    #             if prediction + obj.delta > act_temperature > prediction - obj.delta:
    #                 pass
    #             else:
    #                 obj.big_difference = True
    #                 obj.start_timer = dt.datetime.today()
