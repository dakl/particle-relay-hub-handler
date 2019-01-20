run:
	watchmedo auto-restart python run.py --patterns="*.py" --recursive

unit-test:
	pytest -s .

lint:
	flake8 app/
	mypy --ignore-missing-imports app/

test: unit-test lint

build:
	docker build -t dakl/particle-relay-hub-api .

push:
	docker push dakl/particle-relay-hub-api