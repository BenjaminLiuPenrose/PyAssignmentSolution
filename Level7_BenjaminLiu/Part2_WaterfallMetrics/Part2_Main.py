# -*- coding: utf-8 -*- 
#!/usr/bin/env python
'''
Student name: Beier (Benjamin) Liu
Date:
Project Part 2

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
from Implementations.Tranches.StandardTranche import *
logging.getLogger().setLevel(logging.INFO)
'''===================================================================================================
Main program:
Write comments

Implementations:
Write comments
==================================================================================================='''

def main():
	# Create a LoanPool object that consists of 1,500 loans. Use the provided CSV file of loan data 
	# to create these Loan objects.
	print('\n====================================Part 2=====================================\n');
	print('Creating a LaonPool object with the csv file of loan data ... \n');
	myLoanPool=LoanPool()
	with open('Loans2.csv', 'r') as f:
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

	print('Instantiate my StructuredSecurity object ... \n');
	myStructuredSecurity=StructuredSecurity(myLoanPool.ttlPrincipal(), 'Sequencial');
	myStructuredSecurity.addTranche(0.8, 0.05, 'A');
	myStructuredSecurity.addTranche(0.2, 0.15, 'B');
	logging.debug('The first tranche is {}'.format(myStructuredSecurity.tranches[0].rate*12.0))

	print('Running my doWaterfall function and saving to a csv file ... \n');
	waterfall_s, waterfall_l, reserve_account, IRR_s, DIRR_s, AL_s=doWaterfall(myLoanPool, myStructuredSecurity);
	logging.debug('The waterfall for StructuredSecurity is {}'.format(waterfall_s));
	logging.debug('The waterfall for LoanPool is {}'.format(waterfall_l));
	logging.debug('The reserve_account is {}'.format(reserve_account));
	logging.debug('The IRR for StructuredSecurity is {}'.format(reserve_account));
	logging.debug('The DIRR for StructuredSecurity is {}'.format(reserve_account));
	logging.debug('The AL for StructuredSecurity is {}'.format(reserve_account));
	waterfall_liabilities=[];
	for period, tranches in enumerate(waterfall_s):
		ls=[period];
		for t in tranches:
			ls+=[t[0], t[1], t[2], t[3], t[4]]
		waterfall_liabilities.append(ls);
	logging.debug('Waterfall for L is {}'.format(waterfall_liabilities))
	with open('liabilities.csv', 'w') as f:
		header=['Period', 'A_interestDue', 'A_interestPaid', 'A_interetShort', 'A_principalPaid', 'A_balance'];
		header+=['B_interestDue', 'B_interestPaid', 'B_interetShort', 'B_principalPaid', 'B_balance'];
		f.write(','.join(header)); f.write('\n');
		for row in waterfall_liabilities:
			row=[str(entry) for entry in row];
			f.write(','.join(row)); f.write('\n');
	logging.info('file liabilities.csv is generated successfully.')

	waterfall_asset=[];
	for period, item in enumerate(waterfall_l):
		ls=[period];
		ls+=[item[0], item[1], item[2], item[3], item[4]]
		waterfall_asset.append(ls);
	logging.debug('Waterfall for A is {}'.format(waterfall_asset))
	with open('asset.csv', 'w') as f:
		header=['Period', 'Principal', 'Interest', 'Recoveries', 'Total', 'Balance'];
		f.write(','.join(header)); f.write('\n');
		for row in waterfall_asset:
			row=[str(entry) for entry in row];
			f.write(','.join(row)); f.write('\n');
	logging.info('file asset.csv is generated successfully.')

	raw_input('Part 1 demo finished successfully. Press any key to exit.\n');

def toLetterRating(self):
	pass

if __name__=='__main__':
	main()