#!/usr/bin/python3

import argparse#, pprint

def parse_nmap(fd):
    rps = fd.split("Nmap scan report for ")[1:]
    res = {}
    for rp in rps:
        rpo = parse_rp(rp)
        res[rpo[0]] = rpo[1]
    return res

def parse_rp(rp):
    lines = rp.split("\n")
    # get ip
    ipl = lines[0]
    if "(" in ipl and ")" in ipl:
        ip = ipl.split("(")[1][:-1]
        hn = ipl.split(" (")[0]
        ip = (ip,hn)
    else:
        ip = (ipl)
    # get portlist
#    print(rp) #DEBUG
#    pl0 = rp.split(' filtered ports\n')[1]
#    pl0 = pl0.split('\n')[1:]
    pl0 = rp.split("\n")
    res = {}
    for ln in pl0:
        words = ln.split()
        if len(words) < 2:
            continue
        if not words[1] in ['open','closed','filtered']:
            continue
        pnum = words[0].split("/")[0]
        ptype = words[0].split("/")[1]
        pstate = words[1]
        if len(words) == 2:
            pservice = ''
            pver = ''
        else:
            pservice = words[2]
            if len(words) == 3:
                pver = ''
            else:
                pver = ' '.join(words[3:])
        res[pnum] = {'type':ptype,'state':pstate,'service':pservice,'version':pver}
    return ip[0], {'ip':ip,'ports':res}

def pretty_output(json):
    n = 0
    for i in json:
        if n == 0:
            n += 1
        else:
            print('\n')
        print(' '.join(json[i]['ip'])+":") if len(json[i]['ip']) == 2 else print(json[i]['ip']+":")
        for port in json[i]['ports']:
            print('\t%s : %s %s %s' % (
                port,
                json[i]['ports'][port]['type'],
                json[i]['ports'][port]['service'],
                json[i]['ports'][port]['version']))

def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument(
        "FILE",
        help=("File to parse in nmap regular output format"))
    p.add_argument(
        "-p","--pretty",
        help=("Print pretty output"),
        action="store_true")
    return p.parse_args()
def main(args):
    try:
        fd = open(args.FILE,"r").read()
    except Exception as e:
        print("[!] Fatal error:",e)
        exit(1)
    res = parse_nmap(fd)
    if not args.pretty:
        print(res)
    else:
        pretty_output(res)#pprint.pprint(res)
main(parse_args()) if __name__ == "__main__" else None




