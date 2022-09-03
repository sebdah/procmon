phony: test
test:
	python -m unittest discover -s tests -p '*_test.py'
