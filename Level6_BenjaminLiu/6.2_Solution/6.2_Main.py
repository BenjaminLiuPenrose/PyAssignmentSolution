# -*- coding: utf-8 -*- 
#!/usr/bin/env python
'''
Student name: Beier (Benjamin) Liu
Date:
Exercise 6.2.1

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
Exercise 6.2.1
In this exercise, we will look to make the Monty Hall simulation achieve true multi-processing. 
This is a good segue to financial Monte Carlo as the concepts and approaches are the same.
a) Create and initialize five processes. Note that starting processes takes some time, and is the 
upfront cost of using multi-processing.
b) Execute all five processes. Give each process 1/5 of the total simulations (2,000,000 each)
c) Combine the five returned results lists and take the average, to get the overall result.
d) Time all of the above (starting from b). Does total runtime improve from the previous level?
e) Try decreasing/increasing the number of processes to determine the optimal runtime

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

if __name__=='__main__':
	main()