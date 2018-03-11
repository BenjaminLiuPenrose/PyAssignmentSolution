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

	@memoize
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
					percent_dict={'A':0.8, 'B':0.2}; percent=percent_dict.get(t.subordination);
					principalPayment=min(availablePrincipals*percent+priorPrincipalShort, balance, availableFunds)
					t.makePrincipalPayment(principalPayment, min(availablePrincipals*percent+priorPrincipalShort, balance), self._currentPeriod)
				availableFunds-=principalPayment;	
				if availablePrincipals > 0:
					availablePrincipals-=min(principalPayment, availablePrincipals);
			else :
				t.makePrincipalPayment(0, min(availablePrincipals+priorPrincipalShort, balance), self._currentPeriod)

		if availableFunds >0 :
			self._reserveAccount+=availableFunds;	
		return self

	# it returns list of lists and each list is of form [Interest Due, Interest Paid, Interest Shortfall, Principal Paid, Balance]
	#@memoize
	def getWaterfall(self):
		waterfall=[];
		sorted_tranches=sorted(self._tranches, key=lambda t: t.subordination)
		for t in sorted_tranches:
			interestDue=t.interestDueHist[-1]
			interestPaid=t.interestHistory[-1]
			principalPaid=t.principalHistory[-1]
			balance=t.balance[-1]
			ls=[interestDue, interestPaid, interestDue-interestPaid, principalPaid, balance];
			waterfall.append(ls);
		return waterfall

	def reset(self):
		for t in self._tranches:
			t.reset();
		self._reserveAccount=0;
		self._currentPeriod=0;	

'''===================================================================================================
Implementation for Part1.4, 3.5
==================================================================================================='''
def doWaterfall(loanPool, structuredSecurity):
	waterfall_s=[]; waterfall_l=[]; reserveAccount_s=[]; structuredSecurity.reset(); loanPool.reset();
	while loanPool.activeLoan(structuredSecurity.currentPeriod)!=0 :
		logging.debug('The remaining number of active loans is {}'.format(loanPool.activeLoan(structuredSecurity.currentPeriod)))
		structuredSecurity.increaseTimePeriod();
		recoveryValue=loanPool.checkDefaults(structuredSecurity.currentPeriod);
		totalPayment=loanPool.ttlPaymentDue(structuredSecurity.currentPeriod); 
		principalReceived=loanPool.ttlPrincipalDue(structuredSecurity.currentPeriod);
		totalPayment+=recoveryValue;
		structuredSecurity=structuredSecurity.makePayments(totalPayment, principalReceived);
		waterfall_s.append(structuredSecurity.getWaterfall()); 
		waterfall_l.append(loanPool.getWaterfall(structuredSecurity.currentPeriod)); 
		reserveAccount_s.append(structuredSecurity.reserveAccount)
	IRR_s=[]; DIRR_s=[]; AL_s=[]; balance_to_al=1;
	for t in structuredSecurity.tranches:
		if t.subordination=='A':
			balance_to_al=t.notionalBalance()
		IRR_s.append(t.IRR());
		DIRR_s.append(t.DIRR());
		AL_s.append(t.AL(balance_to_al));
	logging.debug('doWaterfall: The DIRR is {} and the AL is {}'.format(DIRR_s, AL_s))
	return waterfall_s, waterfall_l, reserveAccount_s, IRR_s, DIRR_s, AL_s

'''===================================================================================================
Implementation for Part3 MC1
==================================================================================================='''
@Timer
def simulateWaterfall(loanPool, structuredSecurity, NSIM):
	DIRR=[]; AL=[];
	for i in range(NSIM):
		logging.info('Running doWaterfall {} time'.format(i+1))
		_, _, _, _, dirr, al=doWaterfall(loanPool, structuredSecurity);
		DIRR.append(dirr); AL.append(al);
	DIRR_avg=[]; AL_avg=[];
	for i in range(len(DIRR[0])):
		dirr=[x[i] for x in DIRR]; 
		al=[x[i] for x in AL if x[i]!=None];
		DIRR_avg.append(sum(dirr)/float(len(dirr)));
		AL_avg.append(sum(al)/float(len(al)) if len(al)!=0 else None); 
	logging.info('simulateWaterfall: The DIRR is {} and the AL is {}'.format(DIRR_avg, AL_avg))
	return DIRR_avg, AL_avg

