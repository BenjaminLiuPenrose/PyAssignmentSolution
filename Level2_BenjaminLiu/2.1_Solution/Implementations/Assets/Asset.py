# -*- coding: utf-8 -*- 
#!/usr/bin/env python
'''
Student name: Beier (Benjamin) Liu
Date: 2/14/2018
Exercise 2.1.6 and 2.2.6

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
# d. Create a method that returns the current value of the asset, for a given period

Exercise 2.2.6
# This exercise focuses on creating the individual Asset derived classes. Do the following:
# a. Modify the annualDeprRate method of the Asset class to trigger a not-implemented error. This 
# ensures that no one can directly instantiate an Asset object (makes it abstract)
# b. Create a Car class, derived from Asset. Derive multiple car types from Car (i.e. Civic, 
# Lexus, Lamborghini, etc.). Give each one a different depreciation rate
# c. Create a HouseBase class, derived from Asset. Derive PrimaryHome and VacationHome from House
# Give each one a different depreciation rate (note, a vacation home will depreciate slower than 
# a primary home since it is often vacant)
==================================================================================================='''

# Exercise 2.1.6
class Asset(object):
	# a) Save an initial asset value upon object initialization (i.e. the initial value of a car)
	def __init__(self, initValue, yearlyDepre):
		self._initValue=initValue;
		self._yearlyDepre=yearlyDepre;

	# Getter and setter
	@property
	def initValue(self):
		return float(self._iniValue)

	@iniValue.setter
	def initValue(self, iIniValue):
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
	def yearlyToMonthly(yearlyDepre):
		return yearlyDepre/12.0

	# d) Create a method that returns the current value of the asset, for a given period. This is the initial 
	# value times total depreciation
	def getPresValue(self, period): # period is in months
		presValue=(1-self.yearlyToMonthly(self._yearlyDepre))**period;
		presValue*=self._initValue
		return presValue

# Exercise 2.2.6
# a) Modify the annualDeprRate method of the Asset class to trigger a not-implemented error. This 
# ensures that no one can directly instantiate an Asset object
class Asset2(object):
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
		raise UnimplementedError()

	@yearlyDepre.setter
	def yearlyDepre(self, iYearlyDepre):
		raise UnimplementedError()


	@staticmethod
	def yearlyToMonthly(yearlyDepre):
		return yearlyDepre/12.0

	def getPresValue(self, period): # period is in months
		presValue=(1-self.yearlyToMonthly(self._yearlyDepre))**period;
		presValue*=self._initValue
		return presValue

# b) Create a Car class, derived from Asset. Derive multiple car types from Car (i.e. Civic, 
# Lexus, Lamborghini, etc.). Give each one a different depreciation rate
class Car(Asset2):
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

class Car(Asset2):
	def __init__(self, initValue, carType='Civic', yearlyDepreDict={'Civic':0.20, 'Lexus':0.10, 'Lamborghini':0.05}):
		self._carType=carType;
		self._yearlyDepre=yearlyDepreDict.get(carType);
		super(Car, self).__init__(initValue);

# c) Create a HouseBase class, derived from Asset. Derive PrimaryHome and VacationHome from House
# Give each one a different depreciation rate (note, a vacation home will depreciate slower than 
# a primary home since it is often vacant)
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


