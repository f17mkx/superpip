#!/usr/bin/env bash
# https://dzone.com/articles/executable-package-pip-install
#version="0.3"
#python setup.py bdist_wheel "$version"
python setup.py bdist_wheel
wheel_file="dist/$(ls dist | tail -1)"
echo $wheel_file
#wheel_file="$PWD/dist/superpro-$version-py3-none-any.whl"



sleep 2
python -m twine upload $wheel_file
sleep 2
pip uninstall superpro
sleep 2
# https://pypi.org/project/superpro/
pip install superpro
#pip install "dist/$wheel_file"
