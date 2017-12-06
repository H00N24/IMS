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
je potrebne pripraviť virtualne prostredie s
kniznicami Numpy a Scipy. Postup pripravy a spustenia je:
1. Priravenie virtualneho prostredia
```
$ python3 -m venv ims-env
```
2. Nainstalovanie kniznic Numpy a Scipy
```
$ ims-env/bin/pip3 install scipy
```
3. Spustenie programu
```
$ ims-env/bin/python3 main.py
```
Pre zrychlenie je priraveny `Makefile`, ktory ma argumenty:
* `run` - spustenie programu (bez virtualneho prostredia)
* `run_env` - spustenie vo virtualnom prostredi
* `install` - vytvorenie a nainstalovanie knizic do virtualneho prostredia
* `clean` - odstranenie virtualneho prostredia
