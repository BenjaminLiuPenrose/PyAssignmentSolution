# -*- coding: utf-8 -*- 
#!/usr/bin/env python
'''
Student name: Beier (Benjamin) Liu
Date:
Exercise 2.1.1

Remark:
Python 2.7 is recommended
Before running please install packages
Using cmd line py -2.7 -m install [package_name]
'''
from Implementations.Timer import *

'''===================================================================================================
Main program:
# Exercise 2.1.1 Demo
# a. Create a class called Timer.
# b. Add a start method and end method. They should work as follows:
# c. Note that start should give an error if the Timer is already started and end should give an error if the 
# Timer is not currently running.
# d. Add the ability to configure the Timer to display either seconds, minutes, or hours.
# e. Add a method to retrieve the last timer result.
# f. Test your class thoroughly.

Implementations:
See file 2.1_Solution\Implementations\Timer.py
==================================================================================================='''

def main():
	# Exercise 2.1.1
	print('\n====================================Exercise 2.1.1 (a)=====================================\n');
	
	# a) Create a class called Timer
	print('In step a: Creating a object t belongs to class Timer ... \n');
	ta=Timer();
	print('Type of new object t is '+str(type(ta))+'\n');
	raw_input('Program pause. Press enter to continue.\n');

	# b) Add a start method and end method
	print('\n====================================Exercise 2.1.1 (b)=====================================\n');
	print('In step b: Using start and end method ... \n');
	ta.start();
	for i in range(10000000): #some random functions that takes time to execute
		i+=1;
	ta.end();
	raw_input('Program pause. Press enter to continue.\n');

	# c) Note that start should give an error if the Timer is already started and end should give an error if the 
	# Timer is not currently running
	print('\n====================================Exercise 2.1.1 (c)=====================================\n');
	print('In step c: start and end will raise errors message if unappropriate call ... \n');
	print('Case 1 demo: start is called after the timer is started. \n');
	tc=Timer();
	tc.start();
	tc.start();
	print('Case 2 demo: end is called before the timer is started. \n');
	tc2=Timer();
	tc2.end();
	raw_input('Program pause. Press enter to continue.\n');

	# d) Add the ability to configure the Timer to display either seconds, minutes, or hours
	print('\n====================================Exercise 2.1.1 (d)=====================================\n');
	print('In step d: Running my display function ... \n');
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

	# e) Add a method to retrieve the last timer result
	print('\n====================================Exercise 2.1.1 (e)=====================================\n');
	te=Timer();
	te.start();
	for i in range(10000000):
		i+=1;
	te.end(); te.start();
	for i in range(5000000):
		i*=1;
	te.end();
	print('Running my retrieve function ... \n');
	print('Retriving the current data: \n');
	print(str(te.retrieve(0))+'\n');
	print('Retriving the previous one data: \n');
	print(str(te.retrieve(1))+'\n');
	raw_input('Timer demo is successfully finished. Press any key to exit. \n');

if __name__=='__main__':
	main()

