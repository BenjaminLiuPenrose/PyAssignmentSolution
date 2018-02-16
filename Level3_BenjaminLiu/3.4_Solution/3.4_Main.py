# -*- coding: utf-8 -*- 
#!/usr/bin/env python
'''
Student name: Beier (Benjamin) Liu
Date:
Exercise 3.4.1

Remark:
Python 2.7 is recommended
Before running please install packages
Using cmd line py -2.7 -m install [package_name]
'''
import logging
logging.getLogger().setLevel(logging.DEBUG)

'''===================================================================================================
Main program:
Exercise 3.4.1
Open a file and write to it, using the with statement. Verify that the file has indeed been closed, 
once the with statement exits (check the closed attribute on the file handle variable)

Implementations:
Write comments
==================================================================================================='''

def main():
	# Exercise 3.4.1
	print('\n====================================Exercise 3.4.1=====================================\n');
	print('Running context manager demo ... \n');
	with open('randomfile.txt', 'w') as f:
		f.write('This is a demo file. \n');
		f.write('This is the second line. \n');
		f.write('This is the ending line. \n');
	if f.closed:
		logging.info('File is closed. \n');
	raw_input('Program pause. Press enter to continue.\n');

if __name__=='__main__':
	main()