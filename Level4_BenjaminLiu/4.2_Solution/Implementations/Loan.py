# -*- coding: utf-8 -*- 
#!/usr/bin/env python
'''
Student name: Beier (Benjamin) Liu
Date:
Exercise 4.2.3

Remark:
Python 2.7 is recommended
Before running please install packages
Using cmd line py -2.7 -m install [package_name]
'''

'''===================================================================================================
File content:
# Exercise 4.2.3 implementations
# Add logging statements to your Loan class. This should consist of the following:
# a. Anytime an exception is thrown (i.e., when an incorrect Asset type is passed-into the 
# initialization function), log an error prior to raising the exception.
# b. Debug-level logs which display interim steps of calculations and return values for the Loan functions.
# c. Info-level logs to display things like ‘t is greater than term’ in the loan functions.
# d. At the point the exception is caught (in your main function) use logging.exception to display 
# the exception in addition to a custom message.
# e. Add a warn log to the recursive versions of the waterfall functions (that they are expected 
# to take a long time, so the explicit versions are recommended).
==================================================================================================='''

# Create a basic Loan class
# Input principal is face value
# convRate is the proper interest rate, such as monthly interest rate calculated from APR
# numPeriods is the term of the loan, for example 6 months loan the number is 6
class Loan(object):
	# Initialization
	def __init__(self, principal, convRate, numPeriods):
		self._principal=principal;
		self._convRate=convRate; # converted proper interest rates, such as the monthly interest rate from APR
		self._numPeriods=numPeriods;

	# Getter and setter
	@property
	def principal(self):
		return float(self._principal);

	@principal.setter
	def principal(self, iPrincipal):
		self._principal=iPrincipal;

	@property
	def convRate(self):
		return float(self._convRate);

	@convRate.setter
	def convRate(self, iConvRate):
		self._convRate=iConvRate;

	@property
	def numPeriods(self):
		return float(self._numPeriods);

	@numPeriods.setter
	def set(self, iNumPeriods):
		self._numPeriods=iNumPeriods;

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
		return float((face*rate))/(1-(1+rate)**(-term));

	@classmethod
	def calcBalance(cls, face, rate, term, period):
		return face*((1+rate)**period)- \
		cls.calcMonthlyPmt(face, rate, term)*((1+rate)**period-1)/rate;

	# Object-level methods
	def monthlyPayment(self, period): #period is dummy variable
		rate=Loan.monthlyRate(self._convRate*12);
		pmt=float((self._principal*rate))/(1-(1+rate)**(-self._numPeriods));
		return pmt 

	def totalPayments(self, period): 
		pmt=self.monthlyPayment(period);
		pmtTtl=pmt*self._numPeriods;
		return pmtTtl

	def totalInterest(self):
		rate=Loan.monthlyRate(self._convRate*12);
		instTtl=self._principal*rate*self._numPeriods;
		return instTtl

	def interestDueFoml(self, period):
		if period<=self._numPeriods();
		rate=Loan.monthlyRate(self._convRate*12);
		instDue=self.balanceFoml(period-1)*rate;
		return instDue 

	def principalDueFoml(self, period):
		principalDue=self.balanceFoml(period-1)-self.balanceFoml(period);
		return principalDue

	def balanceFoml(self, period): 
		rate=Loan.monthlyRate(self._convRate*12);
		balance=self._principal*((1+rate)**period)- \
		self.monthlyPayment(period)*((1+rate)**period-1)/rate
		return balance 

	def interestDueRecur(self, period): 
		rate=Loan.monthlyRate(self._convRate*12);
		return self.balanceRecur(period-1)*rate

	def principalDueRecur(self, period): 
		return self.monthlyPayment(period)-self.interestDueRecur(period)

	def balanceRecur(self, period):
		if period==0:
			return self._principal
		else :
			return self.balanceRecur(period-1)-self.principalDueRecur(period)

	def monthlyPayment2(self, period): #period is dummy variable 
		rate=Loan.monthlyRate(self._convRate*12);
		pmt=self.calcMonthlyPmt(self._principal, rate, self._numPeriods);
		return pmt 




