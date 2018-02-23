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
from doWaterfall_m import *
logging.getLogger().setLevel(logging.DEBUG)

'''===================================================================================================
File content:
Write comments
==================================================================================================='''

'''===================================================================================================
Implementation for Part3 MC1
==================================================================================================='''
@Timer
def simulateWaterfall(loanPool, structuredSecurity, NSIM):
	DIRR=[]; WAL=[]; 
	for i in range(NSIM):
		logging.debug('Running doWaterfall {} time'.format(i+1))
		res=doWaterfall(loanPool, structuredSecurity);
		if i+1==1:
			DIRR=res.get('DIRR tranches'); WAL=res.get('WAL tranches');
		else :
			DIRR=[DIRR_t+DIRR[t] for t, DIRR_t in enumerate(res.get('DIRR tranches'))]
			WAL=[WAL_t+WAL[t] for t, WAL_t in enumerate(res.get('WAL tranches'))]
		# DIRR.append(res.get('DIRR tranches')); WAL.append(res.get('WAL tranches'));
	DIRR=[DIRR_t/float(NSIM) for DIRR_t in DIRR]
	WAL=[WAL_t/float(NSIM) for WAL_t in WAL]
	# DIRR_avg=[]; WAL_avg=[];
	# for i in range(len(DIRR[0])):
	# 	dirr=[x[i] for x in DIRR]; 
	# 	al=[x[i] for x in AL if x[i]!=None];
	# 	DIRR_avg.append(sum(dirr)/float(len(dirr)));
	# 	AL_avg.append(sum(al)/float(len(al)) if len(al)!=0 else None); 
	return {'DIRR tranches':DIRR, 'WAL tranches':WAL}
