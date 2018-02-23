# -*- coding: utf-8 -*- 
#!/usr/bin/env python
'''
Student name: Beier (Benjamin) Liu
Date: 2/22/2018
Project Part 1

Remark:
Python 2.7 is recommended
Before running please install packages *numpy
Using cmd line py -2.7 -m install [package_name]
'''
import os, time, datetime, logging
import copy, math
import functools, itertools
import numpy as np 
from Implementations.Loans.LoanPool import *
from Implementations.Tranches.StructuredSecurity import *
from Implementations.Loans.AutoLoan import *
from Implementations.Assets.Car import *
from Implementations.Tranches.StandardTranche import *
logging.getLogger().setLevel(logging.INFO)
np.random.seed(int(time.time()));
'''===================================================================================================
Main program:
demo Part1.1, 1.2 and 1.3

Implementations:
implementation code for this part can be found at Solution\Implementations\Tranches\*.py
It is suggested that one can open all .py files in \Tranches to check
==================================================================================================='''

def main():
	'''===================================================================================================
	Implementation for Part1.1
	==================================================================================================='''
	# Create a LoanPool object that consists of 1,500 loans. Use the provided CSV file of loan data 
	# to create these Loan objects.
	print('\n====================================Part 1.1=====================================\n');
	print('Creating a LoanPool object with the csv file of loan data ... \n');
	myLoanPool=LoanPool()
	with open('Loans.csv', 'r') as f:
		f.readline();cnt=0;
		while 1:
			line=f.readline();
			if line=='':
				break
			elif cnt==1500: # cnt id for debug perpose
				break
			else :
				lst=line.split(',');
				# logging.debug(lst);
				loan=AutoLoan(Civic(initValue=float(lst[6])), face=float(lst[2]), rate=float(lst[3]), term=float(lst[4]))
				myLoanPool.loans.append(loan);
				cnt+=1;

	logging.debug('The first loan is {}'.format(myLoanPool.loans[0].face))
	raw_input('Program pause. Press enter to continue.\n');

	'''===================================================================================================
	Implementation for Part1.2
	==================================================================================================='''
	# Instantiate your StructuredSecurities object, specify the total notional (from the LoanPool), add 
	# two standard tranches (class A and class B in terms of subordination), and specify sequential or 
	# pro-rata mode
	# The rates for each tranche can be arbitrary (for now). Note that subordinated tranches should always 
	# have a higher rate, as they have increased risk
	print('\n====================================Part 1.2=====================================\n');
	print('Instantiate my StructuredSecurity object ... \n');
	myStructuredSecurity=StructuredSecurity(myLoanPool.ttlPrincipal(), 'Sequencial');
	myStructuredSecurity.addTranche(0.8, 0.05, 'A');
	myStructuredSecurity.addTranche(0.2, 0.08, 'B');
	logging.debug('The first tranche is {}'.format(myStructuredSecurity.tranches[0].rate*12.0))
	raw_input('Program pause. Press enter to continue.\n');

	'''===================================================================================================
	Implementation for Part1.3
	==================================================================================================='''
	# Call doWaterfall and save the results into two CSV files (one for the asset side and one for the 
	# liabilities side). All the tranches’ data for a given time period should be a single row in the CSV 
	# The reserve account balance should also be in liabilities CSV, for each time period. Each time period 
	# gets its own row. Note that you may need to do some clever list comprehensions and string parsing to 
	# get this to output correctly
	print('\n====================================Part 1.3=====================================\n');
	print('Running my doWaterfall function and saving to a csv file ... \n');
	logging.info('Attention: when running doWaterfall(), I will run checkDefaults(). Or you can go to file StructuredSecurity.py->doWaterfall() to disable it. \n');
	waterfall_s, waterfall_l, reserve_account, IRR_s, DIRR_s, AL_s=doWaterfall(myLoanPool, myStructuredSecurity);
	logging.debug('The waterfall for StructuredSecurity is {}'.format(waterfall_s));
	logging.debug('The waterfall for LoanPool is {}'.format(waterfall_l));
	logging.debug('The reserve_account is {}'.format(reserve_account));
	logging.debug('The IRR for StructuredSecurity is {}'.format(IRR_s));
	logging.debug('The DIRR for StructuredSecurity is {}'.format(DIRR_s));
	logging.debug('The AL for StructuredSecurity is {}'.format(AL_s));
	waterfall_liabilities=[];
	for period, tranches in enumerate(waterfall_s):
		ls=[period+1];
		for t in tranches:
			ls+=[t[0], t[1], t[2], t[3], t[4]]
		waterfall_liabilities.append(ls);
	logging.debug('Waterfall for L is {}'.format(waterfall_liabilities))
	timestr=datetime.datetime.now().strftime('%H%M%S');
	with open('liabilities_{}.csv'.format(timestr), 'w') as f:
		header=['Period', 'A_interestDue', 'A_interestPaid', 'A_interetShort', 'A_principalPaid', 'A_balance'];
		header+=['B_interestDue', 'B_interestPaid', 'B_interetShort', 'B_principalPaid', 'B_balance'];
		f.write(','.join(header)); f.write('\n');
		for row in waterfall_liabilities:
			row=[str(round(entry,2)) for entry in row];
			f.write(','.join(row)); f.write('\n');
	logging.info('file liabilities.csv is generated successfully.')

	waterfall_asset=[];
	for period, item in enumerate(waterfall_l):
		ls=[period+1];
		ls+=[item[0], item[1], item[2], item[3], item[4]]
		waterfall_asset.append(ls);
	logging.debug('Waterfall for A is {}'.format(waterfall_asset))
	with open('asset_{}.csv'.format(timestr), 'w') as f:
		header=['Period', 'Principal', 'Interest', 'Recoveries', 'Total', 'Balance'];
		f.write(','.join(header)); f.write('\n');
		for row in waterfall_asset:
			row=[str(round(entry,2)) for entry in row];
			f.write(','.join(row)); f.write('\n');
	logging.info('file asset.csv is generated successfully.')

	raw_input('Part 1 demo finished successfully. Press any key to exit.\n');


if __name__=='__main__':
	main()