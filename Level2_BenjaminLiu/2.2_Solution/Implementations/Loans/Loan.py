# -*- coding: utf-8 -*- 
#!/usr/bin/env python
'''
Student name: Beier (Benjamin) Liu
Date: 2/14/2018
Exercise 2.2.7

Remark:
Python 2.7 is recommended
'''
from Implementations.Assets.Asset import *
import logging
logging.getLogger().setLevel(logging.DEBUG)

'''===================================================================================================
File content:
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
# (the asset value less the loan balance).
# f. In main, instantiate different Loan types with different assets and test the new functionality
==================================================================================================='''

class Loan(object):
	# Initialization
	def __init__(self, asset, face, rate, term):
		if isinstance(asset, Asset):
			self._asset=asset;
		else :
			logging.error('The input asset is not of type Asset. \n');
		self._face=face;
		if isinstance(rate, (int, float)) :
			self._rate=Loan.monthlyRate(rate);
		else :
			self._rate=0.05; # _rate is the monthly interest rate, _term is the  number of months # _rate is the monthly interest rate, _term is the  number of months
		self._term=term;

	# Getter and setter
	@property
	def face(self):
		return float(self._face);

	@face.setter
	def face(self, iface):
		self._face=iface;

	@property
	def rate(self):
		return float(self._rate);

	@rate.setter
	def rate(self, irate):
		self._rate=irate;

	@property
	def term(self):
		return float(self._term);

	@term.setter
	def set(self, iterm):
		self._term=iterm;

	@property
	def asset(self):
		return self._asset

	@asset.setter
	def asset(self, iasset):
		self._asset=iasset

	# Static methods
	@staticmethod
	def monthlyRate(ATR):
		return float(ATR)/12

	@staticmethod
	def annualRate(monthlyRte):
		return float(monthlyRte)*12

	# Class methods
	@classmethod
	def calcMonthlyPmt(cls, face, rate, term):
		rate=monthlyRate(rate)
		return float((face*rate))/(1-(1+rate)**(-term));

	@classmethod
	def calcBalance(cls, face, rate, term, period):
		rate=monthlyRate(rate)
		return face*((1+rate)**period)- \
		cls.calcMonthlyPmt(face, rate, term)*((1+rate)**period-1)/rate;

	# Object-level methods
	def monthlyPayment(self, period): #period is dummy variable
		pmt=float((self._face*self._rate))/(1-(1+self._rate)**(-self._term));
		return pmt 

	def totalPayments(self, period): #this method no rate is involved
		pmt=self.monthlyPayment(period);
		pmtTtl=pmt*self._term;
		return pmtTtl

	def totalInterest(self):
		instTtl=self._face*self._rate*self._term;
		return instTtl

	# Not preferred
	def interestDueFoml(self, period):
		instDue=self.balanceFoml(period-1)*self._rate;
		return instDue 

	# Not preferred
	def principalDueFoml(self, period): #this method no rate is involved
		faceDue=self.balanceFoml(period-1)-self.balanceFoml(period);
		return faceDue

	# Not preferred
	def balanceFoml(self, period): 
		balance=self._face*((1+self._rate)**period)- \
		self.monthlyPayment(period)*((1+self._rate)**period-1)/self._rate
		return balance 

	def interestDueRecur(self, period): 
		return self.balanceRecur(period-1)*self._rate

	def principalDueRecur(self, period): #this method no rate is involved
		return self.monthlyPayment(period)-self.interestDueRecur(period)

	def balanceRecur(self, period): #this method no rate is involved
		if period==0:
			return self._face
		else :
			return self.balanceRecur(period-1)-self.principalDueRecur(period)

	# Not prefered
	def monthlyPayment2(self, period): #period is dummy variable 
		pmt=self.calcMonthlyPmt(self._face, self._rate, self._term);
		return pmt 

	def recoveryValue(self, period):
		recoveryMult=0.60;
		return self._asset.getPresValue(period)*recoveryMult

	def equity(self, period):
		return self._asset.getPresValue(period)-self.balanceRecur(period) 


