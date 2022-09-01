#!/usr/bin/env bash
# https://dzone.com/articles/executable-package-pip-install
version="0.4.2"
git add .
git commit -m "build version$version"
git push
gh release create $version --title "$version" --notes "**new functions**\n- printl\n- files_in_dir\n- files_in_dir_ending\n"

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
