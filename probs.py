#!/usr/bin/env python3
"""File with `Probs` class

Authors:
    Martin Bazik (xbazik00)
    Ondrej Kurak (xkurak00)
"""
import json
import numpy as np
from scipy.optimize import least_squares

class Probs():
    """Class for counting dead probablities

    Counts dead probabilities

    Args:
        data_file (str): Path to the data file
        max_y (int): Final year of simulation
    """

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
    def __model_down(val, x):
        return np.absolute(val[0] / (x**val[1] + val[2]))

    @staticmethod
    def __model_up(val, x):
        return np.absolute(val[0] + val[1] * x**val[2])

    def __func_down(self, val, x, y):
        return self.__model_down(val, x) - y

    def __func_up(self, val, x, y):
        return self.__model_up(val, x) - y

    def age_start(self):
        """Starting parameters
        Counts parameters for `__model_down` for every age category
        """
        x_o = np.array(self.data['years'][-12:])
        x = x_o / x_o.max()

        for part, name in zip(self.data['data'],
                              self.data['names']):
            if name == '0':
                continue

            y = np.array(part[-12:])
            y = y / 10**5

            x0 = np.array([1, 1, 1])

            self.ress.append(least_squares(self.__func_down,
                                           x0,
                                           args=(x, y)))

    def set_max_year(self, max_y):
        """Parameters for every year
        Count parameters for every year of simulation, so dead probability
        could be evaluated faster.

        Args:
            max_y (int): Final year of simulation
        """
        if max_y < self.max:
            return
        for year in range(self.max-1, max_y + 1):
            values = []
            for res in self.ress:
                val = self.__model_down(res.x, year / self.m_y)
                values += [val] * 5
            values += [values[-1]] * 5

            y = np.array(values)
            x = np.array(range(1, len(values) + 1))
            x0 = np.array([1, 1, 1])

            self.year_data[year] = least_squares(self.__func_up,
                                                 x0,
                                                 args=(x, y))

    def mort_rate(self, year, age):
        """Mortality ratio
        Returns and returns mortality ratio

        Args:
            year (int): Year
            age (int): Age
        
        Returns:
            (float): Mortality rate
        """
        if year not in self.year_data:
            return 0
        return self.__model_up(self.year_data[year].x, age)

    def death_prob(self, year, age):
        """Death probability
        Retuns death probability for age in year
        
        Args:
            year (int): Year
            age (int): Age

        Returns:
            (float): Death probability
        """
        return 1 - np.exp(-self.mort_rate(year, age))

    def max_age(self, year):
        """Maximum life span
        Returns maximal life span based on mortality rate

        Args:
            year (int): year
        
        Returns:
            (int): Maximum life span    
        """
        if year not in self.year_data:
            return 0

        x = self.year_data[year].x
        return round(np.power((1 - x[0])/x[1], 1/x[2]))
    