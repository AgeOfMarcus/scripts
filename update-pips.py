import os

for package in os.popen("pip3 freeze"):
	os.system("pip3 install --upgrade %s --user" % package.split("==")[0])
