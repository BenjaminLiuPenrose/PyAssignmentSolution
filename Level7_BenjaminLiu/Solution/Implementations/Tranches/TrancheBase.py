# -*- coding: utf-8 -*- 
#!/usr/bin/env python
'''
Student name: Beier (Benjamin) Liu
Date: 2/22/2018
Project Part 1.1, Part 2.4, 2.5, 2.6

Remark:
Python 2.7 is recommended
'''
import os, time, logging
import copy, math
import functools, itertools
import numpy as np 
from Implementations.Tools import *
logging.getLogger().setLevel(logging.DEBUG)
'''===================================================================================================
File content:
class Tranche
==================================================================================================='''

'''===================================================================================================
Implementation for Part1.1
==================================================================================================='''
class Tranche(object):
	def __init__(self, face, rate, subordination):
		self._face=face;
		self._rate=Tranche.monthlyRate(rate);
		self._currentPeriod=0;
		self._principalHistory=[0];
		self._interestHistory=[0];
		self._principalShort=[0];
		self._interestShort=[0];
		self._interestDueHist=[0];
		self._balance=[face];
		if isinstance(subordination, (str, int, float)):
			self._subordination=subordination;
		else :
			self._subordination='A'; 
			logging.error('Please enter a number or alphabet letter for subordination.')

	@property
	def face(self):
		return self._face
	@face.setter
	def face(self, iface):
		self._face=iface;
	@property
	def rate(self):
		return self._rate
	@rate.setter
	def rate(self, irate):
		self._rate=Tranche.monthlyRate(irate);
	@property
	def subordination(self):
		return self._subordination
	@subordination.setter
	def subordination(self, isubord):
		self._subordination=isubord;
	@property
	def currentPeriod(self):
		return self._currentPeriod
	@currentPeriod.setter
	def currentPeriod(self, icurrentPeriod):
		self._currentPeriod=icurrentPeriod;
	@property
	def principalHistory(self):
		return self._principalHistory
	@property
	def interestHistory(self):
		return self._interestHistory
	@property
	def principalShort(self):
		return self._principalShort
	@property
	def interestShout(self):
		return self._interestShort
	@property
	def interestDueHist(self):
		return self._interestDueHist
	@property
	def balance(self):
		return self._balance
	@staticmethod
	def monthlyRate(APR):
		return APR/12.0

	def notionalBalance(self):
		raise NotImplementedError()

	'''===================================================================================================
	Implementation for Part2.4, 2.5 and 2.6
	==================================================================================================='''
	#@memoize
	def IRR(self):
		ls=[p+i for p, i in zip(self._principalHistory, self._interestHistory)];
		ls[0]=-self._face;
		IRR=np.irr(ls); IRR*=12.0;
		logging.info('Cash flow history (for IRR) for tranche with rate {} is {}'.format(self._rate*12.0, IRR))
		return round(IRR, 10)
	#@memoize
	def DIRR(self):
		return round(self._rate*12.0-self.IRR(), 10) # annual rate
	#@memoize
	def AL(self, balance):
		if round(balance,2)!=0.0 :
			return None 
		else :
			period=[i for i in range(len(self._principalHistory))]
			AL=reduce(lambda total, (period, principalPayment): total+period*principalPayment, zip(period, self._principalHistory), 0);
			AL=AL/float(self._face);
			return AL 
