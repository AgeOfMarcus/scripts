#!/usr/bin/python3

from Crypto.PublicKey import RSA
import os, fire, base64

class RSACrypt(object):
	help = '''
	rsacrypt encrypts and decrypts files with an RSA public/private key.
	(encrypt also encodes with base64)
	(decrypt needs a file encrypted with the same method as this encrypt)
	'''
	def encrypt(self, key, file):
		try:
			key = RSA.importKey(open(key,"rb").read())
		except Exception as e:
			print("[!] Error importing key:\n"+str(e))
			return None
		try:
			filedata = open(file,"rb").read()
		except Exception as e:
			print("[!] Error reading target file:\n"+str(e))
			return None
		if 'publickey' in dir(key):
			key = key.publickey()
		enc = base64.b64encode(key.encrypt(filedata,1024)[0])
		try:
			with open("encrypted."+file,"wb") as f:
				f.write(enc)
		except Exception as e:
			print("Error writing encrypted data to file:\n"+str(e))
			return None
	def decrypt(self, key, file):
		try:
			key = RSA.importKey(open(key,"rb").read())
		except Exception as e:
			print("[!] Error importing key:\n"+str(e))
			return None
		try:
			filedata = open(file,"rb").read()
		except Exception as e:
			print("[!] Error reading target file:\n"+str(e))
			return None
		if not 'publickey' in dir(key):
			print("[!] Key is not a private key")
			return None
		try:
			enc = base64.b64decode(filedata)
		except Exception as e:
			print("[!] Error base64 decoding filedata:\n"+str(e))
			return None
		try:
			dec = key.decrypt(enc)
		except Exception as e:
			print("[!] Error decrypting data:\n"+str(e))
			return None
		try:
			with open("decrypted."+file,"wb") as f:
				f.write(dec)
		except Exception as e:
			print("[!] Error writing decrypted data:\n"+str(e))
			return None
	def generate(self, leng=4096):
		key = RSA.generate(leng,os.urandom)
		print(key.exportKey().decode())

if __name__ == "__main__":
	fire.Fire(RSACrypt)