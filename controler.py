from age import Age
from probs import Probs

class Controler():

    def __init__(self, data_file, max_year):
        self.prob = Probs(data_file, max_year)
        self.clr = []
        for i in range(1, 118):
            self.clr.append(Age(i, 2016, self.prob))
        

    def num_of_people(self):
        pass
