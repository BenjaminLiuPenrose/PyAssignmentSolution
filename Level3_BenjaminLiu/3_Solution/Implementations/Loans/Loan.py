# -*- coding: utf-8 -*- 
#!/usr/bin/env python
'''
Student name: Beier (Benjamin) Liu
Date: 2/14/2018
Exercise 

Remark:
Python 2.7 is recommended
'''
from Implementations.Assets.Asset import *
import logging
logging.getLogger().setLevel(logging.DEBUG)

'''===================================================================================================
File content:

==================================================================================================='''

class Loan(object):
	# Initialization
	def __init__(self, asset, face, rate, term):
		if isinstance(asset, Asset):
			self._asset=asset;
		else :
			self._asset=PrimaryHome(face);
			logging.exception('The input asset is not of type Asset. \n');
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

	# @property
	def rate(self, period=1):
		return float(self._rate);

	# @rate.setter
	def rate(self, irate, period=1):
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
		pmt=float((self.face*self.rate(period)))/(1-(1+self.rate(period))**(-self.term));
		return pmt 

	def totalPayments(self, period): #this method no rate is involved
		pmt=self.monthlyPayment(period);
		pmtTtl=pmt*self.term;
		return pmtTtl

	def totalInterest(self, period):
		instTtl=self.face*self.rate(period)*self.term;
		return instTtl

	# Not preferred
	def interestDueFoml(self, period):
		instDue=self.balanceFoml(period-1)*self.rate(period);
		return instDue 

	# Not preferred
	def principalDueFoml(self, period): #this method no rate is involved
		faceDue=self.balanceFoml(period-1)-self.balanceFoml(period);
		return faceDue

	# Not preferred
	def balanceFoml(self, period): 
		balance=self.face*((1+self.rate(period))**period)- \
		self.monthlyPayment(period)*((1+self.rate(period))**period-1)/self.rate(period)
		return balance 

	def interestDueRecur(self, period): 
		return self.balanceRecur(period-1)*self.rate(period)

	def principalDueRecur(self, period): #this method no rate is involved
		return self.monthlyPayment(period)-self.interestDueRecur(period)

	def balanceRecur(self, period): #this method no rate is involved
		if period==0:
			return self.face
		else :
			return self.balanceRecur(period-1)-self.principalDueRecur(period)

	# Not prefered
	def monthlyPayment2(self, period): #period is dummy variable 
		pmt=self.calcMonthlyPmt(self.face, self.rate(period), self.term);
		return pmt 

	def recoveryValue(self, period):
		recoveryMult=0.60;
		return self._asset.getPresValue(period)*recoveryMult

	def equity(self, period):
		return self._asset.getPresValue(period)-self.balanceRecur(period) 


