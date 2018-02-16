# -*- coding: utf-8 -*- 
#!/usr/bin/env python
'''
Student name: Beier (Benjamin) Liu
Date: 2/14/2018
Exercise 2.2.5

Remark:
Python 2.7 is recommended
Before running please install packages
Using cmd line py -2.7 -m install [package_name]
'''
from Implementations.Loans.LoanPool import *
from Implementations.Loans.Loans import *

'''===================================================================================================
Main program:
# Exercise 2.2.5
# Create a LoanPool class that can contain and operate on a pool of loans (composition). Provide the 
# following functionality:
# a. A method to get the total loan principal.
# b. A method to get the total loan balance for a given period.
# c. Methods to get the aggregate principal, interest, and total payment due in a given period.
# d. A method that returns the number of ‘active’ loans. Active loans are loans that have a balance 
# greater than zero.
# e. Methods to calculate the Weighted Average Maturity (WAM) and Weighted Average Rate (WAR) of the 
# loans. You may port over the previously implemented global functions

Implementations:
See file 2.2_Solution\Implementations\Loans\LoanPool.py
==================================================================================================='''

def main():
	# Exercise 2.2.5
	print('\n====================================Exercise 2.2.5=====================================\n');
	print('Running my LoanPool class ... \n');
	pool=LoanPool(FixedRateLoan(None, 1000000, 0.05, 36), FixedRateLoan(None, 5000000, 0.03, 12), FixedRateLoan(None, 500000, 0.06, 6))
	print('The total face value is {}. \n'.format(pool.ttlPrincipal()));
	print('The total balnace at period {} is {}. \n'.format(3, pool.ttlBalance(3)));
	print('The total principal due at period {} is {}. \n'.format(3, pool.ttlPrincipalDue(3)));
	print('The total interest due at period {} is {}. \n'.format(3, pool.ttlInterestDue(3)));
	print('The total payment due at period {} is {}. \n'.format(3, pool.ttlPaymentDue(3)));
	print('The number of active loans at period {} is {}. \n'.format(10, pool.activeLoan(10)));
	print('The WAM is {}. \n'.format(pool.WAM()));
	print('The WAR is {}. \n'.format(pool.WAR()));
	raw_input('The demo successfully finished. Press press any key to exit.\n\n');

if __name__=='__main__':
	main()