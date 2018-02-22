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
	print('\n====================================Part 3 (Same as Part 1)=====================================\n');
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


	print('\n====================================Part 3 (Different from Part 1)=====================================\n');
	


	
	print('Printing IRR, DIRR, AL and letter rating for Tranche A and Tranche B to the screen ... \n');
	letter_s=[toLetterRating(DIRR) for DIRR in DIRR_s]; DIRR_s; IRR_s; AL_s
	logging.info('For trenche A, the IRR is {0}, the DIRR is {1}, the AL is {2}, the letter rating is {3}.'.\
		format(IRR_s[0], DIRR_s[0], AL_s[0], letter_s[0]))
	logging.info('For trenche B, the IRR is {0}, the DIRR is {1}, the AL is {2}, the letter rating is {3}.'.\
		format(IRR_s[1], DIRR_s[1], AL_s[1], letter_s[1]))
	raw_input('Part 3 demo finished successfully. Press any key to exit.\n');

def toLetterRating(DIRR):
	DIRR*=10000.0;
	letter=['Aaa','Aa1','Aa2','Aa3','A1','A2','A3','Baa1','Baa2','Baa3','Ba1','Ba2','Ba3','B1','B2','B3','Caa','Ca'];
	threshold=[0.06, 0.67,1.3,2.7,5.2,8.9,13.0,19.0,27.0,46.0,72.0,106.0,143.0,183.0,231.0,311.0,2500.0,10000.0];
	letter_rate='C';
	cnt=0;
	while 1:
		if DIRR <= threshold[cnt]:
			letter_rate=letter[cnt];
			break
		cnt+=1;
	return letter_rate


if __name__=='__main__':
	main()