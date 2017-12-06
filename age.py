#!/usr/bin/env python3
"""File containing `Age` class

Authors:
    Martin Bazik (xbazik00)
    Ondrej Kurak (xkurak00)
"""
import numpy as np

class Age():
    """Class for storing age data
    Stores data for age block

    Args:
        age (int): Age for which data are stored
        year (int): Starting year of simulation
        prob (:obj: `Probs`): `Probs` class for counting death propability
    """
    def __init__(self, age, year, prob):
        self.age = age
        self.year = year
        self.prob = prob
        self.ppl_s_h = 0
        self.ppl_h = 0
        self.ppl_d = 0
        self.d_prob = 0

    def alive(self):
        """People alive
        Returns how many people are alive

        Returns:
            int: Number of living people
        """
        return self.ppl_h

    def dead(self):
        """People dead
        Returns how many people are dead

        Returns:
            int: Number of dead people
        """
        return self.ppl_d

    def resolve_year(self):
        """Resolve year

        Sets number of people based on death probability

        Returns:
            int: Number of living people
        """
        if self.ppl_s_h != 0:
            self.ppl_h = 0
            self.ppl_d = 0

            self.d_prob = self.prob.death_prob(self.year, self.age)

            for _ in range(int(self.ppl_s_h)):
                if np.random.random() <= self.d_prob:
                    self.ppl_d += 1

            self.ppl_h = self.ppl_s_h - self.ppl_d

            self.ppl_s_h = 0
            self.year += 1

        return self.ppl_h
