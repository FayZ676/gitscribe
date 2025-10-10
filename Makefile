install:
	python -m venv .venv
	source .venv/bin/activate && pip install -r requirements.txt

build_binary:
	pyinstaller --onefile --name commit2content cli.py

test_binary:
	./dist/commit2content commit2content

install_binary:
	sudo cp dist/commit2content /usr/local/bin/
	sudo chmod +x /usr/local/bin/commit2content

uninstall_binary:
	sudo rm -f /usr/local/bin/commit2content