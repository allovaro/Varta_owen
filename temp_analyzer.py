import datetime as dt
import time


class Analyzer(object):
    temperature_direction = 'ODD'
    in_range = False
    tracking_status = 'IDLE'
    temperature_average = 0
    temperature_memory = []
    prev_temp = 0
    prev_time = 0
    next_temp = 0
    next_time = 0
    big_difference = False
    delta_val = 3
    start_timer = None
    points = None

    def execute_analysis(self, owen_num, act_temperature):
        self.add_new_value(act_temperature)  # Добавляем текущее значение температуры в буффер
        # print(self.tracking_status)
        if self.tracking_status == 'IDLE':
            if len(self.temperature_memory) >= 14:
                aver1 = (self.temperature_memory[0] + self.temperature_memory[1] + self.temperature_memory[2]) / 3
                aver2 = (self.temperature_memory[-1] + self.temperature_memory[-2] + self.temperature_memory[-3]) / 3
                if aver1 > aver2:   # Определяем направление температуры нагрев или остывание
                    self.temperature_direction = 'DOWN'
                    self.tracking_status = 'SICKING_POINTS'
                    print('Температура падает')
                else:
                    self.temperature_direction = 'UP'
                    self.tracking_status = 'SICKING_POINTS'
                    print('Температура растет')

        # Определяем между какими точками графика находимся
        elif self.tracking_status == 'SICKING_POINTS':
            self.points = self.find_points('graph.cfg', owen_num, act_temperature)
            print(self.points)
            if self.points:
                self.prev_time = dt.datetime.today()
                self.next_time = self.prev_time + dt.timedelta(minutes=self.points[1][1] -
                                                                       self.points[1][0])
                if self.temperature_direction == 'UP':
                    self.prev_temp = self.points[0][0]
                    self.next_temp = self.points[0][1]
                    if self.next_temp - 10 <= act_temperature or self.prev_temp >= act_temperature:
                        self.in_range = True
                    else:
                        if self.in_range:
                            self.tracking_status = 'TRACKING'

                if self.temperature_direction == 'DOWN':
                    self.prev_temp = self.points[0][2]
                    self.next_temp = self.points[0][3]
                    if self.next_temp + 10 <= act_temperature or self.prev_temp >= act_temperature:
                        self.in_range = True
                    else:
                        if self.in_range:
                            self.tracking_status = 'TRACKING'
            # print('next_time = {} prev_time = {}'.format(self.next_time, self.prev_time))
            print('prev_temp = {} act_temp = {}'.format(self.prev_temp, act_temperature))
            print('next_temp = {} act_temp = {}'.format(self.next_temp, act_temperature))


        # Ждем когда дойдем до точки чтобы зафиксировать время и от последнего
        # в дальнейшем отталкиваться для расчета точки в будущем
        elif self.tracking_status == 'WAIT_ON_PATH':
            if self.next_temp -3 < act_temperature < self.next_temp + 3:
                self.tracking_status = 'SICKING_POINTS'
            if self.temperature_direction == 'UP':
                print('Prev_temp = {}'.format(self.prev_temp))
                print('Next_temp = {}'.format(self.next_temp))
            if self.temperature_direction == 'DOWN':
                print('Prev_temp = {}'.format(self.prev_temp))
                print('Next_temp = {}'.format(self.next_temp))

        # Отслеживаем по графику температуру
        elif self.tracking_status == 'TRACKING':
            prediction = self.get_prediction()
            print('Actual_temp = {}, Prediction = {}'.format(act_temperature, prediction))
            if prediction - self.delta_val < act_temperature < prediction + self.delta_val:
                pass
            else:
                self.big_difference = True
                self.start_timer = dt.datetime.today()

    @staticmethod
    def calc_average(all_values):
        if all_values:
            res = 0
            for val in all_values:
                res += val
            return res / len(all_values)
        else:
            return False

    def add_new_value(self, new_value):
        if self.temperature_memory:
            if new_value != self.get_last_value():
                if len(self.temperature_memory) < 15:
                    self.temperature_memory.append(new_value)
                else:
                    self.temperature_memory.pop(0)
                    self.temperature_memory.append(new_value)
        else:
            self.temperature_memory.append(new_value)
        # print(len(self.temperature_memory))

    @staticmethod
    def find_and_add_check_point(curr_value, next_check_point):
        if next_check_point - 10 <= curr_value <= next_check_point:
            return curr_value, dt.datetime.today()

    @staticmethod
    def calc_next_timestamp(time1, time2, timestamp):
        """
        Функция вычисляет смещение второй опорной точки для построения графика прямой
        по двух точкам.
        return: Объект типа время
        """
        temp = time1.split('.')
        mins = 0
        mins2 = 0
        if len(temp) >= 2:
            mins = int(temp[0]) * 60 + int(temp[1]) * 10
        temp = time2.split('.')
        if len(temp) >= 2:
            mins2 = int(temp[0]) * 60 + int(temp[1]) * 10
        if mins != 0 and mins2 != 0:
            return timestamp + dt.timedelta(minutes=(mins2 - mins))
        else:
            return 0

    def get_prediction(self):
        """
        С помощью уравнения прямой по двум точкам расчет следущей
        величины температуры по текущему времени
        """
        next_time = dt.datetime(self.next_time.year, self.next_time.month, self.next_time.day,
                                self.next_time.hour, self.next_time.minute, self.next_time.second).timestamp()
        prev_time = dt.datetime(self.prev_time.year, self.prev_time.month, self.prev_time.day,
                                self.prev_time.hour, self.prev_time.minute, self.prev_time.second).timestamp()
        temp1 = next_time * self.prev_temp - prev_time * self.next_temp
        temp2 = dt.datetime.today().timestamp() * (self.prev_temp - self.next_temp)
        temp3 = next_time - prev_time
        return (temp1 - temp2) / temp3

    def get_last_value(self):
        return self.temperature_memory[-1]

    @staticmethod
    def find_points(file_name, owen_num, current_val):
        array = []
        array_time = []
        try:
            with open(file_name, 'r') as file:
                for i in range(owen_num * 2 - 1):
                    line = file.readline()
                line_time = file.readline()
                if line:
                    array = list(map(float, line.split(' ')))
                    if line_time:
                        array_time = list(map(float, line_time.split(' ')))
                        # print(array_time)
        except FileNotFoundError:
            print('File graph.cfg not found')
        point1 = 0
        point2 = 0
        point3 = -1
        point4 = -1
        point1_time = 0
        point2_time = 0
        point3_time = -1
        point4_time = -1
        for i in range(len(array)):
            if i < len(array) - 1:
                if array[i] <= current_val <= array[i + 1]:
                    point1 = array[i]
                    point2 = array[i + 1]
                    temp_list = str(array_time[i]).split('.')
                    point1_time = int(temp_list[0]) * 60 + int(temp_list[1])
                    temp_list = str(array_time[i + 1]).split('.')
                    point2_time = int(temp_list[0]) * 60 + int(temp_list[1])
        for i in reversed(range(len(array))):
            if i > 0:
                if array[i] <= current_val <= array[i - 1]:
                    point3 = array[i]
                    point4 = array[i - 1]
                    temp_list = str(array_time[i]).split('.')
                    point3_time = int(temp_list[0]) * 60 + int(temp_list[1])
                    temp_list = str(array_time[i - 1]).split('.')
                    point4_time = int(temp_list[0]) * 60 + int(temp_list[1])
        if point1 == point4 and point2 == point3:
            return [[point1, point2, -1, -1], [point1_time, point2_time, -1, -1]]
        else:
            return [[point1, point2, point3, point4], [point1_time, point2_time, point3_time, point4_time]]
        return False

    def is_temp_changes(self):
        if self.temperature_memory:
            if abs(self.temperature_memory[-1] - self.temperature_memory[0]) > 10:
                return True
            else:
                return False


if __name__ == "__main__":
    analyz = Analyzer()
    act_temperature = 290
    # print(analyz.find_points('graph.cfg', 2, 156))
    while True:
        act_temperature -= 1
        # print('Actual_temp = {}'.format(act_temperature))
        analyz.execute_analysis(2, act_temperature)
        time.sleep(1)

