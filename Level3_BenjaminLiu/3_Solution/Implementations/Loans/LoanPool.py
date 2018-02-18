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
from Implementations.Loans.Loans import *
import logging
logging.getLogger().setLevel(logging.DEBUG)

'''===================================================================================================
File content:

==================================================================================================='''

class LoanPool(object):
	# init
	def __init__(self, *loan):
		self._loan=[];
		for l in loan:
			if isinstance(l, FixedRateLoan):
				self._loan.append(l);
			else :
				logging.error('The loan you are entering does not belong to class Loan. \n');

	def __iter__(self):
		for l in self.loan:
			yield l;

	# getter and setter
	@property
	def loan(self, number=None):
		if number!=None:
			try :
				self._loan[number];
				return self._loan[number];
			except Exception as e:
				logging.exception('{} \n'.format(e));
				logging.error('The index of loan you are choosing does not exist. \n');
		else :
			return self._loan

	@loan.setter
	def loan(self, iLoan, number=None):
		if number!=None:
			try :
				self._loan[number]=iLoan;
			except Exception as e:
				logging.exception('{} \n'.format(e));
				logging.error('The index of loan you are choosing does not exist. \n');
		else :
			try :
				logging.warning('You are trying to replace all loans in LoanPool. \n');
				self._loan=iLoan
			except Exception as e:
				logging.exception('{} \n'.format(e));
				logging.error('In order to replace the LoanPool, please enter a list of Loan objects. \n');


	# object-level method
	def ttlPrincipal(self):
		ttl=0;
		for i in self.loan:
			ttl+=i.face
		return ttl

	def ttlBalance(self, period):
		ttl=0;
		for i in self.loan:
			ttl+=i.balanceRecur(period);
		return ttl 

	def ttlPrincipalDue(self, period):
		ttl=0;
		for i in self.loan:
			ttl+=i.principalDueRecur(period);
		return ttl

	def ttlInterestDue(self, period):
		ttl=0;
		for i in self.loan:
			ttl+=i.interestDueRecur(period);
		return ttl

	def ttlPaymentDue(self, period):
		ttl=0;
		for i in self.loan:
			ttl+=i.monthlyPayment(period);
		return ttl 

	def activeLoan(self, period):
		active=0;
		for i in self.loan:
			if i.balanceRecur(period)>0:
				active+=1;
		return active

	def WAM(self):
		loanAmounts=[]; loanTerms=[]; I=[];
		for i in self.loan:
			loanAmounts.append(i.face);
			loanTerms.append(i.term);
			I.append(1.0);
		sumWeight=reduce(lambda total, (face, inden): total+(face*inden), zip(loanAmounts, I), 0)
		return reduce(lambda total, (face, term): total+(face*term), zip(loanAmounts, loanTerms), 0)/sumWeight

	def WAR(self):
		loanAmounts=[]; rates=[];
		for i in self.loan:
			loanAmounts.append(i.face);
			rates.append(i.rate(period=1));
		sumWeight=reduce(lambda total, (face, inden): total+(face*inden), zip(loanAmounts, I), 0)
		return reduce(lambda total, (face, rate): total+(face*rate), zip(loanAmounts, rates), 0)/sumWeight