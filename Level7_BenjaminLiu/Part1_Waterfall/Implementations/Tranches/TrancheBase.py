# -*- coding: utf-8 -*- 
#!/usr/bin/env python
'''
Student name: Beier (Benjamin) Liu
Date:
Project Part

Remark:
Python 2.7 is recommended
Before running please install packages *numpy
Using cmd line py -2.7 -m install [package_name]
'''
import os, time, logging
import copy, math
import functools, itertools
import numpy as np 
logging.getLogger().setLevel(logging.DEBUG)

'''===================================================================================================
File content:
Write comments
==================================================================================================='''

class Tranche(object):
	def __int__(self, face, rate, subordination):
		self._face=face;
		self._rate=rate;

		self._currentTime=0;
		self._principalHistory={};
		self._interestHistory={};
		self._interestShort={};
		self._principalShort={};
		if isinstance(subordination, (str, int, float)):
			self._subordination=subordination;
		else :
			self._subordination='A'; #
			logging.error('Please enter a number or alphabet letter for subordination.')

	@property
	def rate(self):
		return self._rate
	@rate.setter
	def rate(self, iRate):
		self._rate=iRate;

	def getSubord(self):
		return self._subordination

	def getCurrentTime(self):
		return self._currentTime

	def getPrincipalHistory(self):
		return self._principalHistory

	def getInterestHistory(self):
		return self._interestHistory

	def getPrincipalShort(self):
		return self._principalShort

	def getInterestShout(self):
		return self._interestShort

	def IRR(self):
		ls=[self._principalHistory[i]+self._interestHistory[i] for i, _ in enumertae(self.getPrincipalHistory())]
		ls.insert(0, -self._face);
		IRR=np.IRR(ls); IRR*=12.0;
		return IRR

	def DIRR(self):
		return self.IRR()-self._rate

	def AL(self):
		if self.notionalBalance()!=0 :
			return None 
		else :
			AL=reduce(lambda total, (time, principalPayment): total+time*principalPayment, (time, principalPayment), 0);
			AL=AL/float(self._face);
			return AL 

