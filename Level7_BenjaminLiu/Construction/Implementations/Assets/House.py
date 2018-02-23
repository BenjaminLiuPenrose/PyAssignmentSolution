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
class HouseBase(Asset):
	@property
	def yearlyDepre(self):
		return self._yearlyDepre;
	@yearlyDepre.setter
	def yearlyDepre(self, iYearlyDepre):
		self._yearlyDepre=iYearlyDepre;

class PrimaryHome(HouseBase):
	def __init__(self, initValue, recoveryMult=0.60, yearlyDepre=0.20):
		self._yearlyDepre=yearlyDepre;
		super(HouseBase, self).__init__(initValue, recoveryMult);

class VacationHome(HouseBase):
	def __init__(self, initValue, recoveryMult=0.60, yearlyDepre=0.05):
		self._yearlyDepre=yearlyDepre;
		super(HouseBase, self).__init__(initValue, recoveryMult);