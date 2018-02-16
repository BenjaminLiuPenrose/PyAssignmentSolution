# -*- coding: utf-8 -*- 
#!/usr/bin/env python
'''
Student name: Beier (Benjamin) Liu
Date:
Exercise 2.2.5

Remark:
Python 2.7 is recommended
Before running please install packages
Using cmd line py -2.7 -m install [package_name]
'''

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
Write comments
==================================================================================================='''

def main():
	# Exercise 2.2.5
	# Write comments
	print('\n====================================Exercise 2.2.5=====================================\n');
	print('Running my myFunction function ... \n');
	myFunction();
	raw_input('Program pause. Press enter to continue.\n');

if __name__=='__main__':
	main()