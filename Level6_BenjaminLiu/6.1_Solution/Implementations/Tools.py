# -*- coding: utf-8 -*- 
#!/usr/bin/env python
'''
Student name: Beier (Benjamin) Liu
Date:
Exercise

Remark:
Python 2.7 is recommended
Before running please install packages *numpy
Using cmd line py -2.7 -m install [package_name]
'''
import os, time, logging
import copy, math
import functools, itertools
import numpy as np 
import multiprocessing
logging.getLogger().setLevel(logging.DEBUG)

'''===================================================================================================
File Content:
Timer, memoize, multiProcess
==================================================================================================='''

def Timer(func):
	@functools.wraps(func)
	def wrapped(*args, **kwargs):
		s=time.time()
		res=func(*args, **kwargs);
		e=time.time()
		logging.info('{}: {} seconds.'.format(func, e-s))
		return res
	return wrapped

def memoize(func):
    memo = {}
    @functools.wraps(func)
    def wrapped(*args):
        if args not in memo:            
            memo[args] = func(*args)
        return memo[args]
    return wrapped 


@Timer
def multiProcess(process_num, func, *args):
	input_queue=multiprocessing.Queue()
	output_queue=multiprocessing.Queue()

	for i in range(len(args[0])):
		input_queue.put((func, tuple([x[i] for x in args])))

	for i in range(process_num):
		multiprocessing.Process(target=doWork, args=(input_queue, output_queue)).start()

	res=[];
	# freq=np.zeros((max(args[0])-min(args[0])+1, 1)) ###
	while 1:
		r=output_queue.get()
		logging.debug('The r is {}'.format(r))
		if r!='Done':
			# freq[r-min(args[0])]+=1; ###
			res.append(r)
		else :
			break
	input_queue.close(); output_queue.close()
	return res#, freq 

def doWork(input, output):
	while 1:
		try :
			logging.debug('Point 1');
			func, args=input.get(timeout=3);
			logging.debug('Point 2 {} {}'.format(args,*args))
			res=func(*args)
			logging.debug('Running the func.')
			output.put(res)
		except Exception as e:
			logging.debug('{}'.format(e));
			output.put('Done')
			break