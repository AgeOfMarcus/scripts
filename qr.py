#!/usr/bin/python3
import qrcode
from sys import argv
txt = ' '.join(argv[1:])
qr = qrcode.QRCode()
qr.add_data(txt)
qr.print_ascii()