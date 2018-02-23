# -*- coding: utf-8 -*- 
#!/usr/bin/env python
'''
Student name: Beier (Benjamin) Liu
Date: 2/22/2018
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
np.random.seed(int(time.time()));
'''===================================================================================================
Main program:
demo Part2.4, 2.5 and 2.6

Implementations:
implementation code for this part can be found at Solution\Implementations\Tranches\TrancheBase.py
==================================================================================================='''

def main():
	print('\n====================================Part 2 (Same as Part 1)====================================\n');
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
				loan=AutoLoan(Civic(initValue=float(lst[6])), face=float(lst[2]), rate=float(lst[3]), term=float(lst[4]))
				myLoanPool.loans.append(loan);
				cnt+=1;

	print('Instantiate my StructuredSecurity object ... \n');
	myStructuredSecurity=StructuredSecurity(myLoanPool.ttlPrincipal(), 'Sequencial');
	tranchesChar=[(0.8, 0.05, 'A'), (0.2, 0.08, 'B')]
	for percent, rate, subordination in tranchesChar:
		myStructuredSecurity.addTranche(percent, rate, subordination);
	logging.debug('The first tranche is {}'.format(myStructuredSecurity.tranches[0].rate*12.0))

	print('Running my doWaterfall function ... \n');
	logging.info('Attention: when running doWaterfall(), I will run checkDefaults(). Or you can go to file StructuredSecurity.py->doWaterfall() to disable it. \n');
	res=doWaterfall(myLoanPool, myStructuredSecurity);
	raw_input('Program pause. Press enter to continue.\n');

	'''===================================================================================================
	Implementation and demo for Part2
	==================================================================================================='''
	print('\n====================================Part 2 (Different from Part 1)=====================================\n');
	print('Printing IRR, DIRR, WAL and letter rating for Tranche A and Tranche B to the screen ... \n');
	IRR=output.get('IRR tranches'); DIRR=output.get('DIRR tranches'); WAL=output.get('WAL tranches');
	letter=[toLetterRating(dirr) for dirr in DIRR]; 
	logging.info('For trenche A, the IRR is {0}, the DIRR is {1}, the AL is {2}, the letter rating is {3}.'.\
		format(IRR[0], DIRR[0], WAL[0], letter[0]))
	logging.info('For trenche B, the IRR is {0}, the DIRR is {1}, the AL is {2}, the letter rating is {3}.'.\
		format(IRR[1], DIRR[1], WAL[1], letter[1]))
	print('');
	raw_input('Part 2 demo finished successfully. Press any key to exit.\n');


if __name__=='__main__':
	main()