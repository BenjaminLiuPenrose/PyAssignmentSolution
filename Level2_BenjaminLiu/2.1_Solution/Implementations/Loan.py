# -*- coding: utf-8 -*- 
#!/usr/bin/env python
'''
Student name: Beier (Benjamin) Liu
Date:
Exercise 1.2.2 - 1.2.4

Remark:
Python 2.7 is recommended
Before running please install packages
Using cmd line py -2.7 -m install [package_name]
'''

'''===================================================================================================
File content:
# Exercise 2.1.2
# Create a basic Loan class exactly as demonstrated in the lecture (including the setter/getter property methods). 
# Then, extend it with methods that return the following (refer to the slides for any necessary formulas):
# a. The monthly payment amount of the Loan (monthlyPayment). Even though monthlyPayment is likely to be equal for 
# all months, you should still define this with a dummy ‘period’ parameter, since it’s possible some loan types will 
# have a monthly payment dependent on the period.
# b. The total payments of the Loan (totalPayments). This is principal plus interest.
# c. The total interest of the Loan (totalInterest).

# Exercise 2.1.3
# Interest due at time T on a loan depends on the outstanding balance. Principal due is the monthly payment 
# less the interest due. Conceptually, these are recursive calculations as one can determine the interest/principal 
# due at time T if one knows the balance at time T-1 (which, in turn, can be determined if one knows the balance 
# at time T-2).
# For each of the below functions, implement two versions: A recursive version (per the above statement) and a 
# version that uses the formulas provided in the slides:
# a. The interest amount due at a given period (interestDue).
# b. The principal amount due at a given period (principalDue).
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
# Input principal is face value
# convRate is the proper interest rate, such as monthly interest rate calculated from APR
# numPeriods is the term of the loan, for example 6 months loan the number is 6
class Loan(object):
	def __init__(self, principal, convRate, numPeriods):
		self._principal=principal;
		self._convRate=convRate; # converted proper interest rates, such as the monthly interest rate from APR
		self._numPeriods=numPeriods;

	# Exercise 2.1.2 implementation
	# Getter and setter for attributes _principal, _convRate, _numPeriods
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
	def numPeriods(self, iNumPeriods):
		self._numPeriods=iNumPeriods;

	# a) Add a method to compute monthly payment
	# Rmk: The basic equation: A = (P*i)/1-(1+i)^-n
	def monthlyPayment(self, period): #period is dummy variable
		pmt=float((self._principal*self._convRate))/(1-(1+self._convRate)**(-self._numPeriods));
		return pmt 

	# b) Add a method to compute total payment
	# Rmk: The total payments of the Loan (totalPayments). This is principal plus interest
	def totalPayments(self, period):
		pmt=self.monthlyPayment(period);
		pmtTtl=pmt*self._numPeriods;
		return pmtTtl

	# c) Add a method to compute total interest
	# Rmk: The total interest of the Loan (totalInterest) 
	def totalInterest(self):
		instTtl=self._principal*self._convRate*self._numPeriods;
		return instTtl

	# Exercise 2.1.3 implementation
	# Formulas calculations version implementation of the following three methods
	# a) The interest amount due at a given period (interestDue)
	# b) The principal amount due at a given period (principalDue)
	# c) The balance of the loan at a given period (balance)
	def interestDueFoml(self, period):
		instDue=self.balanceFoml(period-1)*self._convRate;
		return instDue 

	def principalDueFoml(self, period):
		principalDue=self.balanceFoml(period-1)-self.balanceFoml(period);
		return principalDue

	def balanceFoml(self, period):
		balance=self._principal*((1+self._convRate)**period)- \
		self.monthlyPayment(period)*((1+self._convRate)**period-1)/self._convRate
		return balance 

	# Recursive version implementation of the following three methods
	# a) The interest amount due at a given period (interestDue)
	# b) The principal amount due at a given period (principalDue)
	# c) The balance of the loan at a given period (balance)
	def interestDueRecur(self, period):
		return self.balanceRecur(period-1)*self._convRate

	def principalDueRecur(self, period):
		return self.monthlyPayment(period)-self.interestDueRecur(period)

	def balanceRecur(self, period):
		if period==0:
			return self._principal
		else :
			return self.balanceRecur(period-1)-self.principalDueRecur(period)

	# Exercise 2.1.4 implementation
	# a) Implement a class-level method called calcMonthlyPmt, in the Loan base class. This should calculate a monthly 
	# payment based on three parameters: face, rate, and term
	@classmethod
	def calcMonthlyPmt(cls, face, rate, term):
		return float((face*rate))/(1-(1+rate)**(-term));

	# b) Create a class-level function, in the Loan base class, which calculates the balance (calcBalance). Input 
	# parameters should be face, rate, term, period
	@classmethod
	def calcBalance(cls, face, rate, term, period):
		return face*((1+rate)**period)- \
		cls.calcMonthlyPmt(face, rate, term)*((1+rate)**period-1)/rate;

	# d) Modify the object-level methods for monthlyPayment and balance to delegate to the class-level methods
	def monthlyPayment2(self, period): #period is dummy variable 
		pmt=self.calcMonthlyPmt(self._principal, self._convRate, self._numPeriods);
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

	# d) Modify all the Loan methods that rely on the rate to utilize the static-level rate functions
	# Create a new class Loan2 to implement this idea
class Loan2(object):
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

	def totalPayments(self, period): #this method no rate is involved
		pmt=self.monthlyPayment(period);
		pmtTtl=pmt*self._numPeriods;
		return pmtTtl

	def totalInterest(self):
		rate=Loan.monthlyRate(self._convRate*12);
		instTtl=self._principal*rate*self._numPeriods;
		return instTtl

	def interestDueFoml(self, period):
		rate=Loan.monthlyRate(self._convRate*12);
		instDue=self.balanceFoml(period-1)*rate;
		return instDue 

	def principalDueFoml(self, period): #this method no rate is involved
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

	def principalDueRecur(self, period): #this method no rate is involved
		return self.monthlyPayment(period)-self.interestDueRecur(period)

	def balanceRecur(self, period): #this method no rate is involved
		if period==0:
			return self._principal
		else :
			return self.balanceRecur(period-1)-self.principalDueRecur(period)

	def monthlyPayment2(self, period): #period is dummy variable 
		rate=Loan.monthlyRate(self._convRate*12);
		pmt=self.calcMonthlyPmt(self._principal, rate, self._numPeriods);
		return pmt 




