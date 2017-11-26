from age import Age
from probs import Probs
import numpy as np

class Controler():

    def __init__(self, data_file, max_year):
        self.prob = Probs(data_file, max_year)
        self.clr = []
        for i in range(1, 118):
            self.clr.append(Age(i, 2016, self.prob))
        
        self.num_of_people()
        self.resovle_year()

    def resovle_year(self):
        tmp = None
        for i in self.clr[::-1]:
            ppl_s_h, ppl_s_nh = i.resolve_year()
            if tmp:
                tmp.ppl_s_h = ppl_s_h
                tmp.ppl_s_nh = ppl_s_nh
            tmp = i
        self.clr[0].ppl_s_h = np.random.exponential(11000)
 
    def num_of_people(self):
        age = 0
        res = []
        for y in self.prob.data['ppl'][:-1]:
            res += self.div(y, age, 5)
            age += 5

        res += self.div(self.prob.data['ppl'][-1], 95, len(self.clr)-94)
        for age_block, ppl in zip(self.clr, res):
            age_block.ppl_h = ppl

    def div(self, y, age, num):
        res = 1
        for i in range(age + num , age + 1, -1):
            tmp = 1 - self.prob.dead_prob(2016, i)
            res = 1 + tmp * res

        fld = [y/res]
        for i in range(age + 2, age + num + 1):
            fld.append(fld[-1] * (1 - self.prob.dead_prob(2016, i)))

        return fld
        
