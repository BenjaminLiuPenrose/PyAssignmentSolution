# -*- coding: utf-8 -*- 
#!/usr/bin/env python
'''
Student name: Beier (Benjamin) Liu
Date:
Project Part

Remark:
Python 2.7 is recommended
'''
import os, time, logging
import copy, math
import functools, itertools
import numpy as np 
from Implementations.Tranches.TrancheBase import *
from Implementations.Tranches.StandardTranche import *
from Implementations.Loans.LoanPool import *
from Implementations.Tools import *
logging.getLogger().setLevel(logging.DEBUG)
'''===================================================================================================
File content:
Write comments
==================================================================================================='''
class StructuredSecurity(object):
	def __init__(self,  *tranches, mode='Sequencial'):
		self._tranches=[];
		for t in tranches:
			if isinstance(t, StandardTranche):
				self._tranches.append(t);
			else :
				logging.error('The loan you are entering does not belong to class StandardTranche.');
		self._totalFace=sum(t.face for t in tranches)
		self._mode=mode.lower();
		self._reserveAccount=0;
		self._currentPeriod=0;

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
	def currentPeirod(self):
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
	def tranches(self):
		return self._tranches

	def addTranche(self, face, rate, subordination, trancheClass='StandardTranche'):
		tranche_new=StandardTranche(face=face, rate=rate, subordination=subordination);
		self._tranches.append(tranche_new)
	def increaseTimePeriod(self):
		for t in self._tranches:
			t.increaseTimePeriod();
		self._currentTime+=1;

	def makePayments(self, cashAmount, principalReceived):
		availableFunds=cashAmount+self._reserveAccount;
		availablePrincipals=principalReceived;
		sorted_tranches=sorted(self._tranches, key=lambda t: t.subordination)
		for t in sorted_tranches:
			interestDue=t.interestDue()
			if availableFunds > 0:
				interestPayment=min(interestDue, availableFunds);
				t.makeInterestPaymemt(interestPayment, self._currentPeriod)
				availableFunds-=interestPayment;
			else :
				t.makeInterestPaymemt(0, self._currentPeriod);

		for t in sorted_tranches:
			principalReceived=100 #
			priorPrincipalShort=t.principalShort[-1]
			balance=t.notionalBalance();
			if availableFunds > 0:
				if (self._mode=='sequencial'):
					principalPayment=min(availablePrincipals+priorPrincipalShort, balance, availableFunds)
					t.makePrincipalPayment(principalPayment, min(availablePrincipals+priorPrincipalShort, balance), self._currentPeriod)
				else : # (self._mode=='pro rata')
					principalPayment=min(availablePrincipals*percent+priorPrincipalShort, balance, availableFunds)
					t.makePrincipalPayment(principalPayment, min(availablePrincipals*percent+priorPrincipalShort, balance), self._currentPeriod)
				availableFunds-=principalPayment;	
				if availablePrincipals > 0:
					availablePrincipals-=min(principalPayment, availablePrincipals);
			else :
				t.makePrincipalPayment(0, min(availablePrincipals+priorPrincipalShort, balance), self._currentPeriod)

		if availableFunds >0 :
			self._reserveAccount+=availableFunds;	

	# it returns list of lists and each list is of form [Interest Due, Interest Paid, Interest Shortfall, Principal Paid, Balance]
	def getWaterfall(self):
		waterfall=[];
		sorted_tranches=sorted(self._tranches, key=lambda t: t.getSubord())
		for t in sorted_tranches:
			interestDue=t.interestDue()
			interestPaid=t.interestHistory[-1]
			principalPaid=t.principalHistory[-1]
			balance=t.notionalBalance()
			ls=[interestDue, interestPaid, interestDue-interestPaid, principalPaid, balance];
			waterfall.append(ls);
		return waterfall

def doWaterfall(loanPool, structuredSecurity):
	waterfall_s=[]; waterfall_l=[];
	while loanPool.activeLoan(structuredSecurity.currentPeriod)!=0 :
		structuredSecurity.increaseTimePeriod();
		recoveryValue=loanPool.checkDefaults(structuredSecurity.currentPeriod);
		totalPayment=loanPool.ttlPaymentDue(structuredSecurity.currentPeriod); 
		principalReceived=loanPool.ttlPrincipalDue(structuredSecurity.currentPeriod);
		totalPayment+=recoveryValue;
		structuredSecurity.makePayments(totalPayment, principalReceived);
		waterfall_s.append(structuredSecurity.getWaterfall()); 
		waterfall_l.append(loanPool.getWaterfall()); 
	IRR_s=[]; DIRR_s=[]; AL_s=[];
	for t in structuredSecurity.tranches:
		IRR_s.append(t.IRR());
		DIRR_s.append(t.DIRR());
		AL_s.append(t.AL());
	return waterfall_s, waterfall_l, structuredSecurity.getReserveAccount(), IRR_s, DIRR_s, AL_s

def simulateWaterfall(loanPool, structuredSecurity, NSIM):
	DIRR=[]; AL=[];
	for i in range(NSIM):
		_, _, _, _, dirr, al=doWaterfall(loanPool, structuredSecurity);
		DIRR.append(dirr); AL.append(al);
	DIRR_avg=[]; AL_avg=[];
	for i in range(len(DIRR[0])):
		dirr=[x[i] for x in DIRR]; 
		al=[x[i] for x in AL if x[i]!=None];
		DIRR_avg.append(sum(dirr)/float(len(dirr)));
		AL_avg.append(sum(al)/float(len(al))); 
	return DIRR_avg, AL_avg
