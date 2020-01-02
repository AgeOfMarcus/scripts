#!/usr/bin/python3

import os

os.system("python3 setup.py bdist_wheel")
os.system("python3 -m twine upload dist/*")
os.system("rm -rf build dist *.egg_info")