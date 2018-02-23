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

class Car(Asset):
	pass

class Civic(Car):
	def __init__(self, initValue, yearlyDepre=0.20):
		self._yearlyDepre=yearlyDepre;
		super(Civic, self).__init__(initValue);

class Lexus(Car):
	def __init__(self, initValue, yearlyDepre=0.10):
		self._yearlyDepre=yearlyDepre;
		super(Lexus, self).__init__(initValue);

class Lamborghini(Car):
	def __init__(self, initValue, yearlyDepre=0.05):
		self._yearlyDepre=yearlyDepre;
		super(Lamborghini, self).__init__(initValue);

# Depreciated class Car
# class Car2(Asset):
# 	def __init__(self, initValue, carType='Civic', yearlyDepreDict={'Civic':0.20, 'Lexus':0.10, 'Lamborghini':0.05}):
# 		self._carType=carType;
# 		self._yearlyDepre=yearlyDepreDict.get(carType);
# 		super(Car, self).__init__(initValue);
