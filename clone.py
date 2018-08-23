#!/usr/bin/python3

from sys import argv
import os

try:
	repo = argv[1]
except:
	print("Arg needed: repo (example/repo)")
	exit(0)

url = "https://github.com/"+repo
name = repo.split("/")[1].lower()

print("Cloning %s into ./%s" % (url, name))
os.system("git clone --recursive %s %s" % (url,name))
exit(0)
