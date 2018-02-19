# -*- coding: utf-8 -*- 
#!/usr/bin/env python
'''
Student name: Beier (Benjamin) Liu
Date: 2/18/2018
Exercise 4.2.3

Remark:
Python 2.7 is recommended
'''
from Implementations.Asset import *
from Implementations.Timer import *
import logging
# logging.getLogger().setLevel(logging.DEBUG)

'''===================================================================================================
File content:
# Exercise 4.2.3
# Add logging statements to your Loan class. This should consist of the following:
# a. Anytime an exception is thrown (i.e., when an incorrect Asset type is passed-into the initialization 
# function), log an error prior to raising the exception.
# b. Debug-level logs which display interim steps of calculations and return values for the Loan functions
# c. Info-level logs to display things like ‘t is greater than term’ in the loan functions
# d. At the point the exception is caught (in your main function) use logging.exception to display the 
# exception in addition to a custom message
# e. Add a warn log to the recursive versions of the waterfall functions (that they are expected to 
# take a long time, so the explicit versions are recommended)
==================================================================================================='''

class Loan(object):
	# Initialization
	def __init__(self, asset, face, rate, term):
		if isinstance(asset, Asset):
			self._asset=asset;
		else :
			self._asset=PrimaryHome(face);
			logging.error('The input asset is not of type Asset. \n');
			# raise Exception('The input asset is not of type Asset. \n');
		if isinstance(rate, (int, float)) :
			self._rate=Loan.monthlyRate(rate);
		else :
			self._rate=0.05; # _rate is the monthly interest rate, _term is the  number of months # _rate is the monthly interest rate, _term is the  number of months
		try :
			int(term); int(face);
			self._face=face;
			self._term=term;
		except Exception as e:
			logging.exception('{}. \nPlease enter number for rate and term'.format(e)) # Exception logging


	# Getter and setter
	@property
	def face(self):
		return float(self._face);

	@face.setter
	def face(self, iface):
		self._face=iface;

	@property
	def rate(self, period=1):
		return float(self._rate);

	@rate.setter
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
	def rate(self, period):
		return float(self._rate)

	def monthlyPayment(self, period): #period is dummy variable
		pmt=float((self.face*self.rate(period)))/(1-(1+self.rate(period))**(-self.term));
		logging.debug('The monthly payment for {} is {}.'.format(period, pmt))
		return pmt 

	def totalPayments(self, period): #this method no rate is involved
		pmt=self.monthlyPayment(period);
		pmtTtl=pmt*self.term;
		logging.debug('The total payment for {} is {}.'.format(period, pmtTtl))
		return pmtTtl

	def totalInterest(self, period):
		instTtl=self.face*self.rate(period)*self.term;
		logging.debug('The total interest for {} is {}.'.format(period, instTtl))
		return instTtl

	# Not preferred
	def interestDueFoml(self, period):
		if period > self.term:
			logging.info('Period is greater than the term.');
			return None
		instDue=self.balanceFoml(period-1)*self.rate(period);
		logging.debug('The interest due for {} is {}.'.format(period, instDue))
		return instDue 

	# Not preferred
	def principalDueFoml(self, period): #this method no rate is involved
		if period > self.term:
			logging.info('Period is greater than the term.');
			return None
		faceDue=self.balanceFoml(period-1)-self.balanceFoml(period);
		logging.debug('The principal due for {} is {}.'.format(period, faceDue))
		return faceDue

	# Not preferred
	def balanceFoml(self, period): 
		if period > self.term:
			logging.info('Period is greater than the term.');
			return None
		balance=self.face*((1+self.rate(period))**period)- \
		self.monthlyPayment(period)*((1+self.rate(period))**period-1)/self.rate(period)
		logging.debug('The balance for {} is {}.'.format(period, balance))
		return balance 

	def interestDueRecur(self, period): 
		t=Timer('Interest Due Recur Timer'); t.start();
		if period > self.term:
			logging.info('Period is greater than the term.');
			return None
		logging.debug('The interest due for {} is {}.'.format(period, self.balanceRecur(period-1)*self.rate(period)))
		t.end(); 
		if t.retrieve(0)>t.getWarnThreshold():
			logging.warning('The running time is over {} for {} and it is driving out your computer resource.'.format(t.getWarnThreshold(), t._timerName));
		return self.balanceRecur(period-1)*self.rate(period)

	def principalDueRecur(self, period): #this method no rate is involved
		t=Timer('Principal Due Recur Timer'); t.start();
		if period > self.term:
			logging.info('Period is greater than the term.');
			return None
		logging.debug('The principal due for {} is {}.'.format(period, self.monthlyPayment(period)-self.interestDueRecur(period)))
		t.end(); 
		if t.retrieve(0)>t.getWarnThreshold():
			logging.warning('The running time is over {} for {} and it is driving out your computer resource.'.format(t.getWarnThreshold(), t._timerName));
		return self.monthlyPayment(period)-self.interestDueRecur(period)

	def balanceRecur(self, period): #this method no rate is involved
		t=Timer('Balance Recur Timer'); t.start();
		if period > self.term:
			logging.info('Period is greater than the term.');
			return None
		if period==0:
			logging.debug('The balance for {} is {}.'.format(period, self.face))
			return self.face
		else :
			logging.debug('The balance for {} is {}.'.format(period, self.balanceRecur(period-1)-self.principalDueRecur(period)))
			t.end(); 
			if t.retrieve(0)>t.getWarnThreshold():
				logging.warning('The running time is over {} for {} and it is driving out your computer resource.'.format(t.getWarnThreshold(), t._timerName));
			return self.balanceRecur(period-1)-self.principalDueRecur(period)

	# Not prefered
	def monthlyPayment2(self, period): #period is dummy variable 
		pmt=self.calcMonthlyPmt(self.face, self.rate(period), self.term);
		logging.debug('The monthly payment for {} is {}.'.format(period, pmt))
		return pmt 

	def recoveryValue(self, period):
		if period > self.term:
			logging.info('Period is greater than the term.');
			return None
		recoveryMult=0.60;
		logging.debug('The recovery value for {} is {}.'.format(period, self._asset.getPresValue(period)*recoveryMult))
		return self._asset.getPresValue(period)*recoveryMult

	def equity(self, period):
		t=Timer('Equity Recur Timer'); t.start();
		if period > self.term:
			logging.info('Period is greater than the term.');
			return None
		logging.debug('The equity for {} is {}.'.format(period, self._asset.getPresValue(period)-self.balanceRecur(period)))
		t.end(); 
		if t.retrieve(0)>t.getWarnThreshold():
			logging.warning('The running time is over {} for {} and it is driving out your computer resource.'.format(t.getWarnThreshold(), t._timerName));
		return self._asset.getPresValue(period)-self.balanceRecur(period)