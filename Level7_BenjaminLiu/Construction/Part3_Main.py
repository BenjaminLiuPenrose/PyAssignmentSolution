# -*- coding: utf-8 -*- 
#!/usr/bin/env python
'''
Student name: Beier (Benjamin) Liu
Date: 2/22/2018
Project Part 3

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
from simulateWaterfallParallel_m import *
from runMonte_m import *
logging.getLogger().setLevel(logging.INFO)
np.random.seed(int(time.time()));
'''===================================================================================================
Main program:
demo Part 3

Implementations:
implementation code for this part can be found at Solution\Implementations\Tranches\TrancheBase.py
==================================================================================================='''

def main():
	print('\n====================================Part 3 (Same as Part 1)=====================================\n');
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
	logging.debug('The first tranche is {}'.format(myStructuredSecurity.tranches[0].subordination))
	raw_input('Program pause. Press enter to continue.\n');

	'''===================================================================================================
	Implementation and demo for Part3
	==================================================================================================='''
	print('\n====================================Part 3 (Different from Part 1)=====================================\n');
	print('Seeking optimal numProcess for multiProcessing ... \n');
	ans=raw_input('Sir, do you want to explore the optimal numProcess ? [y/n] \n');
	try :
		if ans.lower()=='y':
			numProcess_list=[2+2*i for i in range(8)]; numProcess_list.insert(0, 1)
			minimum=original=float("inf"); optimal_processes=None;
			for numProcess in numProcess_list:
				s=time.time(); 
				res=simulateWaterfallParallel(myLoanPool, myStructuredSecurity, NSIM=2000, numProcess=numProcess);
				e=time.time();
				if e-s<minimum and res.get('DIRR tranches')!=[]:
					optimal_processes=numProcess; minimum=e-s;
				if numProcess==1:
					original=e-s
				logging.info('Using {} processes, it takes time {}'.format(numProcess, e-s))
			logging.info('Original it takes {} secs without multiprocessing; with multiprocessing method, it takes {} secs with optimal_processes {}.'\
				.format(original, minimum, optimal_processes))
			raw_input('Program pause. Press enter to continue.\n');
		else :
			optimal_processes=4;
	except Exception as e:
		logging.exception('Error Message: {}'.format(e));
		logging.info('The optimal_processes will be set to 4.')


	print('Running my runMonte function ... \n');
	# res=runMonte(myLoanPool, myStructuredSecurity, NSIM=2000, tol=0.005);
	res=runMonte(myLoanPool, myStructuredSecurity, NSIM=2000, tol=0.005, numProcess=optimal_processes);
	rate=res.get('rate');
	logging.info('The result optimal rates are {}'.format(rate))
	resStructuredSecurity=StructuredSecurity(myLoanPool.ttlPrincipal(), 'Sequencial');
	tranchesChar=[(0.8, 0.05, 'A'), (0.2, 0.08, 'B')]
	tranchesChar=[(percent, rate[idx], subordination) for idx, percent, _, subordination in enumerate(tranchesChar)]
	for percent, rate, subordination in tranchesChar:
		resStructuredSecurity.addTranche(percent, rate, subordination);
	output=doWaterfall(myLoanPool, resStructuredSecurity);

	print('Printing IRR, DIRR, WAL and letter rating for Tranche A and Tranche B to the screen ... \n');
	IRR=output.get('IRR tranches'); DIRR=output.get('DIRR tranches'); WAL=output.get('WAL tranches');
	letter=[toLetterRating(dirr) for dirr in DIRR]; 
	for idx, _, rate, subordination in enumerate(tranchesChar):
		logging.info('{0} trenche: class {1}, the rate is {2}, the IRR is {3}, the DIRR is {4}, the AL is {5}, the letter rating is {6}.'.\
			format(idx, subordination, rate, IRR[0], DIRR[0], WAL[0], letter[0]))
	raw_input('Part 3 demo finished successfully. Press any key to exit.\n');



if __name__=='__main__':
	main()