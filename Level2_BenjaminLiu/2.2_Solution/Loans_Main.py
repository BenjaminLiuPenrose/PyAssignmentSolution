# -*- coding: utf-8 -*- 
#!/usr/bin/env python
'''
Student name: Beier (Benjamin) Liu
Date: 2/14/2018
Exercise 2.2.1

Remark:
Python 2.7 is recommended
'''
from Implementations.Loans.Loans import *
from Implementations.Assets.Asset import *

'''===================================================================================================
Main program:
Exercise 2.2.1
# As shown in the lecture, create derived classes as follows:
# a. A FixedRateLoan class which derives from Loan.
# b. A VariableRateLoan class which derives from Loan. This should have its own __init__ function that 
# sets a _rateDict attribute on the object and then invokes the super-class’ __init__ function. Override 
# the base-class rate function as follows:
# Modify the Loan class functions to use the rate (or getRate) function to get the rate for the current 
# period. Note that the monthly payment and balance formulas are different in this Variable case

Implementations:
See file 2.2_Solution\Implementations\Loans\Loans.py
==================================================================================================='''

def main():
	# Exercise 2.2.1
	# Write comments
	print('\n====================================Exercise 2.2.1=====================================\n');
	print('Creating a FixedRateLoan and VariableRateLoan object ... \n');
	home=PrimaryHome(1000000);
	fixedLoan=FixedRateLoan(asset=home, face=1000000, rate=0.05, term=6);
	variableLoan=VariableRateLoan(asset=home, face=1000000, rateDict={1:0.05,2:0.06,3:0.08,4:0.12,5:0.08,6:0.05}, term=6);
	raw_input('The demo successfully finished. Press press any key to exit.\n\n');

if __name__=='__main__':
	main()