#!/usr/bin/python3

import fire, os

class Title(object):
	def set(self, title):
		os.system("PROMPT_COMMAND=\'echo -ne \"\\033]0;%s\\007\"\'" % title)

if __name__ == "__main__":
	fire.Fire(Title)
