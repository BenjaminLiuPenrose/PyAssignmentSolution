# -*- coding: utf-8 -*- 
#!/usr/bin/env python
'''
Student name: Beier (Benjamin) Liu
Date:
Project Part

Remark:
Python 2.7 is recommended
'''
import os, time, logging
import copy, math
import functools, itertools
import numpy as np 
logging.getLogger().setLevel(logging.DEBUG)
'''===================================================================================================
File content:

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

	def IRR(self):
		ls=[self._principalHistory[i]+self._interestHistory[i] for i in range(len(self._principalHistory))];
		ls.insert(0, -self._face);
		IRR=np.irr(ls); IRR*=12.0;
		return IRR

	def DIRR(self):
		return self.IRR()-self._rate*12.0 # annual rate

	def AL(self):
		if self.notionalBalance()!=0 :
			return None 
		else :
			period=[i for i in range(len(self._principalHistory))]
			AL=reduce(lambda total, (period, principalPayment): total+period*principalPayment, zip(period, self._principalHistory), 0);
			AL=AL/float(self._face);
			return AL 
