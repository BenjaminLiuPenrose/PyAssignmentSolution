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
from Implementations.Tranches.TrancheBase import *
logging.getLogger().setLevel(logging.DEBUG)

'''===================================================================================================
File content:
Write comments
==================================================================================================='''

class StandardTranche(Tranche):
	def increaseTimePeriod(self):
		self._currentTime+=1;

	def makePrincipalPayment(self, principalPayment, time):
		while 1:
			if self.notionalBalance()==0:
				logging.error('The notional balance is zero, no principal payment can be made.');
				break
			if self._principalHistory.get(time)!=None:
				logging.error('Sorry, make principal payment twice at the same time period is not allowed.')
				break
			# self._balance-=principalPayment;
			self._principalShort[time]=self.principalReceived()-principalPayment;
			self._principalHistory[time]=principalPayment;
			break

	def makeInterestPayment(self, interestPayment, time):
		while 1:
			if self.interestDue()==0:
				logging.error('The interest due is zero, no interest payment can be made.');
				break
			if self._interestHistory.get(time)!=None:
				logging.error('Sorry, make interest payment twice at the same time period is not allowed.')
				break
			self._interestShort[time]=self.interestDue()-interestPayment;
			self._interestHistory[time]=interestPayment;
			break

	def notionalBalance(self):
		sumOfPrincipal=sum(self._principalHistory.value());
		sumOfInterestShort=sum(self._interestShort.value());
		return float(self._face )- sumOfPrincipal + sumOfInterestShort

	def interestDue(self):
		return self.notionalBalance()*float(self._rate)

	def principalReceived(self):
		pass
		return self.monthlyPayment()-self.interestDue()


	def reset(self):
		self._principalHistory={};
		self._interestHistory={};
		self._interestShort={};
		self._principalShort={};
		self._currentTime=0

