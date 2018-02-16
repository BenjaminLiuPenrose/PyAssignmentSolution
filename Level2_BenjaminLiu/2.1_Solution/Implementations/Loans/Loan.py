# -*- coding: utf-8 -*- 
#!/usr/bin/env python
'''
Student name: Beier (Benjamin) Liu
Date: 2/14/2018
Exercise 1.2.2 - 1.2.5

Remark:
Python 2.7 is recommended
'''
from Implementations.Assets.Asset import *
import logging
logging.getLogger().setLevel(logging.DEBUG)

'''===================================================================================================
File content:
# Exercise 2.1.2
# Create a basic Loan class exactly as demonstrated in the lecture (including the setter/getter property methods). 
# Then, extend it with methods that return the following (refer to the slides for any necessary formulas):
# a. The monthly payment amount of the Loan (monthlyPayment). Even though monthlyPayment is likely to be equal for 
# all months, you should still define this with a dummy ‘period’ parameter, since it’s possible some loan types will 
# have a monthly payment dependent on the period.
# b. The total payments of the Loan (totalPayments). This is face plus interest.
# c. The total interest of the Loan (totalInterest).

# Exercise 2.1.3
# Interest due at time T on a loan depends on the outstanding balance. face due is the monthly payment 
# less the interest due. Conceptually, these are recursive calculations as one can determine the interest/face 
# due at time T if one knows the balance at time T-1 (which, in turn, can be determined if one knows the balance 
# at time T-2).
# For each of the below functions, implement two versions: A recursive version (per the above statement) and a 
# version that uses the formulas provided in the slides:
# a. The interest amount due at a given period (interestDue).
# b. The face amount due at a given period (faceDue).
# c. The balance of the loan at a given period (balance).
# Use your Timer class to time each version of each function; what do you observe? What happens as the time period increases?

# Exercise 2.1.4
# To demonstrate understanding of class-level methods, do the following:
# a. Implement a class-level method called calcMonthlyPmt, in the Loan base class. This should calculate a monthly 
# payment based on three parameters: face, rate, and term.
# b. Create a class-level function, in the Loan base class, which calculates the balance (calcBalance). Input 
# parameters should be face, rate, term, period.
# c. Test the class-level methods in main.
# d. Modify the object-level methods for monthlyPayment and balance to delegate to the class-level methods.
# e. Test the object-level methods to ensure they still work correctly.
# f. What are the benefits of class-level methods? When are they useful?

# Exercise 2.1.5
# To demonstrate understanding of static-level methods, do the following:
# a. Create a static-level method in Loan called monthlyRate. This should return the monthly interest 
# rate for a passed-in annual rate
# b. Create another static-level method that does the opposite (returns an annual rate for a passed-in monthly rate).
# c. Test the static-level method in main.
# d. Modify all the Loan methods that rely on the rate to utilize the static-level rate functions.
# e. What are the benefits of static-level methods? When are they useful?
==================================================================================================='''

# Create a basic Loan class
# Input face is face value
# rate is the proper interest rate, such as monthly interest rate calculated from APR
# term is the term of the loan, for example 6 months loan the number is 6
class Loan(object):
	def __init__(self, asset, face, rate, term):
		if isinstance(asset, Asset2):
			self._asset=asset;
		else :
			logging.error('The entered asset is not of type Asset. \n');
		self._face=face;
		if isinstance(rate, (int, float)) :
			self._rate=rate/12;
		else :
			self._rate=0.05; # _rate is the monthly interest rate, _term is the  number of months
		self._term=term;

	# Exercise 2.1.2 implementation
	# Getter and setter for attributes _face, _rate, _term
	@property
	def face(self):
		return float(self._face);

	@face.setter
	def face(self, iface):
		self._face=iface;

	@property
	def rate(self):
		return float(self._rate);

	@rate.setter
	def rate(self, irate):
		self._rate=irate;

	@property
	def term(self):
		return float(self._term);

	@term.setter
	def term(self, iterm):
		self._term=iterm;

	@property
	def asset(self):
		return self._asset

	@asset.setter
	def asset(self, iasset):
		self._asset=iasset

	# a) Add a method to compute monthly payment
	# Rmk: The basic equation: A = (P*i)/1-(1+i)^-n
	def monthlyPayment(self, period): #period is dummy variable
		pmt=float((self._face*self._rate))/(1-(1+self._rate)**(-self._term));
		return pmt 

	# b) Add a method to compute total payment
	# Rmk: The total payments of the Loan (totalPayments). This is face plus interest
	def totalPayments(self, period):
		pmt=self.monthlyPayment(period);
		pmtTtl=pmt*self._term;
		return pmtTtl

	# c) Add a method to compute total interest
	# Rmk: The total interest of the Loan (totalInterest) 
	def totalInterest(self):
		instTtl=float(self._face*self._rate*self._term);
		return instTtl

	# Exercise 2.1.3 implementation
	# Formulas calculations version implementation of the following three methods
	# a) The interest amount due at a given period (interestDue)
	# b) The face amount due at a given period (faceDue)
	# c) The balance of the loan at a given period (balance)
	def interestDueFoml(self, period):
		instDue=self.balanceFoml(period-1)*self._rate;
		return instDue 

	def principalDueFoml(self, period):
		faceDue=self.balanceFoml(period-1)-self.balanceFoml(period);
		return faceDue

	def balanceFoml(self, period):
		balance=self._face*((1+self._rate)**period)- \
		self.monthlyPayment(period)*((1+self._rate)**period-1)/self._rate
		return balance 

	# Recursive version implementation of the following three methods
	# a) The interest amount due at a given period (interestDue)
	# b) The face amount due at a given period (faceDue)
	# c) The balance of the loan at a given period (balance)
	def interestDueRecur(self, period):
		return self.balanceRecur(period-1)*self._rate

	def principalDueRecur(self, period):
		return self.monthlyPayment(period)-self.interestDueRecur(period)

	def balanceRecur(self, period):
		if period==0:
			return self._face
		else :
			return self.balanceRecur(period-1)-self.principalDueRecur(period)

	# Exercise 2.1.4 implementation
	# a) Implement a class-level method called calcMonthlyPmt, in the Loan base class. This should calculate a monthly 
	# payment based on three parameters: face, rate, and term
	@classmethod
	def calcMonthlyPmt(cls, face, rate, term):
		rate=rate/12.0;
		return float((face*rate))/(1-(1+rate)**(-term));

	# b) Create a class-level function, in the Loan base class, which calculates the balance (calcBalance). Input 
	# parameters should be face, rate, term, period
	@classmethod
	def calcBalance(cls, face, rate, term, period):
		rate=rate/12.0;
		return face*((1+rate)**period)- \
		cls.calcMonthlyPmt(face, rate, term)*((1+rate)**period-1)/rate;

	# d) Modify the object-level methods for monthlyPayment and balance to delegate to the class-level methods
	def monthlyPayment2(self, period): #period is dummy variable 
		pmt=self.calcMonthlyPmt(self._face, self._rate, self._term);
		return pmt 

	# Exercise 2.1.5 implementation
	# a) Create a static-level method in Loan called monthlyRate. This should return the monthly interest 
	# rate for a passed-in annual rate
	@staticmethod
	def monthlyRate(ATR):
		return float(ATR)/12

	# b) Create another static-level method that does the opposite (returns an annual rate for a passed-in monthly rate)
	@staticmethod
	def annualRate(monthlyRte):
		return float(monthlyRte)*12

	def recoveryValue(self, period):
		recoveryMult=0.60;
		return self._asset.getPresValue(period)*recoveryMult

	def equity(self, period):
		return self._asset.getPresValue(period)-self.balanceRecur(period) 


	# d) Modify all the Loan methods that rely on the rate to utilize the static-level rate functions
	# Create a new class Loan2 to implement this idea
