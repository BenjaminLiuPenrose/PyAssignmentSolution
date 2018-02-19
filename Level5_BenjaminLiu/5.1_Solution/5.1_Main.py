# -*- coding: utf-8 -*- 
#!/usr/bin/env python
'''
Student name: Beier (Benjamin) Liu
Date:
Exercise 5.1.1 to 5.1.5

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
See implementations in the code followed by the main() program
==================================================================================================='''

def main():
	# Exercise 5.1.1
	logging.info('\n====================================Exercise 5.1.1=====================================\n');
	while 1:
		try :
			logging.info('Step a: Asking for user datetime input ... \n');
			year=int(raw_input('Please enter your desired year: \n'));
			month=int(raw_input('Please enter your desired month: \n'));
			day=int(raw_input('Please enter your desired day: \n'));
			hour=int(raw_input('Please enter your desired hour: \n'));
			minute=int(raw_input('Please enter your desired minute: \n'));
			second=int(raw_input('Please enter your desired second: \n'));
			microsecond=int(raw_input('Please enter your desired microsecond: \n'));
			break
		except Exception as e:
			logging.info('{} \nInvalid input, please enter again. \n');

	logging.info('Step b: Creating a datetime variable ... \n');
	time_var=datetime.datetime(year, month, day, hour, minute, second, microsecond)

	logging.info('Step c: Extracting the datetime and diaplaying ... \n');
	# time_var.year
	logging.info(time_var.strftime('\nYear:%Y \nMonth:%m \nDay:%d \nHour: %H \nMinute:%M \nSecond:%S \nMicrosecond:%f \n'));

	logging.info('Step d: Displaying the datetiem with format one ... ');
	logging.info(time_var.strftime('%Y-%m-%d %H:%M:%S:%f'));

	logging.info('Step e: Displaying the datetime with format two ... ');
	logging.info(time_var.strftime('%Y %B %d %I:%M:%S:%f %p'));

	now=datetime.datetime.now()
	logging.info('\nStep f: Displaying the local time with two formats ... ');
	logging.info('Displaying the datetiem with format one ... ');
	logging.info(now.strftime('%Y-%m-%d %H:%M:%S:%f'));

	logging.info('Displaying the datetime with format two ... ');
	logging.info(now.strftime('%Y %B %d %I:%M:%S:%f %p'));

	utcnow=datetime.datetime.utcnow()
	logging.info('\nStep e: Displaying the UTC time with two formats ... ');
	logging.info('Displaying the datetiem with format one ... ');
	logging.info(utcnow.strftime('%Y-%m-%d %H:%M:%S:%f'));

	logging.info('Displaying the datetime with format two ... ');
	logging.info(utcnow.strftime('%Y %B %d %I:%M:%S:%f %p'));
	raw_input('Program pause. Press enter to continue.\n');

	# Exercise 5.1.2
	logging.info('\n====================================Exercise 5.1.2=====================================\n');
	strdate1=raw_input('Please enter the datetime in the following format: (yyyy-mm-dd hh:mm:ss:fffff) ... \n');
	date1=datetime.datetime.strptime(strdate1, '%Y-%m-%d %H:%M:%S:%f');
	logging.info('Time is stored. {}. \n'.format(date1))
	raw_input('Program pause. Press enter to continue.\n');

	# Exercise 5.1.3
	logging.info('\n====================================Exercise 5.1.3=====================================\n');
	strdate2=raw_input('Please enter the datetime in the following format: (yyyy Month dd hh:mm:ss:fffff AM/PM) ... \n');
	date2=datetime.datetime.strptime(strdate2, '%Y %B %d %I:%M:%S:%f %p');
	logging.info('Time is stored. {}. \n'.format(date2))
	raw_input('Program pause. Press enter to continue.\n');

	# Exercise 5.1.4
	logging.info('\n====================================Exercise 5.1.4=====================================\n');
	logging.info('Running my dateCalculatorn function ... \n');
	dateCalculator();
	raw_input('Program pause. Press enter to continue.\n');

	# Exercise 5.1.5
	logging.info('\n====================================Exercise 5.1.5=====================================\n');
	logging.info('Running my dateDiff function ... \n');
	dateDiff();
	raw_input('Program pause. Press enter to continue.\n');


# Exercise 5.1.4 implementation
def dateCalculator():
	strdate=raw_input('Please enter one datetime in the following format: (yyyy-mm-dd hh:mm:ss:fffff) ... \n');
	strdatedelta=raw_input('Please enter datetime delta in the following format: (dd hh:mm:ss:fffff) ... \n');
	date=datetime.datetime.strptime(strdate, '%Y-%m-%d %H:%M:%S:%f');
	datedelta=datetime.datetime.strptime(strdatedelta, '%d %H:%M:%S:%f');

	date2=date+datetime.timedelta(days=datedelta.days, seconds=datedelta.seconds, microseconds=datedelta.microseconds)

	strdate2=strftime(date2, '%Y-%m-%d %H:%M:%S:%f');
	logging.info('The resulting time is {}.'.format(strdate2));
	logging.info('The date calculator is exiting. Have a nice day, sir!');

# Exercise 5.1.5 implementation
def dateDiff():
	strdate1=raw_input('Please enter one datetime in the following format: (yyyy-mm-dd hh:mm:ss:fffff) ... \n');
	strdate2=raw_input('Please enter another datetime in the following format: (yyyy-mm-dd hh:mm:ss:fffff) ... \n');
	date1=datetime.datetime.strptime(strdate1, '%Y-%m-%d %H:%M:%S:%f');
	date2=datetime.datetime.strptime(strdate2, '%Y-%m-%d %H:%M:%S:%f');

	datedelta=date2-date1;

	logging.info('The total number of days are {}.'.format(datedelta.days));
	logging.info('The total number of hours are {}.'.format(datedelta.hours));
	logging.info('The total number of minutes are {}.'.format(datedelta.minutes));
	logging.info('The total number of seconds are {}.'.format(datedelta.seconds));
	logging.info('The total number of microseconds are {}.'.format(datedelta.microseconds));
	logging.info('The difference is {0} days, {1} hours, {2} minutes, {3} seconds, and {4} microseconds.'.\
		format(datedelta.days, datedelta.hours, datedelta.minutes, datedelta.seconds, datedelta.microseconds));
	logging.info('The date differential is exiting. Have a nice day, sir!');

if __name__=='__main__':
	main()
