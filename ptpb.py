#!/usr/bin/python3

from sys import argv
import os

try:
	fn = argv[1]
except:
	print("argument needed: filename")

if fn == "help":
	print("Usage: ptpb filename [urlname]")
	exit(0)

if len(argv) >= 3:
	un = "~"+argv[2]
else:
	un = ""
os.system("cat %s | curl -F c=@- https://ptpb.pw/%s" % (fn,un))
exit(0)
