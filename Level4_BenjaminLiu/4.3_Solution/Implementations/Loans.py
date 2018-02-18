# -*- coding: utf-8 -*- 
#!/usr/bin/env python
'''
Student name: Beier (Benjamin) Liu
Date:Liu 2/14/2018
Exercise 

Remark:
Python 2.7 is recommended
'''
from Implementations.Loan import *

'''===================================================================================================
File content:

==================================================================================================='''

class FixedRateLoan(Loan):
	def rate(self, period):
		return self._rate

class VariableRateLoan(Loan):
	def __init__(self, asset, face, rateDict, term):
		self._rateDict=rateDict;
		super(VariableRateLoan, self).__init__(asset, face, None, term)

	def rate(self, period):
		return self._rateDict.get(period)