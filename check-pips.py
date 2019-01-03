#!/usr/bin/python3
'''req pyver in $PATH'''
from subprocess import Popen, PIPE
import os, sys

sh = lambda cmd: Popen(cmd, stdout=PIPE, shell=True).communicate()[0]


td = []
errs = []
for pkg in sh("pip3 freeze").strip().decode().split("\n"):
	try:
		name = pkg.split("==")[0]
		r = sh("pyver %s" % name).strip().decode().split("\n")
		lv = r[0].split(": ")[1]
		gv = r[1].split(": ")[1]
		if gv > lv:
			td.append(name)
	except Exception as e:
		errs.append([name,e])

print(' '.join(td))
if sys.argv[-1] == "-v":
	print("\n\n",errs)