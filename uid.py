#!/usr/bin/python3

import uuid, argparse

def parse_args():
	p = argparse.ArgumentParser()
	p.add_argument(
		"-l","--length",
		help=("Length of UID"),
		type=int)
	p.add_argument(
		"-s","--safe",
		help=("Alphanumeric only"),
		action="store_true")
	return p.parse_args()

uid = lambda: str(uuid.uuid4())
safe_uid = lambda: ''.join(uid().split("-"))

def main(args):
	leng = 36 if args.length is None else args.length
	func = uid if not args.safe else safe_uid
	
	res = ''
	while len(res) <= leng:
		res += func()
	print(res[:leng])
main(parse_args()) if __name__ == "__main__" else None
