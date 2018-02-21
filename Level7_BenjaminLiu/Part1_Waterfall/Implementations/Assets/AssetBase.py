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
'''===================================================================================================
File content:

==================================================================================================='''

class Asset(object):
	def __init__(self, initValue):
		self._initValue=initValue;

	# Getter and setter
	@property
	def initValue(self):
		return float(self._initValue)

	@initValue.setter
	def initValue(self, iInitValue):
		self._initValue=iInitValue;

	@property # this is the annualDeprRate required by question
	def yearlyDepre(self):
		raise NotImplementedError()

	@yearlyDepre.setter
	def yearlyDepre(self, iYearlyDepre):
		raise NotImplementedError()


	@staticmethod
	def yearlyToMonthly(yearlyDepre):
		return yearlyDepre/12.0

	def getPresValue(self, period): # period is in months
		presValue=(1-self.yearlyToMonthly(self.yearlyDepre))**period;
		presValue*=self.initValue
		return presValue