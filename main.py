#!/usr/bin/env python3

from controler import Controler
import numpy as np

controler = Controler('new_data.json', 2050)

s = 0
for i in range(1, 117):
    a = controler.prob.dead_prob(2016, i)
    s += a
    #print(a)

print(s)

s = sum([x.ppl_nh for x in controler.clr])
print('start', s)
while controler.clr[0].year != 2050:
    nh = [0, 0, 0]
    a = 0
    dead = 0
    for i in controler.clr[65:75]:
        nh[0] += i.ppl_nh
        a += i.alive() * 0.002
        dead += i.ppl_d
    for i in controler.clr[75:85]:
        nh[1] += i.ppl_nh
        a += i.alive() * 0.017
        dead += i.ppl_d
    for i in controler.clr[85:]:
        nh[2] += i.ppl_nh
        a += i.alive() * 0.0758
        dead += i.ppl_d

    print(i.year, np.around(nh), round(sum(nh)))
    print(i.year, round(a), dead)
    controler.resovle_year()
