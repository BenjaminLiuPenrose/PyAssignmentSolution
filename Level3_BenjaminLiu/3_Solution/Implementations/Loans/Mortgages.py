# -*- coding: utf-8 -*- 
#!/usr/bin/env python
'''
Student name: Beier (Benjamin) Liu
Date: 2/14/2018
Exercise 

Remark:
Python 2.7 is recommended
'''
from Implementations.Loans.Loans import VariableRateLoan, FixedRateLoan
from Implementations.Assets.Asset import *
import logging
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
			logging.error('The entered home does not belong to HouseBase. \n');
		super(MortgageMixin, self).__init__(self._home, face, rate, term)

	def PMI(self, period):
		LTV=float(self.balanceRecur(period-1))/self._home.initValue
		if LTV>=0.80:
			return 0.000075
		else :
			return 0.0

	def monthlyPayment(self, period):
		pmt=float((self._face*self._rate))/(1-(1+self._rate)**(-self._term))+self.PMI(period)*super(MortgageMixin, self).balanceRecur(period-1);
		return pmt


	def principalDueRecur(self, period): 
		return self.monthlyPayment(period)-super(MortgageMixin, self).interestDueRecur(period)- \
		self.PMI(period)*super(MortgageMixin, self).balanceRecur(period-1);


class VariableMortgage(MortgageMixin, VariableRateLoan):
	pass
	# def __init__(self, asset, face, rateDict, term):
	# 	super(VariableRateLoan, self).__init__()

class FixedMortgage(MortgageMixin, FixedRateLoan):
	pass
	# def __init__(self, asset, face, rate, term):
	# 	super(FixedMortgage, self).__init__()

