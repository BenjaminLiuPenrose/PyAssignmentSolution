# -*- coding: utf-8 -*- 
#!/usr/bin/env python
'''
Student name: Beier (Benjamin) Liu
Date: 2/14/2018
Exercise 

Remark:
Python 2.7 is recommended
'''

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