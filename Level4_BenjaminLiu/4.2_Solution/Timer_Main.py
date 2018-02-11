# -*- coding: utf-8 -*- 
#!/usr/bin/env python
'''
Student name: Beier (Benjamin) Liu
Date:
Exercise 4.2.1 to 4.2.2

Remark:
Python 2.7 is recommended
'''
from Implementations.Timer import *
import time 
import logging
logging.getLogger().setLevel(logging.DEBUG)

'''===================================================================================================
Main program:
# This is a demo for Exercise 4.2.1 and 4.2.2
# Exercise 4.2.1 
# Modify your Timer class to use a logging statement (info level) instead of a logging.info statement
# Exercise 4.2.2 
# Modify your Timer class as follows:
# a. Add a class-level warnThreshold variable, which defaults to 1 minute.
# b. When logging.infoing the time taken, use a warn-level log statement instead of info-level 
# if the time taken exceeds the warn threshold

Implementations:
See file 4.1_Solution\Implementations\Timer.py
==================================================================================================='''

def main():
	# Exercise 4.1.1 and 4.1.2
	# Add a start method and end method
	logging.info('\n====================================Exercise 4.1.5=====================================\n');
	logging.info('Using start and end method ... \n');
	ta=Timer();
	ta.start();
	time.sleep(5);
	ta.end();
	raw_input('Program pause. Press enter to continue.\n');

	# Showing the ability to configure the Timer to display either seconds, minutes, or hours
	logging.info('Running my display function ... \n');
	logging.info('Displaying seconds only: \n');
	td=ta;
	td.display('seconds');
	logging.info('Displaying minites only: \n');
	td.display('minutes');
	logging.info('Displaying hours only: \n');
	td.display('hours');
	logging.info('Displaying seconds, minutes and hours: \n');
	td.display('seconds','minutes','hours');
	raw_input('Program pause. Press enter to continue.\n');

	# Method to retrieve the last timer result
	te=Timer();
	te.start();
	time.sleep(5);
	te.end(); # will log info
	te.start();
	time.sleep(90);
	te.end(); # will log warning 
	logging.info('Running my retrieve function ... \n');
	logging.info('Retriving the current data: \n');
	logging.info(te.retrieve(0)); logging.info('');
	logging.info('Retriving the previous one data: \n');
	logging.info(te.retrieve(1)); logging.info('');
	raw_input('Timer demo is successfully finished. Press any key to exit. \n');

if __name__=='__main__':
	main()

