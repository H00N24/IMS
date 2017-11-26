#!/usr/bin/env python3

from controler import Controler

controler = Controler('new_data.json', 2050)

s = 0
for i in range(1, 117):
    a = controler.prob.dead_prob(2016, i)
    s += a
    #print(a)

print(s)


while controler.clr[0].year != 2050:
    a = 0
    for i in controler.clr[65:]:
        a += i.alive()
    print(a)
    controler.resovle_year()
