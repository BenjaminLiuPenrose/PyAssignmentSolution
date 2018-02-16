# -*- coding: utf-8 -*- 
#!/usr/bin/env python
'''
Student name: Beier (Benjamin) Liu
Date:
Exercise Exercise 2.2.2 and 2.2.3

Remark:
Python 2.7 is recommended
Before running please install packages *logging
Using cmd line py -2.7 -m install [package_name]
'''
from Implementations.Loans.Loans import VariableRateLoan, FixedRateLoan
import logging

'''===================================================================================================
File content:
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
==================================================================================================='''

# Exercise 2.2.2
class MortgageMixin(Object):
	def __init__(self, home, face, rate, term):
		if isinstance(home, HouseBase):
			self._home=home;
		else :
			self._home=HouseBase(face); 	
			logging.error('The entered home does not belong to HouseBase. \n');
		super(MortgageMixin, self).__init__()

	def PMI(self, period):
		LTV=float(self.balanceRecur(period-1))/self._home.initValue
		if LTV>=0.80:
			return 0.000075
		else :
			return 0.0

	def monthlyPayment(self, period):
		pmt=float((self._face*self._rate))/(1-(1+self._rate)**(-self._term))+self.PMI(period)*super(MortgageMixin, self).balanceRecur(period-1);
	# def interestDueRecur(self, period): 
	# 	return self.balanceRecur(period-1)*self._rate

	def principalDueRecur(self, period): 
		return self.monthlyPayment(period)-super(MortgageMixin, self).interestDueRecur(period-1)- \
		self.PMI(period)*super(MortgageMixin, self).balanceRecur(period-1);

	# def balanceRecur(self, period): 
	# 	if period==0:
	# 		return self._face
	# 	else :
	# 		return self.balanceRecur(period-1)-self.principalDueRecur(period)

# Exercise 2.2.3
class VariableMortgage(MortgageMixin, VariableRateLoan):
	pass
	# def __init__(self, asset, face, rateDict, term):
	# 	super(VariableRateLoan, self).__init__()

class FixedMortgage(MortgageMixin, FixedRateLoan):
	pass
	# def __init__(self, asset, face, rate, term):
	# 	super(FixedMortgage, self).__init__()

