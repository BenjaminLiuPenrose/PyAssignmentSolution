# -*- coding: utf-8 -*- 
#!/usr/bin/env python
'''
Student name: Beier (Benjamin) Liu
Date: 2/14/2018
Exercise 

Remark:
Python 2.7 is recommended
'''
from Implementations.Loans.Loan import *
import logging
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