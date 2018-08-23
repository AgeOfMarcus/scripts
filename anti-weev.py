#!/usr/bin/env python
import sys
import base64

try:
    sys.argv[1]
except Exception:
    print "[*] ./anti-weev.py filename.php"
    sys.exit()
else:
    print "[*] Anti-Weevely ~ v0.1 for Weevely v1.1"
   
try:
    # Saving File contents
    poisoned_lines = []
    poisoned_f = open(sys.argv[1], "r")
    for line in poisoned_f:
        poisoned_lines.append(line)
    poisoned_f.close()
except IOError:
    print "[-] This doesn't seem like a file"
    sys.exit()
    
try:
    # Find Variables which are part of the encoded line
    for i in poisoned_lines:
        if "." in i:
            full_line = i
            poisoned_lines.remove(i)
            base64_line = ((i.split('"", ')[1]).split(")")[0]).split(".")
            break
    to_replace = (full_line.split("$")[4]).split('"')[1]
    # Recreating injected base64 line
    base_64_string = ""
    for item in base64_line:
        for p in poisoned_lines:
            if item in p:
                base_64_string += str(p[p.find("=")+1:])
    # Cleaning Up the String
    base_64_string = base_64_string.replace('"', '')
    base_64_string = base_64_string.replace(';', '')
    base_64_string = base_64_string.replace('\n', '')
    base_64_string = base_64_string.replace(' ', '')
    base_64_string = base_64_string.replace(to_replace, '')
    # Decoding with base64 and parsing in order to find the keys
    final = base64.b64decode(base_64_string)
    start_key = final.split("reset($a)=='")[1][0:2]
    end_key = (final.split("{$k='")[1]).split("';echo")[0]
    print "[+] Discovered Password: %s%s" % (start_key, end_key)
    sys.exit("[*] Shutting down...")
except IndexError:
    print "[*] This doesn't seem like a weevely php backdoor"
except Exception, error:
    print "[-] An error occured: %s" % (error)