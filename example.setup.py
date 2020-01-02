import setuptools
import os

def read(fname):
	return open(os.path.join(os.path.dirname(__file__), fname)).read()

setuptools.setup(name='library',
	version='0.0.0',
	description='calm g snm',
	long_description=read("README.md"),
	url='https://github.com/user/repo',
	author='Your Name',
	author_email='your@email.com',
	license='GPL',
	packages=setuptools.find_packages(),
	zip_safe=False,
	install_requires=[
		
	])
