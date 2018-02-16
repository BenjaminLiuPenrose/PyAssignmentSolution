# -*- coding: utf-8 -*- 
#!/usr/bin/env python
'''
Student name: Beier (Benjamin) Liu
Date: 2/14/2018
Exercise 2.2.7

Remark:
Python 2.7 is recommended
Before running please install packages
Using cmd line py -2.7 -m install [package_name]
'''
from Implementations.Loans.Loan import *
from Implementations.Loans.Mortgages import *
from Implementations.Loans.AutoLoans import *
from Implementations.Timer import *

'''===================================================================================================
Main program:
# Exercise 2.2.7
# Now that we have our Loan and Asset classes, let’s incorporate the asset into the loan. As a loan 
# is ‘on an’ asset, which is similar to ‘has a’, we use composition instead of derivation. To this end:
# a. Add an asset parameter to the base loan __init__ function, which saves it down into an object-level 
# attribute. The one caveat here is that we must to ensure that the asset parameter indeed contains an 
# Asset object (or any of its derived classes). If it’s not an Asset type, you should print an error 
# message to the user, and leave the function.
# b. Modify MortgageMixin to initialize with a home parameter. In this case, we need to ensure that the 
# value of home is indeed a primary home, vacation home, or any other derived HouseBase type. Modify the 
# PMI function to calculate LTV based on the asset initial value (instead of the loan’s face value).
# c. Do the same for the AutoLoan class.
# d. Create a method called recoveryValue in the Loan base class. This method should return the current 
# asset value for the given period, times a recovery multiplier of 0.6.
# e. Create a method called equity in the Loan base class. This should return the available equity 
# (the asset value less the loan balance)

# f. In main, instantiate different Loan types with different assets and test the new functionality

Implementations:
See file 2.2_Solution\Implementations\Loans\Loan.py
==================================================================================================='''

def main():
	# f) In main, instantiate different Loan types with different assets and test the new functionality
	print('======================================Exercise 2.2.7=====================================')
	print('Running my recoveryValue and equity function ... \n');
	home=PrimaryHome(initValue=1000000, yearlyDepre=0.20);
	# varMortgage=VariableMortgage(home, 1000000, {1:0.05,2:0.06,3:0.08,4:0.12,5:0.08,6:0.05}, 6);
	fixMortgage=FixedMortgage(home=home, face=1000000, rate=0.05, term=6);
	civic_car=Civic(initValue=100000, yearlyDepre=0.20);
	autoloan=AutoLoan(auto=civic_car, face=1000000, rate= 0.06, term=12);
	# print(varMortgage.recoveryValue(3), varMortgage.equity(3));
	print(fixMortgage.recoveryValue(3), fixMortgage.equity(3));
	print(autoloan.recoveryValue(3), autoloan.equity(3));
	raw_input('The demo successfully finished. Press press any key to exit.\n');


if __name__=='__main__':
	main()
