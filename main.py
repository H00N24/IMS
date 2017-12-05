#!/usr/bin/env python3

from controler import Controler

controler = Controler('new_data.json', 2051)

print('==== Start ====')
print('Age', 'Number of people', sep=';')
for age, cl in enumerate(controler.clr):
    if cl.alive() != 0:
        print(age, cl.alive(), sep=';')
print()

exp_data = [[], [], []]
exp_perc = [[0.001570500134, 0.002818625599, 0.01876894202, 0.0758],
            [0.001570500134, 0.004098665455, 0.01876894202, 0.1055],
            [0, 0.0, 0.0, 0.165]]

while controler.clr[0].year != 2051:
    tmp = [[0, 0, 0, 0],
           [0, 0, 0, 0],
           [0, 0, 0, 0]]

    for index, part in enumerate([controler.clr[60:65],
                                  controler.clr[65:75],
                                  controler.clr[75:85],
                                  controler.clr[85:]]):
        for age_block in part:
            for tm, perc in zip(tmp, exp_perc):
                tm[index] += age_block.alive() * perc[index]

    for ex, tm in zip(exp_data, tmp):
        ex.append(tm)

    controler.resolve_year()

for num, exp in enumerate(exp_data, 1):
    print('==== Experiment {} ===='.format(num))
    print('60-64', '65-74', '75-84', '85+', 'all', sep=';')
    for year, data in enumerate(exp, 2016):
        print(year,
              round(data[0]),
              round(data[1]),
              round(data[2]),
              round(data[3]),
              round(sum(data)),
              sep=';')
    print()
