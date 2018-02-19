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
from Implementations.Loans.Loan import *
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
See implementations followed by the main() function
==================================================================================================='''

def main():
	# Exercise 5.2.1
	# Write comments
	logging.info('\n====================================Exercise 5.2.1=====================================\n');
	logging.info('Running my myFunction function ... \n');
	myFunction(5);
	logging.info('The decorator approach looks simpler to write. If we need to use the Timer whenever we are calling method myFunction, decorator is helpful. If it is not the case, context manager is more helpful. \n')
	raw_input('Program pause. Press enter to continue.\n');

	# Exercise 5.2.2
	logging.info('\n====================================Exercise 5.2.2=====================================\n');
	logging.info('Running my myIntenseFunction function ... \n');
	logging.info(myIntenseFunction(1, 2));
	logging.info(myIntenseFunction(1, 2));
	logging.info('The later 0.0 sec is displayed since the second time the program skip the evaluation of myIntenseFunction already.')
	raw_input('Program pause. Press enter to continue.\n');

	# Exercise 5.2.3
	logging.info('\n====================================Exercise 5.2.3=====================================\n');
	logging.info('Running my myIntenseFunction function ... \n');
	logging.info(testOnLoan(6)) 
	logging.info(testOnLoan(8)) 
	logging.info(testOnLoan(6)) 
	logging.info('The later 0.0 sec is displayed since the second time the program skip the evaluation of myIntenseFunction already.')
	raw_input('Program pause. Press enter to continue.\n');

# Exercise 5.2.1 Implementation
def Timer(func):
	@functools.wraps(func)
	def wrapped(*args, **kwargs):
		s=time.time()
		res=func(*args, **kwargs);
		e=time.time()
		logging.info('{}: {} seconds.'.format(func, e-s))
		return res
	return wrapped

@Timer
def myFunction(input):
	time.sleep(input)
	return 'Done'

# Exercise 5.2.2 Implementation
def memoize(func):
    memo = {}
    @functools.wraps(func)
    def wrapped(*args):
        if args not in memo:            
            memo[args] = func(*args)
        return memo[args]
    return wrapped 

@Timer 
@memoize 
def myIntenseFunction(*args):
	time.sleep(5);
	return args

# Exercise 5.2.3 Implementation
@Timer
@memoize
def testOnLoan(period):
	loan=Loan(None, 1000000, 0.05, 12); # 12 months loan
	return loan.balanceRecur(period);

if __name__=='__main__':
	main()
