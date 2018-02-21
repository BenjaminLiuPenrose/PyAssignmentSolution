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
from Implementations.Loans.LoanBase import *
from Implementations.Assets.Car import *
logging.getLogger().setLevel(logging.DEBUG)

'''===================================================================================================
File content:

==================================================================================================='''

class AutoLoan(Loan):
	def __init__(self, auto, face, rate, term):
		if isinstance(auto, Car):
			self._auto=auto;
		else :
			self._auto=Car(face); 	
			logging.error('The entered auto does not belong to Car. \n');
		super(AutoLoan, self).__init__(self._auto, face, rate, term)