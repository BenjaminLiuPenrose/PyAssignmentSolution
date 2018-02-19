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

	res1=multiProcess(5, f, np.random.uniform(0,1,100), np.random.uniform(0,1,100))
	res2=multiProcess(50, f, np.random.uniform(0,1,100), np.random.uniform(0,1,100))
	res3=multiProcess(100, f, np.random.uniform(0,1,100), np.random.uniform(0,1,100))

	print sum(res1)/float(len(res1));
	print sum(res2)/float(len(res2));
	print sum(res3)/float(len(res3));

	raw_input('Demo finished successfully. Press any key to exit.\n');

	# Exercise xyz
	# Write comments
	print('\n====================================Exercise xyz=====================================\n');
	print('Running my myFunction function ... \n');
	myFunction();
	raw_input('Program pause. Press enter to continue.\n');

def f(a, b):
	time.sleep(2)
	return a

def montyHall(i):
	logging.info('**********************************This is Game {}*************************************'.format(i+1))
	game_hold=Game(player_hold);
	game_hold.playGame();
	res_hold.append(player_hold.payoff);

	# # play game start
	# res_hold=[]; res_switch=[];
	# for i in range(100000000):
	# logging.info('**********************************This is Game {}*************************************'.format(i+1))
	# game_hold=Game(player_hold);
	# game_hold.playGame();
	# # game_switch=Game(player_switch);
	# # game_switch.playGame();
	# res_hold.append(player_hold.payoff);
	# # res_switch.append(player_switch.payoff);
	# # play game end

freq1=freq(ls1); freq1=curveNormalization(freq1, max_new=100, min_new=1); hist(ls1, freq1);
def freq(ls): # return np.array
	freq=np.zeros((max(ls)-min(ls)+1, 1))
	for num in ls:
		for i in xrange(min(ls), max(ls)+1):	
			if num==i:
				freq[i-min(ls)]+=1;
	return freq


def Timer(func):
	@functools.wraps(func)
	def wrapped(*args, **kwargs):
		s=time.time()
		res=func(*args, **kwargs);
		e=time.time()
		logging.info('{}: {} seconds.'.format(func, e-s))
		return res
	return wrapped

@Timer
def curveNormalization(freq, max_new, min_new): # return list
	# max_old=max(freq); min_old=min(freq);
	# new_freq=freq;
	# for idx, f in enumerate(freq):
	# 	new_freq[idx]=(max_new-min_new)/(max_old-min_old)*(f-min_old)+max_new;
	# return new_freq
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

	# print tuple([x[0] for x in args])
	for i in range(len(args[0])):
		input_queue.put((func, tuple([x[i] for x in args])))

	for i in range(process_num):
		multiprocessing.Process(target=doWork, args=(input_queue, output_queue)).start()

	res=[];
	while 1:
		r=output_queue.get()
		if r!='Done':
			#res.append()
			pass
		else :
			break

	return res

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