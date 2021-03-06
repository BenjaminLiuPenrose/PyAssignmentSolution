# -*- coding: utf-8 -*- 
#!/usr/bin/env python
'''
Student name: Beier (Benjamin) Liu
Date:
Exercise 2.2.5

Remark:
Python 2.7 is recommended
Before running please install packages
Using cmd line py -2.7 -m install [package_name]
'''
from Implementations.Loans.Loan import *
from Implementations.Loan.Loans import *
import logging
logging.getLogger().setLevel(logging.DEBUG)

'''===================================================================================================
File content:
# Exercise 2.2.5
# Create a LoanPool class that can contain and operate on a pool of loans (composition). Provide the 
# following functionality:
# a. A method to get the total loan principal.
# b. A method to get the total loan balance for a given period.
# c. Methods to get the aggregate principal, interest, and total payment due in a given period.
# d. A method that returns the number of ‘active’ loans. Active loans are loans that have a balance 
# greater than zero.
# e. Methods to calculate the Weighted Average Maturity (WAM) and Weighted Average Rate (WAR) of the 
# loans. You may port over the previously implemented global functions
==================================================================================================='''

# Exercise 2.2.5
class LoanPool(object):
	def __init__(self, *loan):
		self._loan=[];
		for l in loan:
			if isinstance(l, FixedRateLoan):
				self._loan.append(l);
			else :
				logging.error('The loan you are entering does not belong to class Loan. \n');

	@property
	def loan(self, number):
		try :
			self._loan[number];
			return self._loan[number];
		except Exception as e:
			logging.exception('{} \n'.format(e));
			logging.error('The index of loan you are choosing does not exist. \n');

	@loan.setter
	def loan(self, number, iLoan):
		try :
			self._loan[number]=iLoan;
		except Exception as e:
			logging.exception('{} \n'.format(e));
			logging.error('The index of loan you are choosing does not exist. \n');

	# a) A method to get the total loan principal.
	def ttlPrincipal(self):
		ttl=0;
		for i in self._loan:
			ttl+=self._loan[i].face
		return ttl

	# b) A method to get the total loan balance for a given period
	def ttlBalance(self, period):
		ttl=0;
		for i in self._loan:
			ttl+=self._loan[i].balanceRecur(period);
		return ttl 

	# c) Methods to get the aggregate principal, interest, and total payment due in a given period
	def ttlPrincipalDue(self, period):
		ttl=0;
		for i in self._loan:
			ttl+=self._loan[i].principalDueRecur(period);
		return ttl

	def ttlInterestDue(self):
		ttl=0;
		for i in self._loan:
			ttl+=self._loan[i].interestDueRecur(period);
		return ttl

	def ttlPaymentDue(self):
		ttl=;
		for i in self._loan:
			ttl+=self._loan[i].monthlyPayment(period);
		return ttl 

	# d) A method that returns the number of ‘active’ loans. Active loans are loans that have a balance 
	# greater than zero
	def activeLoan(self):
		pass

	# e) Methods to calculate the Weighted Average Maturity (WAM) and Weighted Average Rate (WAR) of the 
	# loans. You may port over the previously implemented global functions
	def WAM(self):
		loanAmounts=[]; loanTerms=[];
		for i in self._loan:
			loanAmounts.append(self._loan[i].face);
			loanTerms.append(self._loan[i].term);
		return reduce(lambda total, (face, term): total+(face*term), zip(loanAmounts, loanTerms), 0)

	def WAR(self):
		loanAmounts=[]; rates=[];
		for i in self._loan:
			loanAmounts.append(self._loan[i].face);
			rates.append(self._loan[i].rate);
		return reduce(lambda total, (face, rate): total+(face*rate), zip(loanAmounts, rates), 0)