#!/usr/bin/python3

from sys import argv
import os

try:
	msg = argv[1]
except:
	msg = "new commit"


os.system("git add ./*")
os.system("git commit -m '%s'" % msg)
os.system("git push origin master")

