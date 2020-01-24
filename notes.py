#!/usr/bin/python3
import requests, os
from tempfile import mkstemp as tempfile

prog = requests.get("https://notes.marcusweinberger.repl.co").content
fd, fn = tempfile()

with os.fdopen(fd, "wb") as f:
	f.write(prog)

os.system("python3 " + fn)
os.remove(fn)
