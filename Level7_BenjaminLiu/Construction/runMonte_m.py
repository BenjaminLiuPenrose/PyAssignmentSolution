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
from simulateWaterfall_m import *
from simulateWaterfallParallel_m import *
logging.getLogger().setLevel(logging.DEBUG)

'''===================================================================================================
File content:
Write comments
==================================================================================================='''

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
			res=simulateWaterfall(loanPool, structuredSecurity, NSIM);
		else :
			res=simulateWaterfallParallel(loanPool, structuredSecurity, NSIM, numProcess);
		DIRR=res.get('DIRR tranches'); WAL=res.get('WAL tranches');
		logging.debug('runMonte: The DIRR is {} and the WAL is {}'.format(DIRR, WAL))
		Yield=[calculateYield(dirr, wal) for dirr,wal in zip(DIRR, WAL)];
		percentChg=[]; coeff_dict={'A':1.2, 'B':0.8, 'C':0.8};
		for idx, t in enumerate(structuredSecurity.tranches):
			coeff=coeff_dict.get(t.subordination);
			oldRate=t.rate*12.0;
			newRate=oldRate+coeff*(Yield[idx]-oldRate);
			t.rate=newRate; 
			chg=abs(oldRate-newRate)/oldRate;
			logging.debug('The oldRate is {}, the newRate is {}, the Yield is {}, the chg is {}'.format(oldRate, newRate, Yield[idx], chg))
			percentChg.append(chg);
		notional=[t.face for t in structuredSecurity.tranches];
		diff=reduce(lambda total, (notional, percentChg): total+(notional*percentChg), zip(notional, percentChg), 0);
		diff=diff/float(sum(notional));
		logging.info('runMonte: The diff is {} and the new rates are {}'.format(diff, [t.rate*12.0 for t in structuredSecurity.tranches]))
		if diff < tol:
			rate=[t.rate*12.0 for t in structuredSecurity.tranches]
			break
	return {'rate':rate, 'diff':diff, 'NSIM': NSIM, 'numProcess': numProcess}

def calculateYield(DIRR, WAL):
	logging.debug('calculateYield: The DIRR is {} and the AL is {}'.format(DIRR, WAL))
	if WAL==None:
		logging.info('calculateYield: The input WAL is None.')
		return 0
	r=7/(1+0.08*exp(-0.19/12.0*WAL));
	r+=0.019*sqrt(WAL/12.0*DIRR*100);
	r=r/100.0;
	return r