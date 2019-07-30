#!/usr/bin/python

import winrm, argparse, getpass

def p_a():
	p = argparse.ArgumentParser()
	p.add_argument(
		'-i','--ip',
		help=("IP to connect to"),
		required=True)
	p.add_argument(
		'-u','--username',
		help=("Which username to use"),
		required=True)
	p.add_argument(
		'-p','--password',
		help=("Password for auth"),
		required=False)
	return p.parse_args(), p

def main():
	args, p = p_a()
	pwd = getpass.getpass() if not args.password else args.password
	try:
		s = winrm.Session(args.ip,auth=(args.username,pwd))
		s.run_cmd('dir')
		print('success')
	except winrm.exceptions.InvalidCredentialsError:
		print('failed')
main() if __name__ == "__main__" else None
