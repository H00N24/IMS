# IMS
Modelovanie domova dochodcov

## Autori
* Martin Bazik (xbazik00)
* Ondrej Kurak (xkurak00)

## Potrebne 
* Python 3.x
* Numpy (http://www.numpy.org/)
* Scipy (https://www.scipy.org/)
* **Volitelne** (pre spustenie `ims.ipynb`)
    * jupyter (http://jupyter.org/)
    * matplotlib (https://matplotlib.org/)


## Spustenie na serveri merlin
Pre spustenie programu na serveri merlin,
je potrebné pripraviť virtuálne prostredie s
knižnicami Numpy a Scipy. Postup prípravy a spustenia je:
1. Pripravenie virtuálneho prostredia
```
$ python3 -m venv ims-env
```
2. Nainštalovanie knižníc Numpy a Scipy
```
$ ims-env/bin/pip3 install scipy
```
3. Spustenie programu
```
$ ims-env/bin/python3 main.py
```
Pre zrýchlenie je pripravený `Makefile`, ktorý má argumenty:
* `run` - spustenie programu (bez virtuálneho prostredia)
* `run_env` - spustenie vo virtuálnom prostredí
* `install` - vytvorenie a nainštalovanie knižníc do virtuálneho prostredia
* `clean` - odstránenie virtuálneho prostredia
