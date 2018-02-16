# -*- coding: utf-8 -*- 
#!/usr/bin/env python
'''
Student name: Beier (Benjamin) Liu
Date:
Exercise 3.1.1 to 3.1.5

Remark:
Python 2.7 is recommended
Before running please install packages *numpy
Using cmd line py -2.7 -m install [package_name]
'''
import copy
import logging
import numpy as np 
from functools import *

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
# The previous exercise presents a good use-case for functools.partial:
# a. Create a partial called reconcileListsBreakAbsolute (which uses the breakAbsolute function)
# Test this comprehensively.
# b. Create similar partial functions for each of the break* functions in the previous exercise

Implementations:
Implementations are followed by the main() function
==================================================================================================='''

def main():
	# Exercise 3.1.1
	print('\n====================================Exercise 3.1.1=====================================\n');
	print('Running my stored lambda hypotenuse function ... \n');
	hypotenuse = lambda base, height: (base**2+height**2)**0.5
	print('The hypotenuse of base {base} and height {height} is {hypotenuse} \n'.format(base=6, height=8, hypotenuse=hypotenuse(6, 8)))
	raw_input('Program pause. Press enter to continue.\n');

	# Exercise 3.1.2
	print('\n====================================Exercise 3.1.2=====================================\n');
	print('Using reduce function ... \n');
	loanAmounts=[10000, 15000, 50000, 100000];
	loanTerms=[12, 18, 6, 24];
	rates=[.04, .0375, .032, .054];
	def WAM(total, (loanAmounts, loanTerms)):
		total+=loanAmounts*loanTerms
		return total
	WAM=reduce(WAM, zip(loanAmounts, loanTerms), 0)
	WAR=reduce(lambda total, (face, rate): total+(face*rate), zip(loanAmounts, rates), 0)
	print('The Weighted Average Maturity is {}. \n'.format(WAM));
	print('The Weighted Average Rate is {}. \n'.format(WAR));
	raw_input('Program pause. Press enter to continue.\n');	

	# Exercise 3.1.3
	print('\n====================================Exercise 3.1.3=====================================\n');
	print('Running my reconcileLists function ... \n');
	list_1=[1,2,3,4,5,6,7,8,9,10,11,12];
	list_2=[1,2,3,4,5,6,7,8,9,10,11,12];
	list_3=[1,2,3,4,5,6,6,8,9,10,12,12];
	rlist_1=reconcileLists(list_1, list_2);
	rlist_2=reconcileLists(list_2, list_3);
	rlist_3=reconcileLists(list_1, list_3);
	print('The original lists are {}, {} and {}. \n'.format(list_1, list_2, list_3));
	print('The reconcileLists are {}, {} and {}. \n'.format(rlist_1, rlist_2, rlist_3));
	raw_input('Program pause. Press enter to continue.\n');

	# Exercise 3.1.4
	print('\n====================================Exercise 3.1.4=====================================\n');
	print('Running my reconcileLists function with break* lambda functions ... \n');
	breakAbsolute = lambda var1, var2, epsilon: False if abs(var1-var2)<=epsilon else True
	breakRelative = lambda var1, var2, percent: False if abs((var1-var2)/var2)<=percent else True
	breakAbsRelative = lambda var1, var2, percent: False if abs((abs(var1)-abs(var2))/var2)<=percent else True
	list_1=[1,2,3,4,5,6,7,8,9,10,11,12];
	list_2=[1,2,3,4,5,6,7,8,9,10,11,12];
	list_3=[1,2,3,4,5,6,6,8,9,10,12,12];
	rlist_1=reconcileLists(list_1, list_2, functools.partial(breakAbsolute, epsilon=e-4));
	rlist_2=reconcileLists(list_2, list_3, functools.partial(breakRelative, percent=e-4));
	rlist_3=reconcileLists(list_1, list_3, functools.pertial(breakAbsRelative, percent=e-4));
	print(rlist_1, rlist_2, rlist_3)
	raw_input('Program pause. Press enter to continue.\n');

	# Exercise 3.1.5
	print('\n====================================Exercise 3.1.5=====================================\n');
	print('Running my reconcileListsBreakAbsolute, reconcileListsBreakRelative, reconcileListsBreakAbsRelative function ... \n');
	reconcileListsBreakAbsolute=functools.pertial(reconcileLists, breakFn=functools.partial(breakAbsolute, epsilon=e-4))
	reconcileListsBreakRelative=functools.pertial(reconcileLists, breakFn=functools.partial(breakRelative, percent=e-4))
	reconcileListsBreakAbsRelative=functools.pertial(reconcileLists, breakFn=functools.partial(breakAbsRelative, percent=e-4))
	raw_input('Program pause. Press enter to continue.\n');

	# Exercise xyz
	# Write comments
	print('\n====================================Exercise xyz=====================================\n');
	print('Running my myFunction function ... \n');
	myFunction();
	raw_input('Program pause. Press enter to continue.\n');

def reconcileLists(Lst1, Lst2, breakFn=None):
	if len(Lst1)!=len(Lst2):
		logging.error('Two list should be the same size. \n')
	length=min(len(Lst1), len(Lst2))
	if length<10 :
		logging.error('List should be at least of size 10. \n');
	Ls1=copy.deepcopy(Lst1); Ls2=copy.deepcopy(Lst2); Ls=[];
	if breakFn==None:
		breakFn=lambda var1, var2: False if var1==var2 else True 
	for i in range(length):
		if not breakFn(Ls1[i], Ls2[i]) :
			Ls.append(True);
		else :
			Ls.append(False);
	return Ls

if __name__=='__main__':
	main()