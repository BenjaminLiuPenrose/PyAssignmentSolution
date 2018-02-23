# -*- coding: utf-8 -*- 
#!/usr/bin/env python
'''
Student name: Beier (Benjamin) Liu
Date: 

Remark:
Python 2.7 is recommended
'''
import os, time, logging
import copy, math
import functools, itertools
import numpy as np 
from Implementations.Loans.LoanBase import *
from Implementations.Assets.House import *
from Implementations.Toolsimport *
logging.getLogger().setLevel(logging.DEBUG)

'''===================================================================================================
File content:

==================================================================================================='''

class MortgageMixin(object):
	def __init__(self, home, face, rate, term):
		if isinstance(home, HouseBase):
			self._home=home;
		else :
			self._home=HouseBase(face); 	
			logging.error('The entered home does not belong to HouseBase.');
		super(MortgageMixin, self).__init__(self._home, face, rate, term)

	def PMI(self, period):
		LTV=float(self.balanceRecur(period-1))/self._home.initValue
		if LTV >= 0.80:
			return 0.000075
		else :
			return 0.0
	@memoize
	def monthlyPayment(self, period):
		pmt=float((self._face*self._rate))/(1-(1+self._rate)**(-self._term));
		pmt+=self.PMI(period)*super(MortgageMixin, self).balanceRecur(period-1);
		return pmt
	@memoize
	def principalDueRecur(self, period): 
		return self.monthlyPayment(period)-super(MortgageMixin, self).interestDueRecur(period)- \
		self.PMI(period)*super(MortgageMixin, self).balanceRecur(period-1);



class VariableMortgage(MortgageMixin, VariableRateLoan):
	pass

class FixedMortgage(MortgageMixin, FixedRateLoan):
	pass
