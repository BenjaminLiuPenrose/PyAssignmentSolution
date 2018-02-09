#!/usr/bin/env python
# -*- coding: utf-8 -*- 
'''
Student name: Beier (Benjamin) Liu
Date:
Exercise 1.3

Remark:
Python 2.7 is recommended
Before running please install packages
Using cmd line py -2.7 -m install [package_name]
'''
from Implementations.Implementation import *


'''===================================================================================================
Main program:
Write comments

Implementations:
Write comments
==================================================================================================='''

def main():
	# Exercise 1.3
	# Write comments
	print('\n====================================Exercise xyz=====================================\n');
	print('Running my myFunction function ... \n');
	myFunction();
	raw_input('Program pause. Press enter to continue.\n');

if __name__=='__main__':
	a=iterGenFibo(10);
	print(a);
	b, _, _=recurGenFibo(10);
	print(b)
	# main()