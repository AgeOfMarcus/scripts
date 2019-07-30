#!/usr/bin/python3

from Crypto.PublicKey import RSA
from tqdm import tqdm
import random

def getdata(n=2048):
	MOUSE = open("/dev/input/mice","rb")
	d = b''
	for i in tqdm(range(n)):
		d += MOUSE.read(1)
	MOUSE.close()
	return d[:n]

def makekey(dat, keylen=1024, n=2048):
	def rf(n):
		d = b''
		while len(d) < n:
			d += bytes([random.choice(list(dat))])
		return d
	k = RSA.generate(keylen, randfunc=rf)
	return k

def main():
	k = makekey(getdata())
	print(k.exportKey().decode())
main() if __name__ == "__main__" else None
