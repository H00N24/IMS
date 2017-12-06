#!/usr/bin/env python3
"""File containing `Controller` class

Authors:
    Martin Bazik (xbazik00)
    Ondrej Kurak (xkurak00)
"""

from age import Age
from probs import Probs
import numpy as np

class Controller():
    """Controller class
    Class for controlling a simulation

    Agrs:
        data_file (str): Path to a JSON data file
        max_year (int): Final year of a simulation

    Attributes:
        prob (:obj: `Probs`): `Probs` for calculating the death probabillity 
        clr (list(:obj: `Age`)): List of `Age` for storing the data of age groups
    """

    def __init__(self, data_file, max_year):
        self.prob = Probs(data_file, max_year)
        self.clr = []
        for i in range(1, 118):
            self.clr.append(Age(i, 2016, self.prob))

        self.__num_of_people()
        self.resolve_year()

    def resolve_year(self):
        """Resolve year method
        Resolves an actual year for every `Age` in `clr`,
        sets new starting values for each `Age`
        """
        tmp = None
        for i in self.clr[::-1]:
            ppl_s_h = i.resolve_year()
            if tmp:
                tmp.ppl_s_h = ppl_s_h
            tmp = i
        self.clr[0].ppl_s_h = np.random.exponential(12000)

    def __num_of_people(self):
        """Initial number of people
        Sets initial number of people for each `Age` in `clr` based
        on `__div` function
        """
        age = 0
        res = []
        for y in self.prob.data['ppl'][:-1]:
            res += self.__div(y, age, 5)
            age += 5

        res += self.__div(self.prob.data['ppl'][-1], 95, len(self.clr)-94)

        for age_block, ppl in zip(self.clr, res):
            age_block.ppl_h = round(ppl)

    def __div(self, y, age, num):
        """Divide group of people
        Divides group of people into subcategories based on mortality rate
        """
        res = 1
        for i in range(age + num, age + 1, -1):
            tmp = 1 - self.prob.mort_rate(2016, i)
            res = 1 + tmp * res

        fld = [y/res]
        for i in range(age + 2, age + num + 1):
            fld.append(fld[-1] * (1 - self.prob.mort_rate(2016, i)))

        return fld
