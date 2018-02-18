# -*- coding: utf-8 -*- 
#!/usr/bin/env python
'''
Student name: Beier (Benjamin) Liu
Date:
Exercise 5.2.1

Remark:
Python 2.7 is recommended
Before running please install packages *numpy
Using cmd line py -2.7 -m install [package_name]
'''
import os, time, logging
import copy, math
import functools, itertools
import numpy as np 
logging.getLogger().setLevel(logging.DEBUG)

'''===================================================================================================
Main program:
Exercise 5.2.1
Modify the Timer class to work as a decorator (feel free to use the provided sample code). Its 
usage should look like this:
An example output would look like: <function myFunc at 0x34173DF0>: 1.5467 seconds
How does this compare to the previous approach to using the context manager? When is this more useful 
and when are context managers more useful

Exercise 5.2.2
Create a decorator that memoize’s the result of a function. This decorator should be flexible enough 
that it can work with a function with any number of parameters. Note that memoizing should happen on 
a per-parameter basis; meaning, cache the result for every unique set of parameter values. Hint: Use a dict
Be sure to test this decorator on different functions to ensure it works properly. You should also use 
in conjunction with the timer decorator, to demonstrate that subsequent calls to the memoized function 
are quicker than the initial call for a given parameter set

Exercise 5.2.3
Use your memoization decorator from the previous exercise to memoize the recursive versions of the 
Loan waterfall functions. Time the functions before and after; do you see a difference

Implementations:
Write comments
==================================================================================================='''

def main():
	# Exercise xyz
	# Write comments
	print('\n====================================Exercise xyz=====================================\n');
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
