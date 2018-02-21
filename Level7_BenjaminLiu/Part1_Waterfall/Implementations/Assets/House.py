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
'''===================================================================================================
File content:

==================================================================================================='''

class HouseBase(Asset):
	pass
	# def __init__(self, initValue):
	# 	super(HouseBase, self).__init__()

class PrimaryHome(HouseBase):
	def __init__(self, initValue, yearlyDepre=0.20):
		self._yearlyDepre=yearlyDepre;
		super(HouseBase, self).__init__(initValue);

class VacationHome(HouseBase):
	def __init__(self, initValue, yearlyDepre=0.05):
		self._yearlyDepre=yearlyDepre;
		super(HouseBase, self).__init__(initValue);