# -*- coding: utf-8 -*- 
#!/usr/bin/env python
'''
Student name: Beier (Benjamin) Liu
Date: 

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
class Asset(object):
	def __init__(self, initValue, recoveryMult):
		self._initValue=initValue;
		self._recoveryMult=recoveryMult;

	@property
	def initValue(self):
		return self._initValue
	@initValue.setter
	def initValue(self, iInitValue):
		self._initValue=iInitValue;

	@property
	def recoveryMult(self):
		return self._recoveryMult
	@recoveryMult.setter
	def recoveryMult(self, iMult):
		self._recoveryMult=iMult;

	@property
	def yearlyDepre(self):
		raise NotImplementedError()
	@yearlyDepre.setter
	def yearlyDepre(self, iYearlyDepre):
		raise NotImplementedError()

	@staticmethod
	def yearlyToMonthly(yearlyDepre):
		return yearlyDepre/12.0


	def getPresValue(self, period): 
		presValue=(1-self.yearlyToMonthly(self.yearlyDepre))**period;
		presValue*=self.initValue
		return presValue