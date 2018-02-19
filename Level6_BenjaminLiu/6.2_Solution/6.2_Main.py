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
# from Implementations.Tools import *
logging.getLogger().setLevel(logging.DEBUG)

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
	print('\n====================================Exercise 6.2.1=====================================\n');
	print('Running my multiprocessing demo ... \n');
	freq1=multiProcess(50, freq, ls1); freq1=curveNormalization(freq1, max_new=100, min_new=1); hist(ls1, freq1); 
	game=[i for i in xrange(100000000)];res=multiProcess(5, montyHall, game);
	print res
	# res1=multiProcess(5, f, np.random.uniform(0,1,100), np.random.uniform(0,1,100))


	# print sum(res)/float(len(res));
	# print sum(res2)/float(len(res2));
	# print sum(res3)/float(len(res3));
	raw_input('Demo finished successfully. Press any key to exit.\n');

#################################################################################################################################
def Timer(func):
	@functools.wraps(func)
	def wrapped(*args, **kwargs):
		s=time.time()
		res=func(*args, **kwargs);
		e=time.time()
		logging.info('{}: {} seconds.'.format(func, e-s))
		return res
	return wrapped

def f(a, b):
	time.sleep(2)
	return a

def montyHall(i):
	logging.info('**********************************This is Game {}*************************************'.format(i+1))
	player_hold=Player('Alex', 'Hold');
	game_hold=Game(player_hold);
	game_hold.playGame()；
	player_switch=Player('Clare', 'Switch');
	game_switch=Game(player_switch);
	game_switch.playGame();
	return (player_hold.payoff, player_switch.payoff)


def freq(num): # return np.array
	return num 

@Timer
def curveNormalization(freq, max_new, min_new): # return list
	return [int((max_new-min_new)/(max(freq)-min(freq))*(f-min(freq))+max_new) for f in freq]

@Timer
def hist(lst, freq):
	for idx, f in enumerate(freq):
		ls=[];
		for _ in range(1, f+1):
			ls.append('-');
		dash=''.join(ls);
		# logging.info('{}: {}'.format(idx+min(lst), dash))
		print('{}: {}'.format(idx+min(lst), dash))

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
		if r!='Done':
			# freq[r-min(args[0])]+=1; ###
			res.append(r)
			pass
		else :
			break
	return res#, freq 

def doWork(input, output):
	while 1:
		try :
			func, args=input.get(timeout=3);
			res=func(*args)
			output.put(res)
		except :
			output.put('Done')
			break

if __name__=='__main__':
	main()