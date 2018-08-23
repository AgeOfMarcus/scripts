#!/usr/bin/python3

import os
from sys import argv

try:
	filename = argv[1]
	remotename = argv[2]
except:
	print("Expected argument(s): filename, remotefilename")
	exit(0)

cmd = "cat %s | curl -F c=@- https://ptpb.pw/%s" % (filename, remotename)
url = "https://ptpb.pw/%s" % remotename
os.system(cmd)
print("File uploaded to: "+url)
