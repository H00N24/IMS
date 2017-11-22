import numpy as np
from scipy.optimize import least_squares
import json


class Probs():

    def __init__(self, data_file, max_y):
        with open(data_file, 'r') as inp:
            self.data = json.load(inp)

        self.ress = []
        self.age_start()

        self.year_data = {}
        self.m_y = max(self.data['years'])
        self.max = self.m_y
        self.set_max_year(max_y)

    @staticmethod
    def model_down(val, x):
        return  val[0] / (x**val[1] + val[2])
    
    @staticmethod
    def model_up(val, x):
        return val[0] + val[1] * x**val[2]

    def func_down(self, val, x, y):
        return self.model_down(val, x) - y
    
    def func_up(self, val, x, y):
        return self.model_up(val, x) - y

    def age_start(self):
        x_o = np.array(self.data['years'][-12:])
        x = x_o / x_o.max()

        for part, name in zip(self.data['data'],
                              self.data['names']):
            if name == '0':
                continue

            y = np.array(part[-12:])
            y = y / 10**5

            x0 = np.array([1, 1, 1])

            self.ress.append(least_squares(self.func_down,
                                           x0,
                                           args=(x, y)))

    def set_max_year(self, max_y):
        if max_y < self.max:
            return
        for year in range(self.max-1, max_y + 1):
            values = []
            for res in self.ress:
                val = self.model_down(res.x, year / self.m_y)
                values += [val] * 5
            values += [values[-1]] * 5

            y = np.array(values)
            x = np.array(range(1, len(values) + 1))
            x0 = np.array([1, 1, 1])

            self.year_data[year] = least_squares(self.func_up,
                                                 x0,
                                                 args=(x, y))

    def dead_prob(self, year, age):
        if year not in self.year_data:
            return 0
        if age > 116:
            return 1

        return self.model_up(self.year_data[year].x, age)

    def max_age(self, year):
        if year not in self.year_data:
            return 0

        x = self.year_data[year].x
        return np.power((1 - x[0])/x[1], 1/x[2])

    def nursing_house_prob(self, year, age):
        # TODO
        if age < 64:
            return 0

        return 0.02

    