class Loan2(object):
	# Initialization
	def __init__(self, asset, face, rate, term):
		if isinstance(asset, Asset2):
			self._asset=asset;
		else :
			logging.error('The input asset is not of type Asset. \n');
		self._face=face;
		if isinstance(rate, (int, float)) :
			self._rate=Loan2.monthlyRate(rate);
		else :
			self._rate=0.05; # _rate is the monthly interest rate, _term is the  number of months # _rate is the monthly interest rate, _term is the  number of months
		self._term=term;

	# Getter and setter
	@property
	def face(self):
		return float(self._face);

	@face.setter
	def face(self, iface):
		self._face=iface;

	@property
	def rate(self):
		return float(self._rate);

	@rate.setter
	def rate(self, irate):
		self._rate=irate;

	@property
	def term(self):
		return float(self._term);

	@term.setter
	def set(self, iterm):
		self._term=iterm;

	@property
	def asset(self):
		return self._asset

	@asset.setter
	def asset(self, iasset):
		self._asset=iasset

	# Static methods
	@staticmethod
	def monthlyRate(ATR):
		return float(ATR)/12

	@staticmethod
	def annualRate(monthlyRte):
		return float(monthlyRte)*12

	# Class methods
	@classmethod
	def calcMonthlyPmt(cls, face, rate, term):
		rate=monthlyRate(rate)
		return float((face*rate))/(1-(1+rate)**(-term));

	@classmethod
	def calcBalance(cls, face, rate, term, period):
		rate=monthlyRate(rate)
		return face*((1+rate)**period)- \
		cls.calcMonthlyPmt(face, rate, term)*((1+rate)**period-1)/rate;

	# Object-level methods
	def monthlyPayment(self, period): #period is dummy variable
		pmt=float((self._face*self._rate))/(1-(1+self._rate)**(-self._term));
		return pmt 

	def totalPayments(self, period): #this method no rate is involved
		pmt=self.monthlyPayment(period);
		pmtTtl=pmt*self._term;
		return pmtTtl

	def totalInterest(self):
		instTtl=self._face*self._rate*self._term;
		return instTtl

	def interestDueFoml(self, period):
		instDue=self.balanceFoml(period-1)*self._rate;
		return instDue 

	def principalDueFoml(self, period): #this method no rate is involved
		faceDue=self.balanceFoml(period-1)-self.balanceFoml(period);
		return faceDue

	def balanceFoml(self, period): 
		balance=self._face*((1+self._rate)**period)- \
		self.monthlyPayment(period)*((1+self._rate)**period-1)/self._rate
		return balance 

	def interestDueRecur(self, period): 
		return self.balanceRecur(period-1)*self._rate

	def principalDueRecur(self, period): #this method no rate is involved
		return self.monthlyPayment(period)-self.interestDueRecur(period)

	def balanceRecur(self, period): #this method no rate is involved
		if period==0:
			return self._face
		else :
			return self.balanceRecur(period-1)-self.principalDueRecur(period)

	def monthlyPayment2(self, period): #period is dummy variable 
		pmt=self.calcMonthlyPmt(self._face, self._rate, self._term);
		return pmt 

	def recoveryValue(self, period):
		recoveryMult=0.60;
		return self._asset.getPresValue(period)*recoveryMult

	def equity(self, period):
		return self._asset.getPresValue(period)-self.balanceRecur(period) 


