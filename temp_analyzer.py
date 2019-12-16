import datetime as dt

class Analyzer(object):
    temperature_direction = 'ODD'
    in_range = False
    temperature_average = 0
    temperature_memory = []
    prev_temp = 0
    prev_time = 0
    next_temp = 0
    next_time = 0
    big_difference = False
    delta_val = 3
    start_timer = None
    # def __init__(self):
    #     # self.temperature_memory = self.init_list()

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
        try:
            with open(file_name, 'r') as file:
                for i in range(owen_num * 2 - 1):
                    line = file.readline()
                if line:
                    array = list(map(float, line.split(' ')))
        except FileNotFoundError:
            print('File graph.cfg not found')
        point1 = 0
        point2 = 0
        point3 = -1
        point4 = -1
        for i in range(len(array)):
            if i < len(array) - 1:
                if array[i] <= current_val <= array[i + 1]:
                    point1 = array[i]
                    point2 = array[i + 1]
        for i in reversed(range(len(array))):
            if i > 0:
                if array[i] <= current_val <= array[i - 1]:
                    point3 = array[i]
                    point4 = array[i - 1]
        if point1 == point4 and point2 == point3:
            return point1, point2, -1, -1
        else:
            return point1, point2, point3, point4
        return False

    def is_temp_changes(self):
        if self.temperature_memory:
            if abs(self.temperature_memory[-1] - self.temperature_memory[0]) > 10:
                return True
            else:
                return False


# analyz = Analyzer()
# analyz.prev_temp = 450
# analyz.next_temp = 300
# analyz.prev_time = dt.datetime.today() - dt.timedelta(hours=1)
# analyz.next_time = dt.datetime.today() + dt.timedelta(hours=5)
# print(analyz.get_prediction())

# print(dt.datetime.today())
# print(analyz.calc_next_timestamp('1.0', '2.0', dt.datetime.today()))
# my_val = analyz.calc_next_timestamp('1.0', '2.0', dt.datetime.today())
# print(dt.datetime.today().timestamp())
# print(dt.datetime(2017, 6, 11, 0, 0).timestamp())
# print(dt.datetime(my_val.year, my_val.month, my_val.day, my_val.hour, my_val.minute, my_val.second).timestamp())

