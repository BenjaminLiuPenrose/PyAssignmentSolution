# -*- coding: utf-8 -*- 
#!/usr/bin/env python
'''
Student name: Beier (Benjamin) Liu
Date:
Exercise 3.1.1

Remark:
Python 2.7 is recommended
Before running please install packages
Using cmd line py -2.7 -m install [package_name]
'''

'''===================================================================================================
Main program:
# Exercise 3.1.1
# Create a stored lambda function that calculates the hypotenuse of a right triangle; it should 
# take base and height as its parameter. Invoke (test) this lambda with different arguments

# Exercise 3.1.2
# This exercise is a modification of Exercise 1.5.8, to use the reduce function. To this end, create a 
# list of loan terms and a list of rates:
# a. Use the reduce function, with a regular function as its callable, to calculate the WAM of the list 
# of terms.
# b. Use the reduce function, with a lambda as its callable, to calculate the WAR of the list of rates
# c. Modify your WAR and WAM functions in your LoanPool class to use the above code

# Exercise 3.1.3
# Create a regular function (called reconcileLists) that takes two separate lists as its parameters. In 
# this example, List 1 represents risk valuations per trade (i.e. Delta) from Risk System A and List 2 
# has the same from Risk System B. The purpose of this function is to reconcile the two lists and report 
# the differences between the two systems. To this end, it should return a list of True or False values, 
# corresponding to each value in the lists (True means they match at index, False means they don’t match 
# at index).
# Test the reconcileLists function with different lists of values (lists should be of at least length ten)
# Note that the assumption is that both lists are the same length (report an error otherwise)

# Exercise 3.1.4
# To incorporate lambda into the previous exercise, do the following:
# a. Create a breakAbsolute stored lambda which takes two values and an epsilon parameter. This lambda 
# should ‘return’ True if the two values are not within epsilon of each other.
# b. Create a breakRelative stored lambda which takes two values and a percent parameter. This lambda 
# should ‘return’ True if the percent difference between the two values exceeds percent.
# c. Create a breakAbsRelative function which takes two values and a percent parameter. This should 
# return True if the percent difference between the absolute values of the two values exceeds percent.
# d. Modify the reconcileLists function to take a third parameter, called breakFn (this represents a 
# passed-in function or lambda). The reconcileLists function should utilize the passed-in breakFn 
# function to build the True/False list. You will need to use functools.partial to specify the 
# parameter of the breakFn function (i.e., epsilon or percent)
# e. Test reconcileLists with different lists of values (should be large lists of numbers) and 
# with each of the above break* functions

# Exercise 3.1.5
The previous exercise presents a good use-case for functools.partial:
a. Create a partial called reconcileListsBreakAbsolute (which uses the breakAbsolute function)
Test this comprehensively.
b. Create similar partial functions for each of the break* functions in the previous exercise

Implementations:
Write comments
==================================================================================================='''

def main():
	# Exercise 3.1.1
	print('\n====================================Exercise 3.1.1=====================================\n');
	print('Running my myFunction function ... \n');
	myFunction();
	raw_input('Program pause. Press enter to continue.\n');


	# Exercise xyz
	# Write comments
	print('\n====================================Exercise xyz=====================================\n');
	print('Running my myFunction function ... \n');
	myFunction();
	raw_input('Program pause. Press enter to continue.\n');

if __name__=='__main__':
	main()