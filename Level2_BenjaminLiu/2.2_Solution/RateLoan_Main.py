# -*- coding: utf-8 -*- 
#!/usr/bin/env python
'''
Student name: Beier (Benjamin) Liu
Date:
Exercise 2.2

Remark:
Python 2.7 is recommended
Before running please install packages
Using cmd line py -2.7 -m install [package_name]
'''

'''===================================================================================================
File content:
As shown in the lecture, create derived classes as follows:
a. A FixedRateLoan class which derives from Loan.
b. A VariableRateLoan class which derives from Loan. This should have its own __init__ function 
that sets a _rateDict attribute on the object and then invokes the super-class’ __init__ function
Override the base-class rate function as follows:
==================================================================================================='''

class Asset(object):
	# Class init
	# Object init
	def __ini__(self):
		pass

	# Getter and setter
	@property
	def get(self):
		pass

	@get.setter
	def set(self, i):
		pass

	# Static method
	@staticmethod
	def myFunc():
		pass

	# Class method
	@classmethod
	def myFunct(cls):
		pass

	# Object-level method
	def funct():
		pass


def main():
	# Exercise xyz
	# Write comments
	print('\n====================================Exercise xyz=====================================\n');
	print('Running my myFunction function ... \n');
	myFunction();
	raw_input('Program pause. Press enter to continue.\n');

if __name__=='__main__':
	main()