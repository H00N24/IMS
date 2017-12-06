default: run

run:
	python3 main.py

run_env: install
	ims-env/bin/python3 main.py

install:
	python3 -m venv ims-env
	ims-env/bin/pip3 install scipy

pack:
	git archive -v --format=zip HEAD >05_xbazik00_xkurak00.zip

clean:
	rm -rf ims-env