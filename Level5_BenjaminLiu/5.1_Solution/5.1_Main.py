# -*- coding: utf-8 -*- 
#!/usr/bin/env python
'''
Student name: Beier (Benjamin) Liu
Date:
Exercise 5.1.1

Remark:
Python 2.7 is recommended
Before running please install packages *numpy , *datetime
Using cmd line py -2.7 -m install [package_name]
'''
import os, time, logging
import copy, math
import functools, itertools
import numpy as np 
import datetime
logging.getLogger().setLevel(logging.DEBUG)

'''===================================================================================================
Main program:
# Exercise 5.1.1
# Create a program that does the following:
# a. Asks the user to input year, month, day, hour, minute, second, microsecond (one after another)
# b. Create a datetime variable with the entered info.
# c. Extract the datetime into year, month, day, hour, minutes, second, and microsecond. Display the 
# following result (where … is the extracted value):
# Year: …
# Month: …
# Day: …
# Hour: …
# Minute: …
# Second: …
# Microsecond: …
# d. Display the entered datetime with the following format: 2016-09-25 18:23:14:12342
# e. Display the entered datetime with the following format: 2016 September 25 06:24:14:12342 PM
# f. Do parts d-e with the current local time.
# g. Do parts d-e with the current UTC time

# Exercise 5.1.2
# Modify the above program to request the user enter the date in the following format (for example)

# Exercise 5.1.3
# Modify the above program to request the user enter the date in the following format (for example)

# Exercise 5.1.4
# Create a ‘date calculator’ program. It should do the following:
# a. Prompt the user to enter any date and time.
# b. Prompt the user to enter a delta time that is used to add or subtract from the original. 
# For example, if the user enters -00:25:13:0 then subtract 25 minutes and 13 seconds 
# (and zero microseconds). Another example: 72:12:00:154 means to add 72 hours, 12 minutes, 
# and 154 microseconds.
# c. Display the calculated resulting date and time, in an easily-readable format

# Exercise 5.1.5
# Create a ‘date differential’ program. It should do the following:
# a. Prompt the user to enter any date and time.
# b. Prompt the user to enter another date and time.
# c. Subtract the two datetimes and display the result to the user. It should be displayed in several 
# separate ways:
# i. Total number of days (including fractions of days).
# ii. Total number of hours (including fractions).
# iii. Total number of minutes (including fractions).
# iv. Total number of seconds (including fractions).
# v. Total number of microseconds (including fractions).
# vi. A complete (grammatically-correct) sentence that breaks everything down to the correct units and 
# excluding any 0s. For example

# Exercise 5.1.6
# Modify your Loan classes to take a loan start date and loan end (maturity) date instead of a term 
# parameter. Create a term method that calculates and returns the loan term (in months) from the two dates

Implementations:
Write comments
==================================================================================================='''

def main():
	# Exercise 5.1.1
	logging.info('\n====================================Exercise 5.1.1=====================================\n');
	logging.info('Step a: Asking for user datetime input ... \n');
	year=raw_input('Please enter your desired year: \n');
	month=raw_input('Please enter your desired month: \n');
	day=raw_input('Please enter your desired day: \n');
	hour=raw_input('Please enter your desired hour: \n');
	minute=raw_input('Please enter your desired minute: \n');
	second=raw_input('Please enter your desired second: \n');
	microsecond=raw_input('Please enter your desired microsecond: \n');

	logging.info('Step b: Creating a datetime variable ... \n');
	time_var=datetime.datetime(year, month, day, hour, minute, second, microsecond)

	logging.info('Step c: Extracting the datetime and diaplaying ... \n');
	# time_var.year
	logging.info(time_var.strftime('Year:%Y \nMonth:%m \nDay:%d \nHour: %H \nMinute:%M \nSecond:%S \nMicrosecond:%f \n'));

	logging.info('Step d:')
	logging.info(time_var.strftime('%Y-%m-%d %H:%M:%S:%f'));

	logging.info('Step e:')
	logging.info(time_var.strftime('%Y %m %d %H %M %S %f'));

	now=datetime.datetime.now()
	utcnow=datetime.datetime.utcnow()
	myFunction();
	raw_input('Program pause. Press enter to continue.\n');

	# Exercise xyz
	# Write comments
	logging.info('\n====================================Exercise xyz=====================================\n');
	logging.info('Running my myFunction function ... \n');
	myFunction();
	raw_input('Program pause. Press enter to continue.\n');

if __name__=='__main__':
	main()
