#!/data/data/com.termux/files/usr/bin/python
from getpass import getpass
import requests
import argparse

url = "https://stonks.marcusj.tech/admin/bal"

def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument(
        "-u",'--user',
        required=True,
        help="User's balance to modify"
    )
    p.add_argument(
        "-b","--balance",
        required=False,
        help="Set balance"
    )
    args = p.parse_args()
    if args.balance and not args.balance.isnumeric():
        p.errot("Balance must be an integer")
    return args

def main(args):
    d = {
        "password": getpass(),
        "username": args.user,
    }
    if args.balance:
        d["balance"] = int(args.balance)
    r = requests.post(url, data=d)
    print(r.status_code, r.text)

if __name__ == "__main__":
    main(parse_args())
