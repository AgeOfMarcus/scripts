#!/usr/bin/python3

from sys import argv

try:
	filename = argv[1]
	with open(filename,"r") as f:
		text = f.read().split("\n")
except:
	text = input(">>> ")

print(len(text))
