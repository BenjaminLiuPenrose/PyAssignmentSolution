# -*- coding: utf-8 -*- 
#!/usr/bin/env python
'''
Student name: Beier (Benjamin) Liu
Date:
Exercise 4.1.5

Remark:
Python 2.7 is recommended
'''
from Implementations.Timer import *
import time 

'''===================================================================================================
Main program:
# This is a demo for Exercise 4.1.5
# Convert your Timer class’ print statement to use format flags or the format function, instead of concatenating strings

Implementations:
See file 4.1_Solution\Implementations\Timer.py
==================================================================================================='''

def main():
	# Exercise 4.1.5
	# Add a start method and end method
	print('\n====================================Exercise 4.1.5=====================================\n');
	print('Using start and end method ... \n');
	ta=Timer();
	ta.start();
	time.sleep(5);
	ta.end();
	raw_input('Program pause. Press enter to continue.\n');

	# Showing the ability to configure the Timer to display either seconds, minutes, or hours
	print('Running my display function ... \n');
	print('Displaying seconds only: \n');
	td=ta;
	td.display('seconds');
	print('Displaying minites only: \n');
	td.display('minutes');
	print('Displaying hours only: \n');
	td.display('hours');
	print('Displaying seconds, minutes and hours: \n');
	td.display('seconds','minutes','hours');
	raw_input('Program pause. Press enter to continue.\n');

	# Method to retrieve the last timer result
	te=Timer();
	te.start();
	time.sleep(20);
	te.end(); te.start();
	time.sleep(5);
	te.end();
	print('Running my retrieve function ... \n');
	print('Retriving the current data: \n');
	print(te.retrieve(0)); print('');
	print('Retriving the previous one data: \n');
	print(te.retrieve(1)); print('');
	raw_input('Timer demo is successfully finished. Press any key to exit. \n');

if __name__=='__main__':
	main()

