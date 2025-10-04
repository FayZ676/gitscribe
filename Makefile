install:
	python -m venv .venv
	source .venv/bin/activate && pip install -r requirements.txt

bundle:
	echo implement