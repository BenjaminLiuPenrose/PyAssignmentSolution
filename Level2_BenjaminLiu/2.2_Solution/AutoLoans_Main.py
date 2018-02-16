# -*- coding: utf-8 -*- 
#!/usr/bin/env python
'''
Student name: Beier (Benjamin) Liu
Date: 2/14/201
Exercise 2.2.4

Remark:
Python 2.7 is recommended
Before running please install packages
Using cmd line py -2.7 -m install [package_name]
'''
from Implementations.Loans.AutoLoans import *
from Implementations.Assets.Asset import *

'''===================================================================================================
Main program:
# Exercise 2.2.4
# Create a fixed AutoLoan class. This should derive-from the appropriate base class(es)

Implementations:
See file 2.2_Solution\Implementations\Loans\AutoLoans.py
==================================================================================================='''

def main():
	# Exercise 2.2.4
	print('\n====================================Exercise 2.2.4=====================================\n');
	print('Creating my fixed AutoLoan object function ... \n');
	civic_car=Civic(initValue=100000, yearlyDepre=0.20);
	autoloan=AutoLoan(auto=civic_car, face=1000000, rate= 0.06, term=12);
	raw_input('The demo successfully finished. Press press any key to exit.\n\n');

if __name__=='__main__':
	main()