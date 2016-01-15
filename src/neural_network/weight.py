import random


class Weight():
    def __init__(self, range_val):
        self.range_min = range_val[0]
        self.range_max = range_val[1]
        self.value = random.uniform(range_val[0], range_val[1])

    def recompute(self, learning_rate, expected, output, x_in):
        if x_in != 0 and x_in != []:
            for i in x_in:
                self.value += learning_rate * (expected - output) * i

    def get_value(self):
        return self.value
