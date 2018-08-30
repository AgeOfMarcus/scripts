#!/usr/bin/python3

'''
A tool to set and remove proxy settings for your terminal
'''

import fire, os

class SetProxy(object):
	help = '''
	Usage:
		set http://server:port
		remove
	'''
	def set(self, server):
		os.system('export http_proxy="http://%s"' % server)
		os.system('export https_proxy="https://%s"' % server)
		os.system('export ftp_proxy="http://%s"' % server)
	def remove(self):
		os.system("unset http_proxy; unset https_proxy; unset ftp_proxy")

if __name__ == "__main__":
	fire.Fire(SetProxy)
