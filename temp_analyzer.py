

class Analyzer(object):
    temperature_direction = None
    temperature_average = 0
    temperature_memory = []

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
            if new_value == self.get_last_value():
                if len(self.temperature_memory) < 15:
                    self.temperature_memory.append(new_value)
                else:
                    self.temperature_memory.pop(0)
                    self.temperature_memory.append(new_value)
        else:
            self.temperature_memory.append(new_value)
        # print(len(self.temperature_memory))

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


analyz = Analyzer()
print(analyz.find_points('graph.cfg', 3, 20))

