SHELL := /bin/bash

build:

	python setup.py bdist_wheel
	wheel_file="dist/$(ls dist | tail -1)"
	python -m twine upload $wheel_file

install:

	pip uninstall superpro
	sleep 2
	pip install superpro

make:
	install
	build
