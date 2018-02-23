# -*- coding: utf-8 -*- 
#!/usr/bin/env python
'''
Student name: Beier (Benjamin) Liu
Date: 2/22/2018
Project Part 3.2, 3.4

Remark:
Python 2.7 is recommended
'''
import os, time, logging
import copy, math
import functools, itertools
import numpy as np 
from Implementations.Assets.AssetBase import *
from Implementations.Tools import *
logging.getLogger().setLevel(logging.DEBUG)
'''===================================================================================================
File content:
==================================================================================================='''
class Loan(object):
	def __init__(self, asset, face, rate, term, mode='normal'):
		if isinstance(asset, Asset):
			self._asset=asset;
		else :
			self._asset=PrimaryHome(face); # random asset
		self._face=face;
		if isinstance(rate, (int, float)) :
			self._rate=Loan.monthlyRate(rate);
		else :
			self._rate=0.05; 
		self._term=term;
		self._mode=mode;

	@property
	def face(self):
		return self._face;
	@face.setter
	def face(self, iface):
		self._face=iface;

	@property
	def term(self):
		return self._term;
	@term.setter
	def term(self, iterm):
		self._term=iterm;

	@property
	def mode(self):
		return self._mode
	@mode.setter
	def mode(self, imode):
		if imode.lower()=='defaulted' or imode.lower()=='normal':
			self._mode=imode.lower()

	@staticmethod
	def monthlyRate(APR):
		return APR/12.0
	@staticmethod
	def annualRate(monthlyRate):
		return monthlyRate*12.0
	@classmethod
	def calcMonthlyPmt(cls, face, rate, term):
		rate=monthlyRate(rate)
		return (face*rate)/(1-(1+rate)**(-term));
	@classmethod
	def calcBalance(cls, face, rate, term, period):
		rate=monthlyRate(rate)
		return face*((1+rate)**period)- \
		cls.calcMonthlyPmt(face, rate, term)*((1+rate)**period-1)/rate;

	def rate(self, period=1):
		return self._rate 

	def monthlyPayment(self, period=1):
		return (self._face*self.rate(period))/(1.0-(1.0+self.rate(period))**(-self._term))
	def totalPayments(self, period=1):
		return self.monthlyPayment(period)*self._term
	def totalInterest(self, period=1):
		return self._face*self.rate(period)*self._term

	@memoize
	def interestDueRecur(self, period): 
		return self.balanceRecur(period-1)*self.rate(period) if (self._mode!='defaulted' and period<=self._term) else 0
	@memoize
	def principalDueRecur(self, period): 
		return self.monthlyPayment(period)-self.interestDueRecur(period) if (self._mode!='defaulted' and period<=self._term) else 0
	@Timer
	@memoize
	def balanceRecur(self, period): 
		if self._mode=='defaulted' or period > self._term:
			return 0
		if period==0:
			return self._face
		else :
			return self.balanceRecur(period-1)-self.principalDueRecur(period)

	# Not preferred
	def interestDueFoml(self, period):
		return self.balanceFoml(period-1)*self.rate(period)
	def principalDueFoml(self, period):
		return self.balanceFoml(period-1)-self.balanceFoml(period)
	def balanceFoml(self, period): 
		return self._face*((1+self.rate(period))**period)- \
		self.monthlyPayment(period)*((1+self.rate(period))**period-1)/self.rate(period) 

	def recoveryValue(self, period):
		return self._asset.getPresValue(period)*self._asset.recoveryMult if period<=self._term else 0
	def equity(self, period):
		return self._asset.getPresValue(period)-self.balanceRecur(period) 
	'''===================================================================================================
	Implementation and demo for Part3.2, 3.4
	==================================================================================================='''
	def checkDefault(self, num, period):
		if num==0 and period<=self._term and self._mode!='defaulted':
			self._mode='defaulted';
			logging.debug('Loan is defaulted.And the recovery value is {}'.format(self.recoveryValue(period)))
			return self.recoveryValue(period)
		else :
			return 0

	

class FixedRateLoan(Loan):
	def rate(self, period=1):
		return self._rate

class VariableRateLoan(Loan):
	def __init__(self, asset, face, rateDict, term):
		self._rateDict=rateDict;
		super(VariableRateLoan, self).__init__(asset, face, None, term)

	def rate(self, period=1):
		return self._rateDict.get(period)