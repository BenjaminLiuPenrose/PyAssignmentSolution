# -*- coding: utf-8 -*- 
#!/usr/bin/env python
'''
Student name: Beier (Benjamin) Liu
Date: 2/14/2018
Exercise 2.2.2 and 2.2.3 

Remark:
Python 2.7 is recommended
Before running please install packages
Using cmd line py -2.7 -m install [package_name]
'''
from Implementations.Loans.Mortgages import *
from Implementations.Assets.Asset import *

'''===================================================================================================
Main program:
Exercise 2.2.2
# Create a MortgageMixin class which will contain mortgage-specific methods. In particular, we’d like
# to implement the concept of Private Mortgage Insurance (PMI). For those unaware, PMI is an extra 
# monthly payment that one must make to compensate for the added risk of having a Loan-to-Value (LTV) 
# ratio of less than 80% (in other words, the loan covers >= 80% of the value of the asset).
# To this end, implement a function called PMI that returns 0.0075% of the loan face value, but only 
# if the LTV is < 80%. For now, assume that the initial loan amount is for 100% of the asset value
# Additionally, override the base class monthlyPayment and principalDue functions to account for PMI 
# (Hint: use super to avoid duplicating the formulas, and note that the other methods (interestDue, 
# balance, etc.) should not require any changes)

Exercise 2.2.3
# Create a VariableMortgage and FixedMortgage class. These should each derive-from the appropriate 
# base class(es) (TBD by student)

Implementations:
See file 2.2_Solution\Implementations\Loans\Mortgages.py
==================================================================================================='''

def main():
	# Exercise 2.2.2 and 2.2.3
	print('\n====================================Exercise 2.2.2 & 2.2.3=====================================\n');
	print('Creating a MortgageMixin class, a VariableMortgage and a FixedMortgage ... \n');
	home=PrimaryHome(initValue=1000000, yearlyDepre=0.20);
	varMortgage=VariableMortgage(home, 1000000, {1:0.05,2:0.06,3:0.08,4:0.12,5:0.08,6:0.05}, 6);
	fixMortgage=FixedMortgage(home=home, face=1000000, rate=0.05, term=6);
	raw_input('The demo successfully finished. Press press any key to exit.\n\n');

if __name__=='__main__':
	main()