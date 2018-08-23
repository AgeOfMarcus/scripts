#!/usr/bin/python3

from sys import argv
import hashlib

def sha256(string): return hashlib.sha256(string.encode()).hexdigest()

if __name__ == "__main__":
	if len(argv) == 1:
		while True:
			txt = input("sha256 > ")
			print(sha256(txt))
	else:
		print(sha256(argv[1]))
