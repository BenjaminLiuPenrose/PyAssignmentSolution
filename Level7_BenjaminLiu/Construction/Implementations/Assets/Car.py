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
from Implementations.Assets.AssetBase import *
logging.getLogger().setLevel(logging.DEBUG)
'''===================================================================================================
File content:

==================================================================================================='''
class Car(Asset):
	@property
	def yearlyDepre(self):
		return self._yearlyDepre;
	@yearlyDepre.setter
	def yearlyDepre(self, iYearlyDepre):
		self._yearlyDepre=iYearlyDepre;

class Civic(Car):
	def __init__(self, initValue, recoveryMult=0.40, yearlyDepre=0.12):
		self._yearlyDepre=yearlyDepre;
		super(Civic, self).__init__(initValue, recoveryMult);

class Lexus(Car):
	def __init__(self, initValue, recoveryMult=0.60, yearlyDepre=0.10):
		self._yearlyDepre=yearlyDepre;
		super(Lexus, self).__init__(initValue, recoveryMult);

class Lamborghini(Car):
	def __init__(self, initValue, recoveryMult=0.60, yearlyDepre=0.05):
		self._yearlyDepre=yearlyDepre;
		super(Lamborghini, self).__init__(initValue, recoveryMult);