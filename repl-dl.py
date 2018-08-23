#!/usr/bin/python3

import os
from sys import argv

try:
	repo = argv[1]
except:
	print("Argument neede: repo")
	exit(0)

url = "https://repl.it/@%s.zip" % repo
name = repo.split("/")[1]

os.system("mkdir "+name)
os.chdir(name)
os.system("wget "+url)
os.system("unzip %s.zip" % name)
os.system("rm %s.zip" % name)
os.system("mv ./main.py ./%s.py" % name.lower())
os.system("cd ..")
