#!/usr/bin/env bash
# https://dzone.com/articles/executable-package-pip-install
python setup.py bdist_wheel
wheel_file=$(ls dist)
pip install "dist/$wheel_file"
#python -m twine upload $wheel_file
#pip uninstall superpro
#pip install superpro