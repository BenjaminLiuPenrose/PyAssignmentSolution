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
from Implementations.Implementation import *

'''===================================================================================================
Main program:
Demo Exercise 1.4.1 - 1.4.5 in a row

Implementations:
See folder 1.4_Solution\Implementations
==================================================================================================='''

def main():
	# Exercise 1.4.1
	# See function implementation at Exercise 1.4.1 implementation
	print('\n====================================Exercise 1.4.1=====================================\n');
	print('Running my routine for exercise 1.4.1 ... \n');

	# a) Create an unsorted list of mortgage amounts
	# See function implementation at Exercise 1.4.1 a) implementation
	print('***Step a: creating a unsorted list of mortages.***\n')
	mortageAmt=mortageLs();
	print('Displaying the full mortage list: ');
	print(mortageAmt); 
	print('');

	# b) Filter the result of a) into three lists: Amounts below 200, amounts between 200 and 467, and amounts greater than 467. Call these ‘miniMortgages’, 
	# ‘standardMortgages’, and ‘jumboMortgages’ respectively
	# See function implementation at Exercise 1.4.1 b) implementation
	print('***Step b: sorting the mortages from (a) into three tranches.*** \n')
	mini, standard, jumbo=mortageFilter(mortageAmt, 200, 467);
	print('Displaying the three mortage lists: ');
	print(mini); 
	print(standard); 
	print(jumbo); 
	print('');

	# c) Checking the sorted mortages with all and if
	print('***Step c: checking the requirements with all and if.*** \n');
	# Checking the mini mortage
	if all(amt for amt in mini if amt<200):
		print('True, the mini is sorted correctly. ');
	else :
		print('Unfortunately, the mini is unproperly sorted. ');
	# Checking the standard mortage
	if all(amt for amt in standard if (amt>=200 and amt<=467)):
		print('True, the standard is sorted correctly. ');
	else :
		print('Unfortunately, the standard is unproperly sorted. ');
	# Checking the jumbo mortage
	if all(amt for amt in jumbo if amt>467):
		print('True, the jumbo is sorted correctly. ');
	else :
		print('Unfortunately, the jumbo is unproperly sorted. ');
	print('');

	# d) Checking the sorted mortages with any and if
	print('***Step d: checking the requirements with all and if.*** \n');
	# Checking the mini mortage
	if any(amt for amt in mini if amt>=200):
		print('Unfortunately, the mini is unproperly sorted. ');
	else :
		print('True, the mini is sorted correctly. ');		
	# Checking the standard mortage
	if any(amt for amt in standard if (amt<200 and amt>467)):
		print('Unfortunately, the standard is unproperly sorted. ');
	else :
		print('True, the standard is sorted correctly. ');
	# Checking the jumbo mortage
	if any(amt for amt in jumbo if amt<=467):
		print('Unfortunately, the jumbo is unproperly sorted. ');
	else :
		print('True, the jumbo is sorted correctly. ');
	print('');

	raw_input('Program pause. Press enter to continue. \n');

	# Exercise 1.4.2
	# Find the length of each list in part b of the previous exercise. Then, verify that the lengths of all three lists indeed add up to the 
	# length of the full list in part a
	# Functions returns three strings and a boolean value
	print('\n====================================Exercise 1.4.2=====================================\n');
	print('Running my checkLength function ... \n');
	msg_mini, msg_std, msg_jumbo, bl =checkLength(mortageAmt, mini, standard, jumbo);
	msg='Sorry sir, the total number of mortages does not match. \n';
	if bl==True:
		msg='The total number of mortages matches. \n';
	print(msg_mini); print(msg_std); print(msg_jumbo); print(msg);
	raw_input('Program pause. Press enter to continue.\n');

	# Exercise 1.4.3
	# Sum the full list of mortgages, to obtain the total amount owed to your firm
	print('\n====================================Exercise 1.4.3=====================================\n');
	print('Running my routine for Exercise 1.4.3 ... \n');
	amtTtl=sum(mortageAmt)*1000;
	print('The total amount owed to firm is '+str(round(amtTtl,2))+'\n');
	raw_input('Program pause. Press enter to continue.\n');

	# Exercise 1.4.4
	# Find the minimum and maximum mortgage amount owed, for each mortgage sub-list
	print('\n====================================Exercise 1.4.4=====================================\n');
	print('Running my routine for Exercise 1.4.4 ... \n');
	mini_max=max(mini);
	mini_min=min(mini);
	std_max=max(standard);
	std_min=min(standard);
	jumbo_max=max(jumbo);
	jumbo_min=min(jumbo);
	print('The minimum amount of mini mortage is {} and the maximum amount is {}. \n'.format(mini_min, mini_max));
	print('The minimum amount of stadard mortage is {} and the maximum amount is {}. \n'.format(std_min, std_max));
	print('The minimum amount of jumbo mortage is {} and the maximum amount is {}. \n'.format(jumbo_min, jumbo_max));
	raw_input('Program pause. Press enter to continue.\n');

	# Exercise 1.4.5
	# Create any code that demonstrates usage of the abs function
	print('\n====================================Exercise 1.4.5=====================================\n');
	print('Running my routine for Exercise 1.4.5 ... \n');
	print('Comparing the difference (absolute diff) between a=100 and b=600 ... \n');
	a=100; b=600
	print('The absolute diff between a and b is '+str(abs(a-b))+'\n');
	print('The absolute diff between a and b is '+str(abs(b-a))+'\n');
	raw_input('Program pause. Press enter to continue.\n');


if __name__=='__main__':
	main()