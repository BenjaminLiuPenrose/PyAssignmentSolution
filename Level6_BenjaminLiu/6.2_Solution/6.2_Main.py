# -*- coding: utf-8 -*- 
#!/usr/bin/env python
'''
Student name: Beier (Benjamin) Liu
Date: 18/2/2018
Exercise 6.2.1

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
from Implementations.PlayerGame import *
# from Implementations.Tools import *
logging.getLogger().setLevel(logging.INFO)

'''===================================================================================================
Main program:
Exercise 6.2.1
In this exercise, we will look to make the Monty Hall simulation achieve true multi-processing. 
This is a good segue to financial Monte Carlo as the concepts and approaches are the same.
a) Create and initialize five processes. Note that starting processes takes some time, and is the 
upfront cost of using multi-processing.
b) Execute all five processes. Give each process 1/5 of the total simulations (2,000,000 each)
c) Combine the five returned results lists and take the average, to get the overall result.
d) Time all of the above (starting from b). Does total runtime improve from the previous level?
e) Try decreasing/increasing the number of processes to determine the optimal runtime

Implementations:
See implementations followed by main() function
==================================================================================================='''

def main():
	# Exercise 6.2.1
	logging.info('\n====================================Exercise 6.2.1=====================================\n');
	game=[i for i in xrange(10000000)]; 
	logging.info('Step a to c: Runing 5 processes ... \n');
	s=time.time();
	res=multiProcess(5, montyHall, game);
	e=time.time()
	logging.info('Using {} process(es), it takes time {}'.format(5, e-s))

	logging.info('Step d and e: Searching optimal processes number (Calculating the original single precoess cost) ... \n')
	logging.info('Original it takes 147 secs, with multiprocessing method, it takes 60 secs with optimal_processes 8')
	ls=[2**i for i in range(8)]
	minimum=10000000; optimal_processes=1
	for i in ls:
		s=time.time()
		res=multiProcess(i, montyHall, game);
		e=time.time()
		if e-s<minimum:
			optimal_processes=i
			minimum=e-s
		if i==1:
			original_time=e-s
		logging.info('Using {} process(es), it takes time {}'.format(i, e-s))
	logging.info('Original it takes {} secs, with multiprocessing method, it takes {} secs with optimal_processes {}.'\
		.format(original_time, minimum, optimal_processes))
	res_hold=[r[0] for r in res]; 
	res_switch=[r[1] for r in res];
	logging.info('The prob of winning with stay strategy is {}.'.format(sum(res_hold)/float(len(res_hold))));
	logging.info('The prob of winning with switch strategy is {}.'.format(sum(res_switch)/float(len(res_switch))));


	raw_input('Demo finished successfully. Press any key to exit.\n');

#################################################################################################################################
def Timer(func):
	@functools.wraps(func)
	def wrapped(*args, **kwargs):
		s=time.time()
		res=func(*args, **kwargs);
		e=time.time()
		logging.debug('{}: {} seconds.'.format(func, e-s))
		return res
	return wrapped

def montyHall(i):
	logging.debug('**********************************This is Game {}*************************************'.format(i+1))
	player_hold=Player('Alex', 'Hold');
	game_hold=Game(player_hold);
	game_hold.playGame();
	player_switch=Player('Clare', 'Switch');
	game_switch=Game(player_switch);
	game_switch.playGame();
	return (player_hold.payoff, player_switch.payoff)

# def freq(num): 
# 	return num 

@Timer
def multiProcess(process_num, func, *args):
	input_queue=multiprocessing.Queue()
	output_queue=multiprocessing.Queue()

	for i in range(len(args[0])):
		input_queue.put((func, tuple([x[i] for x in args])))

	for i in range(process_num):
		multiprocessing.Process(target=doWork, args=(input_queue, output_queue)).start()

	res=[];
	freq=np.zeros((max(args[0])-min(args[0])+1, 1)) ###
	while 1:
		r=output_queue.get()
		logging.debug('The r is {}'.format(r))
		if r!='Done':
			# freq[r-min(args[0])]+=1; ###
			res.append(r)
			pass
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

# @Timer
# def curveNormalization(freq, max_new, min_new): # return list
# 	return [int((max_new-min_new)/(max(freq)-min(freq))*(f-min(freq))+max_new) for f in freq]

# @Timer
# def hist(lst, freq):
# 	for idx, f in enumerate(freq):
# 		ls=[];
# 		for _ in range(1, f+1):
# 			ls.append('-');
# 		dash=''.join(ls);
# 		logging.info('{}: {}'.format(idx+min(lst), dash))

if __name__=='__main__':
	# ls1=np.random.uniform(1, 20, 200000).astype(int)
	# freq1=multiProcess(50, freq, ls1); freq1=curveNormalization(freq1, max_new=100, min_new=1); hist(ls1, freq1); 
	# res1=multiProcess(5, f, np.random.uniform(0,1,100), np.random.uniform(0,1,100))
	main()