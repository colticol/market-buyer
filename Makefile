init:
	pip install -r requirements.txt

test:
	python3 -m unittest

run:
	python3 -m buyer.main
