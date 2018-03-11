# -*- coding: utf-8 -*- 
#!/usr/bin/env python
'''
Student name: Beier (Benjamin) Liu
Date: 2/22/2018
Project Part 1.2

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
from Implementations.Tools import *
logging.getLogger().setLevel(logging.DEBUG)

'''===================================================================================================
File content:
class StandardTranche
==================================================================================================='''

'''===================================================================================================
Implementation for Part1.2
==================================================================================================='''
class StandardTranche(Tranche):
	def increaseTimePeriod(self):
		self._currentPeriod+=1;

	#@memoize
	def makePrincipalPayment(self, principalPayment, principalDue, period):
		while 1:
			if self.notionalBalance()==0 and principalPayment!=0 :
				logging.error('The notional balance is zero, no principal payment can be made.');
				break
			if len(self._principalHistory)>=period+1 and principalPayment!=0 :
				logging.error('Sorry, make principal payment twice at the same time period is not allowed.')
				break
			self._principalShort.append(round(principalDue-principalPayment, 6));
			self._principalHistory.append(round(principalPayment, 6));
			break
		return self
	#@memoize
	def makeInterestPayment(self, interestPayment, period):
		while 1:
			if self.interestDue()==0 and interestPayment!=0:
				logging.error('The interest due is zero, no interest payment can be made.');
				break
			if len(self._interestHistory)>=period+1 and interestPayment!=0:
				logging.error('Sorry, make interest payment twice at the same time period is not allowed.')
				break
			self._interestDueHist.append(round(self.interestDue(), 6));
			self._interestShort.append(round(self.interestDue()-interestPayment, 6));
			self._interestHistory.append(round(interestPayment, 6));
			break
		return self
	#memoize
	def notionalBalance(self):
		sumOfPrincipal=sum(self._principalHistory);
		sumOfInterestShort=sum(self._interestShort);
		return float(self._face)- sumOfPrincipal + sumOfInterestShort
	#memoize
	def interestDue(self):
		return self.notionalBalance()*self._rate+self._interestShort[-1]

	def reset(self):
		self._currentPeriod=0;
		self._principalHistory=[0];
		self._interestHistory=[0];
		self._principalShort=[0];
		self._interestShort=[0];
		self._interestDueHist=[0];
		self._balance=[self._face];

