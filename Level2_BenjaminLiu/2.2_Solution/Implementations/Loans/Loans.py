# -*- coding: utf-8 -*- 
#!/usr/bin/env python
'''
Student name: Beier (Benjamin) Liu
Date:Liu 2/14/2018
Exercise 2.2.1

Remark:
Python 2.7 is recommended
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