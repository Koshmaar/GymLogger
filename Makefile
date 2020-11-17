.PHONY: install run lint test

install:
	pip install -e .

run:
	python main_test_max.py

lint:
	mypy main_test_max.py

test:
	cd gym/tests/ && python3 -m pytest .