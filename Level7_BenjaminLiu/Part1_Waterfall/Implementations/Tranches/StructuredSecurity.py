# -*- coding: utf-8 -*- 
#!/usr/bin/env python
'''
Student name: Beier (Benjamin) Liu
Date:
Project Part

Remark:
Python 2.7 is recommended
Before running please install packages *numpy
Using cmd line py -2.7 -m install [package_name]
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
	def __init__(self,  mode='Sequencial', *tranches):
		self._tranches=[];
		for t in tranches:
			if isinstance(t, StandardTranche):
				self._tranches.append(t);
			else :
				logging.error('The loan you are entering does not belong to class Loan. \n');
		self._totalFace=sum(t.face for t in tranches)
		self._mode=mode.lower();
		self._reserveAccount=0;
		self._currentTime=0;

	def __iter__(self):
		for t in self._tranches:
			yield t

	@property
	def tranches(self):
		return self._tranches;

	def getReserveAccount(self):
		return self._reserveAccount

	def getCurrentTime(self):
		return self._currentTime


	def addTranche(self, face, rate, subordinate, trancheClass='StandardTranche'):
		tranche_new=StandardTranche(face=face, rate=rate, subordinate=subordinate);
		self._tranches.append(tranche_new)

	def flagMode(self, flag):
		if flag.lower()=='sequencial' or flag.lower()=='pro rata':
			self._mode=flag.lower();
		else :
			logging.error('Please use Sequencial or Pro Rata as param for flagMode().');

	def increaseTimePeriod(self):
		for t in self._tranches:
			t.increaseTimePeriod();
		self._currentTime+=1;

	def makePayments(self, cashAmount):
		availableFunds=cashAmount+self._reserveAccount;
		sorted_tranches=sorted(self._tranches, key=lambda t: t.getSubord())
		for t in sorted_tranches:
			interestDue=t.interestDue()
			if availableFunds >= interestDue:
				t.makeInterestPaymemt(interestDue, t.getCurrentTime());
				availableFunds-=interestDue;
			elif (availableFunds > 0 and availableFunds < interestDue):
				t.makeInterestPaymemt(availableFunds, t.getCurrentTime());
				availableFunds-=availableFunds;
			else :
				t.makeInterestPaymemt(0, t.getCurrentTime());

		for t in sorted_tranches:
			while (availableFunds>0):
				principalReceived=t.principalReceived() #
				balance=t.notionalBalance();
				priorPrincipalShort=t.getPrincipalShort().get(t.getCurrentTime()-1);
				if (self._mode=='sequencial'):
					principalPayment=min(principalReceived+priorPrincipalShort, availableFunds, balance)
				else : # (self._mode=='pro rata')
					principalPayment=min(principalReceived*percent+priorPrincipalShort, availableFunds, balance)

				t.makePrincipalPayment(principalPayment, t.getCurrentTime())
				availableFunds-=principalPayment;	

		if availableFunds >0 :
			self._reserveAccount+=availableFunds;			



	def getWaterfall(self):
		# list of lists and each list is of form [Interest Due, Interest Paid, Interest Shortfall, Principal Paid, Balance]
		waterfall=[];
		sorted_tranches=sorted(self._tranches, key=lambda t: t.getSubord())
		for t in sorted_tranches:
			ls=list(t.interestDue(), t.getInterestHistory().get(t.getCurrentTime()), t.getInterestShort().get(t.getCurrentTime()),\
			t.getPrincipalHistory(t.getCurrentTime()), t.notionalBalance());
			waterfall.append(ls);
		return waterfall


def doWaterfall(loanPool, structuredSecurity): # doWaterfall function to return the metrics after the Waterfall completes
	waterfall_s=[]; waterfall_l=[];
	while all(True for loan in loanPool.loans if loan.face>0 else False):
		structuredSecurity.increaseTimePeriod();
		recoveryValue=loanPool.checkDefaults(structuredSecurity.getCurrentTime());
		totalPayment=loanPool.totalPayment(structuredSecurity.getCurrentTime()); #
		totalPayment+=recoveryValue;
		structuredSecurity.makePayments(totalPayment);
		waterfall_s.append(structuredSecurity.getWaterfall()); 
		waterfall_l.append(loanPool.getWaterfall()); #
	return waterfall_s, waterfall_l, structuredSecurity.getReserveAccount()#, IRR, DIRR, AL

def simulateWaterfall(loanPool, structuredSecurity, NSIM):
	DIRR=[]; AL=[];
	for i in range(NSIM):
		_, _, _, _, dirr, al=doWaterfall(loanPool, structuredSecurity);
		DIRR.append(dirr); AL.append(al);
	DIRR_avg=sum(DIRR)/float(len(DIRR))
	AL=[AL for al in AL if AL!=None];
	AL_avg=sum(AL)/float(len(AL)); #
	return DIRR_avg, AL_avg # The function should return the average DIRR and WAL values for each tranche.

def runMonte(loanPool, structuredSecurity, NSIM, tol):
	while 1:
		DIRR, WAL=simulateWaterfall(loanPool, structuredSecurity, MSIM);
		Yield=calculateYield(DIRR, WAL);
		for t in structuredSecurity.tranches:
			coeff=0.8
			if t.getSubord()=='A':
				coeff=1.2
			oldrate=t.rate;
			t.rate=t.rate+coeff*(Yield-t.rate);
		page 11;
		if diff < tol:
			break









def calculateYield(DIRR, WAL):
	r=7/(1+0.8*exp(-0.19/12.0*WAL));
	r+=0.19*sqrt(WAL/12.0*DIRR*100);
	r=r/100.0;
	return r





		# if (self._mode=='Sequencial'):
		# 	for t in sorted_tranches:
		# 		if availableFunds <= 0:
		# 			break
		# 		principalReceived=t.principalReceived()
		# 		balance=t.notionalBalance();
		# 		priorPrincipalShort=t.getPrincipalShort().get(t.getCurrentTime()-1);
		# 		principalPayment=min(principalReceived+priorPrincipalShort, availableFunds, balance)

		# 		t.makePrincipalPayment(principalPayment, t.getCurrentTime())
		# 		availableFunds-=principalPayment;
		# else :
		# 	for t in sorted_tranches:
		# 		if availableFunds <= 0:
		# 			break
		# 		principalReceived=t.principalReceived()
		# 		balance=t.notionalBalance();
		# 		priorPrincipalShort=t.getPrincipalShort().get(t.getCurrentTime()-1);
		# 		principalPayment=min(principalReceived*percent+priorPrincipalShort, availableFunds, balance)

		# 		t.makePrincipalPayment(principalPayment, t.getCurrentTime())
		# 		availableFunds-=principalPayment;