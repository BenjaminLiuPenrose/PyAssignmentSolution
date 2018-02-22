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
				logging.error('The loan you are entering does not belong to class FixedRateLoan. \n');
		self._defaultProb=[0.0005 for i in range(1, 11)]+[0.001 for i in range(11, 60)]+[0.002 for i in range(60, 121)]
		self._defaultProb+=[0.004 for i in range(121, 181)]+[0.002 for i in range(181, 211)]+[0.001 for i in range(211, 361)]

	def __iter__(self):
		for l in self.loans:
			yield l
	@property
	def loans(self):
		return self._loans

	def ttlPrincipal(self):
		return sum(i.face for i in self._loans)
	def ttlBalance(self, period):
		return sum(i.balanceRecur(period) for i in self._loans)
	def ttlPrincipalDue(self, period):
		return sum(i.principalDueRecur(period) for i in self._loans if i.mode!='defaulted')
	def ttlInterestDue(self, period):
		return sum(i.interestDueRecur(period) for i in self._loans if i.mode!='defaulted')
	def ttlPaymentDue(self, period):
		return sum(i.monthlyPayment(period) for i in self._loans if i.mode!='defaulted')

	def activeLoan(self, period):
		return sum(1 for i in self._loans if i.balanceRecur(period)>0)

	def WAM(self):
		loanAmounts=[]; loanTerms=[]; I=[];
		for i in self._loans:
			loanAmounts.append(i._face);
			loanTerms.append(i._term);
			I.append(1.0);
		sumWeight=reduce(lambda total, (face, inden): total+(face*inden), zip(loanAmounts, I), 0)
		return reduce(lambda total, (face, term): total+(face*term), zip(loanAmounts, loanTerms), 0)/sumWeight

	def WAR(self):
		loanAmounts=[]; rates=[]; I=[];
		for i in self._loans:
			loanAmounts.append(i._face);
			rates.append(i.rate());
			I.append(1.0);
		sumWeight=reduce(lambda total, (face, inden): total+(face*inden), zip(loanAmounts, I), 0)
		return reduce(lambda total, (face, rate): total+(face*rate), zip(loanAmounts, rates), 0)/sumWeight

	# it returns list of lists and each list is of form [Interest Paid, Principal Paid, Recoveries, Total, Balance]
	def getWaterfall(self, period):
		waterfall=[];
		interestPaid_=0; principalPaid_=0; recoveryValue_=0; total_=0; balance_=0
		for l in self._loans:
			interestPaid=l.interestDueRecur(period) if l.mode!='defaulted' else 0
			principalPaid=l.principalDueRecur(period) if l.mode!='defaulted' else 0
			recoveryValue=l.recoveryValue(period) if l.mode=='defaulted' else 0
			balance=l.balanceRecur(period)
			interestPaid_+=interestPaid; principalPaid_+=principalPaid; recoveryValue_+=recoveryValue;
			total_+=interestPaid+principalPaid+recoveryValue; balance_+=balance
			# ls=[principalPaid, interestPaid, recoveryValue, interestPaid+principalPaid+recoveryValue, balance]
			# waterfall.append(ls);
		waterfall=[principalPaid_, interestPaid_, recoveryValue_, total_, balance_];
		return waterfall

	def checkDefaults(self, period):
		try :
			prob=self._defaultProb[period];
		except Exception as e:
			logging.exception('{}. The requested period should be less than 360.'.format(e)); return 0
		default=np.random.choice(2, len(self._loans), p=[prob, 1-prob]); 
		cnt=0; recoveryValue=0;
		for l in self._loans:
			recoveryValue+=l.checkDefault(default[cnt], period); cnt+=1;
		return recoveryValue