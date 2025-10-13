install:
	python -m venv .venv
	source .venv/bin/activate && pip install -r requirements.txt

test:
	python cli.py content --style="style.txt"

# Binary Commands

build_binary:
	pyinstaller --onefile --name gitscribe cli.py

test_binary:
	./dist/gitscribe content --last 1

install_binary:
	sudo cp dist/gitscribe /usr/local/bin/
	sudo chmod +x /usr/local/bin/gitscribe

uninstall_binary:
	sudo rm -f /usr/local/bin/gitscribe