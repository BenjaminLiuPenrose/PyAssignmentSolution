# -*- coding: utf-8 -*- 
#!/usr/bin/env python
'''
Student name: Beier (Benjamin) Liu
Date: 2/10/2017
Exercise 1.4

Remark:
Python 2.7 is recommended
Before running please install packages *numpy
Using cmd line py -2.7 -m install [package_name]
'''
import copy
import numpy as np

'''===================================================================================================
File contents:
Implementations for Exercise 1.4
Implementations for 1.4_Main.py
==================================================================================================='''

# Exercise 1.4.1 implementation
# You are a lender, holding onto a large number of mortgages. Create code that does the following:
# a. A function that returns an unsorted list of mortgage amounts, in thousands. Numbers should range from 100 to 1,000 and do not need to all be unique
# b. Filter the result of a) into three lists: Amounts below 200, amounts between 200 and 467, and amounts greater than 467. Call these ‘miniMortgages’, 
# ‘standardMortgages’, and ‘jumboMortgages’ respectively
# c. Use the all function with an if statement to verify that the resulting lists of b) indeed contain only numbers within the specified ranges.

# Exercise 1.4.1 a) implementation
# Functions returns a list
def mortageLs():
	mortageAmt=[];
	while 1:
		iamt=raw_input('Please add the amount (in thousands) of new moratge (s to stop; d to use default moratge generator): \n');
		if iamt=='s' and len(mortageAmt)>0:
			print('Mortages are ready. \n')
			break;
		elif iamt=='s' and len(mortageAmt)==0:
			print('Sorry sir, please enter a least one moartage amount. ');
		elif iamt=='d':
			mortageAmt=list(np.random.randint(100, 1000+1, 100));
			print('Random moratge amounts are generated successfully. Mortages are ready. \n');
			break;
		else:
			try:
				amt=float(iamt);
				if amt<100:
					print('Sorry sir, amount should be at least 100. Please enter again. ');
				elif amt>1000:
					print('Sorry sir, amount should be at least 100. Please enter again. ');
				else:
					mortageAmt.append(amt);
			except Exception as e:
				print('Error message'+str(e)+'\n');
				print('Sorry sir, please enter a number. Please enter again.  ');
	return mortageAmt

# Exercise 1.4.1 b) implementation
# Functions returns three lists	
def mortageFilter(mortage, param1=200, param2=467):
	miniMortages=[]; standardMortages=[]; jumboMortages=[];
	mortageAmt=copy.deepcopy(mortage);
	for m in mortageAmt:
		if m<param1 :
			miniMortages.append(m);
		elif m>param2 :
			jumboMortages.append(m);
		else :
			standardMortages.append(m);
	return miniMortages, standardMortages, jumboMortages

# Exercise 1.4.1 c) implementation
# Remark: this function is evetually not used in the Exercise Demo in Main
def checkRange(**kwargs):
	bool_1=1; bool_2=1;
	if kwargs.get('upper bound'):
		bool_1=(all(Ls)<=kwargs.get('upper bound'));
	if kwargs.get('lower bound'):
		bool_2=(all(Ls)>=kwargs.get('upper bound'));
	return bool(bool_1*bool_2)

# Exercise 1.4.2 implementation
# Find the length of each list in part b of the previous exercise. Then, verify that the lengths of all three lists indeed add up to the 
# length of the full list in part a
# Functions returns three strings and a boolean value
def checkLength(mortageAmt=None, miniMortages=None, standardMortages=None, jumboMortages=None):
	num_ttl=0; num_mini=0; num_std=0; num_jumbo=0; msg_mini=msg_std=msg_jumbo=''; bl=False;
	if mortageLs:
		num_ttl=len(mortageAmt);
		msg_mini='The number of total mortages is '+str(num_mini)+'\n';
	if miniMortages:
		num_mini=len(miniMortages);
		msg_mini='The number of mini mortages is '+str(num_mini)+'\n';
	if standardMortages:
		num_std=len(standardMortages);
		msg_std='The number of standard mortages is '+str(num_std)+'\n';
	if jumboMortages:
		num_jumbo=len(jumboMortages);
		msg_jumbo='The number of standard mortages is '+str(num_jumbo)+'\n';
	if num_mini+num_std+num_jumbo==num_ttl:
		bl=True
	return msg_mini, msg_std, msg_jumbo, bl 
