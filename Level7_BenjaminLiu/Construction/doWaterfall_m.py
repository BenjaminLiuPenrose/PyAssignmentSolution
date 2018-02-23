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
Write comments
==================================================================================================='''

'''===================================================================================================
Implementation for Part1.4, 3.5
==================================================================================================='''
def doWaterfall(loanPool, structuredSecurity):
	waterfall_tranches=[]; waterfall_loans=[]; reserveAccount_structuredSecurity=[]
	while loanPool.activeLoan(structuredSecurity.currentPeriod)!=0 :
		logging.debug('The remaining number of active loans is {}'.format(loanPool.activeLoan(structuredSecurity.currentPeriod)))
		structuredSecurity.increaseTimePeriod();
		recoveryValue=loanPool.checkDefaults(structuredSecurity.currentPeriod);
		totalPayment=loanPool.ttlPaymentDue(structuredSecurity.currentPeriod); 
		principalReceived=loanPool.ttlPrincipalDue(structuredSecurity.currentPeriod);
		totalPayment+=recoveryValue;
		structuredSecurity.makePayments(totalPayment, principalReceived);
		waterfall_tranches.append(structuredSecurity.getWaterfall()); 
		waterfall_loans.append(loanPool.getWaterfall(structuredSecurity.currentPeriod)); 
		reserveAccount_structuredSecurity.append(structuredSecurity.reserveAccount)
	IRR_tranches=[]; DIRR_tranches=[]; WAL_tranches=[]; 
	sort=sorted(structuredSecurity.tranches, key=lambda t: t.subordination); balance_to_al=sort[0].notionalBalance()
	for t in structuredSecurity.tranches:
		IRR_tranches.append(t.IRR());
		DIRR_tranches.append(t.DIRR());
		WAL_tranches.append(t.AL(balance_to_al));
	return {'Waterfall Tranches':waterfall_tranches, 'Waterfall Loans':waterfall_loans, 'Reserve Account':reserveAccount_structuredSecurity, \
	'IRR tranches':IRR_tranches, 'DIRR tranches':DIRR_tranches, 'WAL tranches':WAL_tranches}

