#!/usr/bin/python3

import os, sys

#ssh -R 80:localhost:3000 serveo.net

try:
	port = int(sys.argv[1])
except:
	print("Argument needed: port")
	exit(0)
os.system("ssh -R 80:localhost:%s serveo.net" % str(port))
