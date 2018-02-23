# -*- coding: utf-8 -*- 
#!/usr/bin/env python
'''
Student name: Beier (Benjamin) Liu
Date: 2/14/2018
Exercise 

Remark:
Python 2.7 is recommended
'''
import os, time, logging
import copy, math
import functools, itertools
import numpy as np 
from Implementations.Loans.LoanBase import *
logging.getLogger().setLevel(logging.DEBUG)

'''===================================================================================================
File content:

==================================================================================================='''

class LoanPool(object):
	def __init__(self, *loan):
		self._loans=[];
		for l in loan:
			if isinstance(l, FixedRateLoan):
				self._loan.append(l);
			else :
				logging.error('The loan you are entering does not belong to class Loan. \n');
		self._defaultProb=[0.0005 for i in range(1, 11)]+[0.001 for i in range(11, 60)]+[0.002 for i in range(60, 121)]+[0.004 for i in range(121, 181)]+[0.002 for i in range(181, 211)]+[0.001 for i in range(211, 361)]

	def __iter__(self):
		for l in self.loans:
			yield l;

	@property
	def loans(self, number=None):
		if number!=None:
			try :
				self._loans[number];
				return self._loans[number];
			except Exception as e:
				logging.exception('{} \n'.format(e));
				logging.error('The index of loan you are choosing does not exist. \n');
		else :
			return self._loans

	@loans.setter
	def loans(self, iLoan, number=None):
		if number!=None:
			try :
				self._loans[number]=iLoan;
			except Exception as e:
				logging.exception('{} \n'.format(e));
				logging.error('The index of loan you are choosing does not exist. \n');
		else :
			try :
				logging.warning('You are trying to replace all loans in LoanPool. \n');
				self._loans=iLoan
			except Exception as e:
				logging.exception('{} \n'.format(e));
				logging.error('In order to replace the LoanPool, please enter a list of Loan objects. \n');

	def ttlPrincipal(self):
		ttl=0;
		for i in self.loans:
			ttl+=i.face
		return ttl

	def ttlBalance(self, period):
		ttl=0;
		for i in self.loans:
			ttl+=i.balanceRecur(period);
		return ttl 

	def ttlPrincipalDue(self, period):
		ttl=0;
		for i in self.loans:
			ttl+=i.principalDueRecur(period);
		return ttl

	def ttlInterestDue(self, period):
		ttl=0;
		for i in self.loans:
			ttl+=i.interestDueRecur(period);
		return ttl

	def ttlPaymentDue(self, period):
		ttl=0;
		for i in self.loans:
			ttl+=i.monthlyPayment(period);
		return ttl 

	def activeLoan(self, period):
		active=0;
		for i in self.loans:
			if i.balanceRecur(period)>0:
				active+=1;
		return active

	def WAM(self):
		loanAmounts=[]; loanTerms=[]; I=[];
		for i in self.loans:
			loanAmounts.append(i.face);
			loanTerms.append(i.term);
			I.append(1.0);
		sumWeight=reduce(lambda total, (face, inden): total+(face*inden), zip(loanAmounts, I), 0)
		return reduce(lambda total, (face, term): total+(face*term), zip(loanAmounts, loanTerms), 0)/sumWeight

	def WAR(self):
		loanAmounts=[]; rates=[];
		for i in self.loans:
			loanAmounts.append(i.face);
			rates.append(i.rate(period=1));
		sumWeight=reduce(lambda total, (face, inden): total+(face*inden), zip(loanAmounts, I), 0)
		return reduce(lambda total, (face, rate): total+(face*rate), zip(loanAmounts, rates), 0)/sumWeight

	def getWaterfall(self):
		# list of lists and each list is of form [Interest Due, Interest Paid, Interest Shortfall, Principal Paid, Balance]
		waterfall=[];
		sorted_tranches=sorted(self._tranches, key=lambda t: t.getSubord())
		for t in sorted_tranches:
			ls=list(t.interestDue(), t.getInterestHistory().get(t.getCurrentTime()), t.getInterestShort().get(t.getCurrentTime()),\
			t.getPrincipalHistory(t.getCurrentTime()), t.notionalBalance());
			waterfall.append(ls);
		return waterfall

	def checkDefaults(self, time):
		prob=self._defaultProb[time];
		default=np.random.choice(2, len(self.loans), p=[prob, 1-prob]); cnt=0; recoveryValue=0;
		for l in self.loans:
			recoveryValue+=l.checkDefault(default[cnt]); cnt+=1;
		return recoveryValue
		