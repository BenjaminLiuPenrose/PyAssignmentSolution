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
logging.getLogger().setLevel(logging.DEBUG)

'''===================================================================================================
File content:
Write comments
==================================================================================================='''

'''===================================================================================================
Implementation for Part3 Multiprocessing 
==================================================================================================='''
@Timer
def simulateWaterfallParallel(loanPool, structuredSecurity, NSIM, numProcess):
	input_queue=multiprocessing.Queue()
	output_queue=multiprocessing.Queue()

	for i in range(numProcess): 
		input_queue.put((simulateWaterfall, (loanPool, structuredSecurity, NSIM/numProcess)))
	
	process_handler=[];
	for i in range(numProcess):
		p=multiprocessing.Process(target=doWork, args=(input_queue, output_queue))
		p.start(); process_handler.append(p)
	
	DIRR=[]; WAL=[]; cnt=0;
	while cnt< numProcess:
		cnt+=1; logging.info('Running simulateWaterfall {} time'.format(cnt))
		res =output_queue.get()
		if cnt==1:
			DIRR=res.get('DIRR tranches'); WAL=res.get('WAL tranches');
		else :
			DIRR=[DIRR_t+DIRR[t] for t, DIRR_t in enumerate(res.get('DIRR tranches'))]
			WAL=[WAL_t+WAL[t] for t, WAL_t in enumerate(res.get('WAL tranches'))]
			# DIRR.append(res.get('DIRR tranches')); WAL.append(res.get('WAL tranches'));

	input_queue.close(); output_queue.close();
	for p in process_handler:
		p.terminate()
	logging.debug('Finishing simulateWaterfallParallel Part.');
	logging.debug('After mutiprocessing, DIRR list is {}'.format(DIRR))
	logging.debug('simulateWF: The DIRR is {} and the WAL is {}'.format(DIRR, WAL))

	DIRR=[DIRR_t/float(numProcess) for DIRR_t in DIRR]
	WAL=[WAL_t/float(numProcess) for WAL_t in WAL]

	# DIRR_avg=[]; AL_avg=[]; # DIRR_avg=DIRR; AL_avg=AL;
	# for i in range(len(DIRR[0])):
	# 	dirr=[x[i] for x in DIRR]; 
	# 	al=[x[i] for x in AL if x[i]!=None];
	# 	DIRR_avg.append(sum(dirr)/float(len(dirr)));
	# 	AL_avg.append(sum(al)/float(len(al)) if len(al)!=0 else None); 
	return {'DIRR tranches':DIRR, 'WAL tranches':WAL}

def doWork(input, output):
	while 1:
		try :
			func, args=input.get(timeout=3);
			res=func(*args)
			output.put(res)
		except Exception as e:
			logging.exception('Error message: {}'.format(e));
			break