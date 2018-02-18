# -*- coding: utf-8 -*- 
#!/usr/bin/env python
'''
Student name: Beier (Benjamin) Liu
Date: 2/18/2018
Exercise 4.2.1 to 4.2.4

Remark:
Python 2.7 is recommended
Before running please install packages *numpy
Using cmd line py -2.7 -m install [package_name]
'''
import os, time, logging
import copy, math
import functools, itertools
import numpy as np 
from Implementations.Loan import *
from Implementations.Asset import *
from Implementations.Timer import *
from Implementations.Loans import *
from Implementations.Mortgages import *

'''===================================================================================================
Main program:
# Exercise 4.2.1
# Modify your Timer class to use a logging statement (info level) instead of a print statement

# Exercise 4.2.2
# Modify your Timer class as follows:
# a. Add a class-level warnThreshold variable, which defaults to 1 minute.
# b. When printing the time taken, use a warn-level log statement instead of info-level if the 
# time taken exceeds the warn threshold

# Exercise 4.2.3
# Add logging statements to your Loan class. This should consist of the following:
# a. Anytime an exception is thrown (i.e., when an incorrect Asset type is passed-into the initialization 
# function), log an error prior to raising the exception.
# b. Debug-level logs which display interim steps of calculations and return values for the Loan functions
# c. Info-level logs to display things like ‘t is greater than term’ in the loan functions
# d. At the point the exception is caught (in your main function) use logging.exception to display the 
# exception in addition to a custom message
# e. Add a warn log to the recursive versions of the waterfall functions (that they are expected to 
# take a long time, so the explicit versions are recommended)

# Exercise 4.2.4
# Play around with your Loan and Timer classes to trigger logging statements. Switch logging levels 
# in your main code to demonstrate how to turn on/off different levels of logging

Implementations:
See implementations in Implementations\Timer.py, Loan.py
==================================================================================================='''

def main():
	# Exercise 4.2.4
	print('\n====================================Exercise 4.2.4=====================================\n');
	print('\n======================Switching my logging level to DEBUG ...========================== \n');
	logging.getLogger().setLevel(logging.DEBUG)
	myDemo();
	raw_input('Program pause. Press enter to continue.\n');

	print('\n=====================Switching my logging level to INFO ...============================ \n');
	logging.getLogger().setLevel(logging.INFO)
	myDemo();
	raw_input('Program pause. Press enter to continue.\n');

	print('\n=====================Switching my logging level to WARNING ...========================= \n');
	logging.getLogger().setLevel(logging.WARNING)
	myDemo();
	raw_input('Program pause. Press enter to continue.\n');

	print('\n=====================Switching my logging level to ERROR ...=========================== \n');
	logging.getLogger().setLevel(logging.ERROR)
	myDemo();
	raw_input('Program pause. Press enter to continue.\n');

	print('\n=====================Switching my logging level to CRITICAL ...======================== \n');
	logging.getLogger().setLevel(logging.CRITICAL)
	myDemo();
	raw_input('Program pause. Press enter to continue.\n');


def myDemo():
	home=PrimaryHome(1000000);
	dummy=FixedMortgage(None, 1000000, .05, 12); # should logging
	loan=FixedMortgage(home, 1000000, .05, 12);
	loan.balanceRecur(13); # should logging
	loan.balanceRecur(3); # should logging
	with Timer('my timer') as t:
		ntime.sleep(61);
		# pass

if __name__=='__main__':
	main()