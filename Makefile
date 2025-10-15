install:
	python -m venv .venv
	source .venv/bin/activate && pip install -r requirements.txt

# Testing

test_content:
	python -m src.cli content --last=5

test_message:
	python -m src.cli message

test_all: test_content test_message

# Hooks

install_hook:
	cp hooks/pre-push .git/hooks/pre-push
	chmod +x .git/hooks/pre-push

uninstall_hook:
	rm -f .git/hooks/pre-push

# Binary Commands

build_binary:
	pyinstaller --onefile --name gitscribe src/cli.py

test_binary:
	./dist/gitscribe content --last 1
	./dist/gitscribe message

install_binary:
	sudo cp dist/gitscribe /usr/local/bin/
	sudo chmod +x /usr/local/bin/gitscribe 	

uninstall_binary:
	sudo rm -f /usr/local/bin/gitscribe