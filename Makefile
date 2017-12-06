default: run

run:
	python3 main.py

run_env: install
	ims-env/bin/python3 main.py

install:
	python3 -m venv ims-env
	ims-env/bin/pip3 install scipy

clean:
	rm -rf ims-env