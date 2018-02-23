# -*- coding: utf-8 -*- 
#!/usr/bin/env python
'''
Student name: Beier (Benjamin) Liu
Date: 2/22/2018
Project Part 1.3, 1.4, Part 3.5, 3 MC1, 3 MC2, 3 Multiprocessing

Remark:
Python 2.7 is recommended
'''
import os, time, logging
from math import exp, sqrt
import functools, itertools
import numpy as np 
from Implementations.Tranches.TrancheBase import *
from Implementations.Tranches.StandardTranche import *
from Implementations.Loans.LoanPool import *
from Implementations.Tools import *
logging.getLogger().setLevel(logging.DEBUG)
'''===================================================================================================
File content:
class StructuredSecurity
global function doWaterfall, simulateWaterfall, simulateWaterfallParallel, runMonte, calculateYield, toLetterRating
==================================================================================================='''

'''===================================================================================================
Implementation for Part1.3
==================================================================================================='''
class StructuredSecurity(object):
	def __init__(self, totalFace, mode='Sequencial'):
		self._totalFace=totalFace;
		self._mode=mode.lower();
		self._reserveAccount=0;
		self._currentPeriod=0;
		self._tranches=[];

	def __iter__(self):
		for t in self._tranches:
			yield t

	@property
	def mode(self):
		return self._mode
	@mode.setter
	def mode(self, imode):
		if imode.lower()=='sequential' or imode.lower()=='pro rata':
			self._mode=imode;
		else :
			logging.error('Please use Sequencial or Pro Rata as param for mode setter.');
	@property
	def currentPeriod(self):
		return self._currentPeriod
	@currentPeriod.setter
	def currentPeriod(self, icurrentPeriod):
		self._currentPeriod=icurrentPeriod;
	@property
	def reserveAccount(self):
		return self._reserveAccount
	@reserveAccount.setter
	def reserveAccount(self, ireserve):
		self._reserveAccount=ireserve;
	@property
	def totalFace(self):
		return self._totalFace
	@totalFace.setter
	def totalFace(self, itotalFace):
		self._totalFace=itotalFace;
	@property
	def tranches(self):
		return self._tranches

	def addTranche(self, percentNotional, rate, subordination, trancheClass='StandardTranche'):
		tranche_new=StandardTranche(face=self._totalFace*percentNotional, rate=rate, subordination=subordination);
		self._tranches.append(tranche_new)
	def increaseTimePeriod(self):
		for t in self._tranches:
			t.increaseTimePeriod();
		self._currentPeriod+=1;

	def makePayments(self, cashAmount, principalReceived):
		availableFunds=cashAmount+self._reserveAccount;
		availablePrincipals=principalReceived;
		sorted_tranches=sorted(self._tranches, key=lambda t: t.subordination)
		logging.debug('The first sorted tranche is {}'.format(sorted_tranches[0].subordination))
		for t in sorted_tranches:
			interestDue=t.interestDue()
			if availableFunds > 0:
				interestPayment=min(interestDue, availableFunds);
				t.makeInterestPayment(interestPayment, self._currentPeriod)
				availableFunds-=interestPayment;
			else :
				t.makeInterestPayment(0, self._currentPeriod);

		for t in sorted_tranches:
			priorPrincipalShort=t.principalShort[-1]
			balance=t.notionalBalance();
			t.balance.append(round(balance, 6));
			if availableFunds > 0:
				if (self._mode=='sequencial'):
					principalPayment=min(availablePrincipals+priorPrincipalShort, balance, availableFunds)
					t.makePrincipalPayment(principalPayment, min(availablePrincipals+priorPrincipalShort, balance), self._currentPeriod)
				else : # in this case, self._mode=='pro rata'
					percent_dict={'A':0.8, 'B':0.2}; percent=percent_dict.get(t.subordination, 0.2);
					principalPayment=min(availablePrincipals*percent+priorPrincipalShort, balance, availableFunds)
					t.makePrincipalPayment(principalPayment, min(availablePrincipals*percent+priorPrincipalShort, balance), self._currentPeriod)
				availableFunds-=principalPayment;	
				if availablePrincipals > 0:
					availablePrincipals-=min(principalPayment, availablePrincipals);
			else :
				t.makePrincipalPayment(0, min(availablePrincipals+priorPrincipalShort, balance), self._currentPeriod)

		if availableFunds >0 :
			self._reserveAccount+=availableFunds;	

	# it returns list of dicts and each list is of form [Interest Due, Interest Paid, Interest Shortfall, Principal Paid, Balance]
	def getWaterfall(self):
		waterfall=[];
		for t in self._tranches:
			interestDue=t.interestDueHist[-1]
			interestPaid=t.interestHistory[-1]
			principalPaid=t.principalHistory[-1]
			balance=t.balance[-1]
			waterfall_tranche={'Interest Due': interestDue, 'Interest Paid':interestPaid, 'Interest Shortfall':interestDue-interestPaid, \
			'Principal Paid':principalPaid, 'Balance':balance};
			waterfall.append(waterfall_tranche);
		return waterfall