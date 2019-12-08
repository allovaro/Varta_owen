

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
        if new_value == self.get_last_value():
            if len(self.temperature_memory) < 15:
                self.temperature_memory.append(new_value)
            else:
                self.temperature_memory.pop(0)
                self.temperature_memory.append(new_value)
        # print(len(self.temperature_memory))

    def get_last_value(self):
        return self.temperature_memory[-1]
