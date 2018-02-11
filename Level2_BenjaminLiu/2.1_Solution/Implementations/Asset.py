# -*- coding: utf-8 -*- 
#!/usr/bin/env python
'''
Student name: Beier (Benjamin) Liu
Date:
Exercise 2.1

Remark:
Python 2.7 is recommended
Before running please install packages
Using cmd line py -2.7 -m install [package_name]
'''

'''===================================================================================================
File content:
# Exercise 2.1.6
# Create a class called Asset. This class will represent the Asset covered by the loan. The class 
# should do the following:
# a. Save an initial asset value upon object initialization (i.e. the initial value of a car).
# b. Create a method that returns a yearly depreciation rate (i.e., 10%).
# c. Create a method that calculates the monthly depreciation rate, from the yearly depreciation rate.
# d. Create a method that returns the current value of the asset, for a given period. This is the initial 
# value times total depreciation. Total depreciation at time t can be calculated as:
==================================================================================================='''

# Exercise 2.1.6
class Asset(object):
	# a) Save an initial asset value upon object initialization (i.e. the initial value of a car)
	def __ini__(self):
		self._iniValue=initValue;
		self._yearlyDepre=yearlyDepre;

	# Getter and setter
	@property
	def iniValue(self):
		return float(self._iniValue)

	@iniValue.setter
	def iniValue(self, iIniValue):
		self._iniValue=iIniValue;

	# b) Create a method that returns a yearly depreciation rate
	@property
	def yearlyDepre(self):
		return float(self._yearlyDepre)

	@yearlyDepre.setter
	def yearlyDepre(self, iYearlyDepre):
		self._yearlyDepre=iYearlyDepre


	# c)  Create a method that calculates the monthly depreciation rate, from the yearly depreciation rate
	@staticmethod
	def monthlyToYearly(yearlyDepre):
		return yearlyDepre/12.0

	# d) Create a method that returns the current value of the asset, for a given period. This is the initial 
	# value times total depreciation
	def getPresValue(self, period):
		presValue=(1-self.monthlyToYearly(self.getYearlyDepre()))**period;
		presValue*=self._iniValue
		return presValue

