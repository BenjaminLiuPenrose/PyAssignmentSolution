# -*- coding: utf-8 -*- 
#!/usr/bin/env python
'''
Student name: Beier (Benjamin) Liu
Date:
Exercise xxx:

Remark:
Python 2.7 is recommended
Before running please install packages
Using cmd line py -2.7 -m install [package_name]
'''
from Implementations.Loans.Loan import *

'''===================================================================================================
File content:
Exercise 2.2.1
# As shown in the lecture, create derived classes as follows:
# a. A FixedRateLoan class which derives from Loan.
# b. A VariableRateLoan class which derives from Loan. This should have its own __init__ function that 
# sets a _rateDict attribute on the object and then invokes the super-class’ __init__ function. Override 
# the base-class rate function as follows:
# Modify the Loan class functions to use the rate (or getRate) function to get the rate for the current 
# period. Note that the monthly payment and balance formulas are different in this Variable case

Exercise 2.2.7
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
# (the asset value less the loan balance).
# f. In main, instantiate different Loan types with different assets and test the new functionality
==================================================================================================='''

# Exercise 2.2.1
class FixedRateLoan(Loan):
	def rate(self, period):
		return self._rate

class VariableRateLoan(Loan):
	def __init__(self, asset, face, rateDict, term):
		self._rateDict=rateDict;
		super(VariableRateLoan, self).__init__(asset, face, None, term)

	def rate(self, period):
		return self._rateDict.get(period)




