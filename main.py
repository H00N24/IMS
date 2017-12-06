#!/usr/bin/env python3
"""Main.py

Authors:
    Martin Bazik (xbazik00)
    Ondrej Kurak (xkurak00)

Python version:
    Python 3.x

External libraries:
    numpy (http://www.numpy.org/)
    scipy (https://www.scipy.org/)

Run:
    $ python3 main.py

Virtual enviroment set-up and run:
    $ python3 -m venv ims-env
    $ ims-env/bin/pip3 install scipy
    $ ims-env/bin/python3 main.py
"""
import os
from controller import Controller

MAIN_DIR = os.path.dirname(os.path.abspath(__file__))
"""str: script directory"""
controller = Controller(MAIN_DIR + '/new_data.json', 2041)

print('==== Start ====')
print('Age', 'Number of people', 'Mortality rate', sep=';')
for age, cl in enumerate(controller.clr[30:], 30):
    if cl.alive() != 0:
        print(age, cl.alive(), controller.prob.mort_rate(2016, age), sep=';')
print()

exp_data = [[], [], []]
"""Stroring data for each experiment"""
exp_perc = [[0.001570500134, 0.002818625599, 0.01876894202, 0.0758],
            [0.001389275368, 0.001934861389, 0.01536942765, 0.1054],
            [0, 0.0, 0.0, 0.165]]
"""Percent of people in nursing houses for every age category"""

while controller.clr[0].year != 2041:
    """Storing data for each expretiment"""
    tmp = [[0, 0, 0, 0],
           [0, 0, 0, 0],
           [0, 0, 0, 0]]

    for index, part in enumerate([controller.clr[60:65],
                                  controller.clr[65:75],
                                  controller.clr[75:85],
                                  controller.clr[85:]]):
        for age_block in part:
            for tm, perc in zip(tmp, exp_perc):
                tm[index] += age_block.alive() * perc[index]

    for ex, tm in zip(exp_data, tmp):
        ex.append(tm)

    controller.resolve_year()

for num, exp in enumerate(exp_data, 1):
    """Printing data for each experiment in csv format (separator is ';')"""
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