'''===================================================================================================
Implementation for Part3 Multiprocessing 
==================================================================================================='''
@Timer
def simulateWaterfallParallel(loanPool, structuredSecurity, NSIM, numProcess):
	input_queue=multiprocessing.Queue()
	output_queue=multiprocessing.Queue()

	for i in range(numProcess): 
		input_queue.put((simulateWaterfall, (loanPool, structuredSecurity, NSIM/numProcess)))
	
	process_handler=[]
	for i in range(numProcess):
		p=multiprocessing.Process(target=doWork, args=(input_queue, output_queue))
		p.start(); process_handler.append(p)
	
	DIRR=[]; AL=[]; cnt=0;
	while cnt< numProcess:
		cnt+=1; logging.info('Running simulateWaterfall {} time'.format(cnt))
		res =output_queue.get()
		DIRR.append(res[0]);
		AL.append(res[1]);

	logging.debug('Finishing simulateWaterfallParallel Part.');
	input_queue.close(); output_queue.close();
	for p in process_handler:
		p.terminate()
	logging.debug('After mutiprocessing, DIRR list is {}'.format(DIRR))
	logging.debug('simulateWF: The DIRR is {} and the AL is {}'.format(DIRR, AL))
	DIRR_avg=[]; AL_avg=[]; # DIRR_avg=DIRR; AL_avg=AL;
	for i in range(len(DIRR[0])):
		dirr=[x[i] for x in DIRR]; 
		al=[x[i] for x in AL if x[i]!=None];
		DIRR_avg.append(sum(dirr)/float(len(dirr)));
		AL_avg.append(sum(al)/float(len(al)) if len(al)!=0 else None); 
	return DIRR_avg, AL_avg

def doWork(input, output):
	while 1:
		try :
			func, args=input.get(timeout=3);
			dirr, al=func(*args)
			output.put([dirr, al])
		except Exception as e:
			logging.exception('Error message: {}'.format(e));
			break

'''===================================================================================================
Implementation for Part3 MC2
==================================================================================================='''
'''===================================================================================================
Implementation for Part3 Multiprocessing 
==================================================================================================='''
@Timer
def runMonte(loanPool, structuredSecurity, NSIM=2000, tol=0.005, numProcess=None): # idea: convert diff to inner product of notional and percentage change
	cnt=0; rate=[]
	while 1:
		cnt+=1; logging.info('Running simulateWaterfallParallel {} time'.format(cnt))
		if numProcess==None:
			DIRR, AL=simulateWaterfall(loanPool, structuredSecurity, NSIM);
		else :
			DIRR, AL=simulateWaterfallParallel(loanPool, structuredSecurity, NSIM, numProcess);
		logging.debug('runMonte: The DIRR is {} and the AL is {}'.format(DIRR, AL))
		Yield=[calculateYield(dirr, al) for dirr,al in zip(DIRR, AL)];
		percentChg=[]; coeff_dict={'A':1.2, 'B':0.8};
		for idx, t in enumerate(structuredSecurity.tranches):
			coeff=coeff_dict.get(t.subordination);
			oldRate=t.rate*12.0;
			newRate=oldRate+coeff*(Yield[idx]-oldRate);
			t.rate=newRate; 
			chg=abs(oldRate-newRate)/oldRate;
			logging.info('The oldRate is {}, the newRate is {}, the Yield is {}, the chg is {}'.format(oldRate, newRate, Yield[idx], chg))
			percentChg.append(chg);
		notional=[t.face for t in structuredSecurity.tranches]
		ttlNotional=float(sum(notional));
		diff=reduce(lambda total, (notional, percentChg): total+(notional*percentChg), zip(notional, percentChg), 0)
		diff=diff/ttlNotional;
		logging.info('runMonte: The diff is {} and the new rate is {}'.format(diff, [t.rate for t in structuredSecurity.tranches]))
		if diff < tol:
			rate=[t.rate*12.0 for t in structuredSecurity.tranches]
			break
	return rate


def calculateYield(DIRR, AL):
	if AL==None:
		return 0
	r=7/(1+0.08*exp(-0.19/12.0*AL));
	r+=0.019*sqrt(AL/12.0*DIRR*100);
	r=r/100.0;
	logging.info('calculateYield: The DIRR is {}, the AL is {} and the yield is {}'.format(DIRR, AL, r))
	return r

'''===================================================================================================
Implementation for Part2 toLetterRating
==================================================================================================='''
def toLetterRating(DIRR):
	DIRR*=10000.0;
	letter=['Aaa','Aa1','Aa2','Aa3','A1','A2','A3','Baa1','Baa2','Baa3','Ba1','Ba2','Ba3','B1','B2','B3','Caa','Ca'];
	threshold=[0.06, 0.67,1.3,2.7,5.2,8.9,13.0,19.0,27.0,46.0,72.0,106.0,143.0,183.0,231.0,311.0,2500.0,10000.0];
	letter_rate='C';
	cnt=0;
	while 1:
		if DIRR < 0:
			letter_rate='N/A';
			break
		if DIRR <= threshold[cnt]:
			letter_rate=letter[cnt];
			break
		cnt+=1;
	return letter_rate