# -*- coding: utf-8 -*- 
#!/usr/bin/env python
'''
Student name: Beier (Benjamin) Liu
Date:
Project Part 1

Remark:
Python 2.7 is recommended
Before running please install packages *numpy
Using cmd line py -2.7 -m install [package_name]
'''
import os, time, logging
import copy, math
import functools, itertools
import numpy as np 
from Implementations.Loans.LoanPool import *
from Implementations.Tranches.StructuredSecurity import *
from Implementations.Loans.AutoLoan import *
from Implementations.Assets.Car import *
from Implementations.Tranches.StandardTrache import *
logging.getLogger().setLevel(logging.DEBUG)

'''===================================================================================================
Main program:
Write comments

Implementations:
Write comments
==================================================================================================='''

def main():
	# Create a LoanPool object that consists of 1,500 loans. Use the provided CSV file of loan data 
	# to create these Loan objects.
	print('\n====================================Part 1.1=====================================\n');
	print('Creating a LaonPool object with the csv file of loan data ... \n');
	myLoanPool=LoanPool()
	for i in range(1500):
		car=Car(intValue);
		loan=AutoLoan(car, face, rate, term);
		myLoanPool.loans.append(loan);
	logging.debug('The first loan is {}'.format(myLoanPool.loans[0].rate(1)))
	raw_input('Program pause. Press enter to continue.\n');

	# Instantiate your StructuredSecurities object, specify the total notional (from the LoanPool), add 
	# two standard tranches (class A and class B in terms of subordination), and specify sequential or 
	# pro-rata mode
	# The rates for each tranche can be arbitrary (for now). Note that subordinated tranches should always 
	# have a higher rate, as they have increased risk
	print('\n====================================Part 1.2=====================================\n');
	print('Instantiate my StructuredSecurity object ... \n');
	myStandardTrache_A=StandardTrache(myLoanPool.ttlPrincipal()/3.0, 0.1, 'A');
	myStandardTrache_B=StandardTrache(myLoanPool.ttlPrincipal()/3.0*2, 0.2, 'B');
	myStructuredSecurity=StructuredSecurity('Sequential', myStandardTrache_A, myStandardTrache_B);
	raw_input('Program pause. Press enter to continue.\n');

	# Call doWaterfall and save the results into two CSV files (one for the asset side and one for the 
	# liabilities side). All the tranches’ data for a given time period should be a single row in the CSV 
	# The reserve account balance should also be in liabilities CSV, for each time period. Each time period 
	# gets its own row. Note that you may need to do some clever list comprehensions and string parsing to 
	# get this to output correctly
	print('\n====================================Part 1.3=====================================\n');
	print('Running my doWaterfall function and saving to a csv file ... \n');
	waterfall_s, waterfall_l, reserve_account=doWaterfall(myLoanPool, myStructuredSecurity);
	raw_input('Program pause. Press enter to continue.\n');

	# Write comments
	print('\n====================================Exercise xyz=====================================\n');
	print('Running my myFunction function ... \n');
	myFunction();
	raw_input('Program pause. Press enter to continue.\n');

if __name__=='__main__':
	main()
