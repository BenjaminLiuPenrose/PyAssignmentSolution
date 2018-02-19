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
Main program:
Timer, memoize, multiProcess

Implementations:
Write comments
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
def multiProcess(input_size, process_num, func, *args):
	input_queue=multiprocessing.Queue()
	output_queue=multiprocessing.Queue()

	for i in range(input_size):
		input_queue.put((func, args))

	for i in range(process_num):
		multiprocessing.Process(target=doWork, args=(input_queue, output_queue)).start()

	res=[];
	while 1:
		r=output_queue.get()
		if r!='Done':
			res.append()
		else :
			break

def doWork(input, output):
	while 1:
		try :
			func, args=input.get(timeout=3);
			res=func(*args)
			output.put(res)
		except :
			output.put('Done')
			break