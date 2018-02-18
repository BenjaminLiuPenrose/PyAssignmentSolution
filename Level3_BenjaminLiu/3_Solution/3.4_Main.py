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
import time
from Implementations.Timer import *
logging.getLogger().setLevel(logging.DEBUG)

'''===================================================================================================
Main program:
# Exercise 3.4.1
# Open a file and write to it, using the with statement. Verify that the file has indeed been closed, 
# once the with statement exits (check the closed attribute on the file handle variable)

# Exercise 3.4.2
# Modify the Timer class to work as a context manager

Implementations:
Implementations are followed by the main() function
Implementations can be found at 3_Solution\Implementations\Timer.py
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

	# Exercise 3.4.2
	print('\n====================================Exercise 3.4.2=====================================\n');
	print('Running context manager with Timer class ... \n');
	with Timer('myTimer') as timer:
		#time.sleep(10);
		timer.configureTimerDisplay('hrs', 'mins');
	raw_input('Demo finished successfully. Press any key to exit.\n');

if __name__=='__main__':
	main()