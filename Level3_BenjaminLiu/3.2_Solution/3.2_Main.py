# -*- coding: utf-8 -*- 
#!/usr/bin/env python
'''
Student name: Beier (Benjamin) Liu
Date:
Exercise 3.2.1 to 3.2.9

Remark:
Python 2.7 is recommended
Before running please install packages *numpy
Using cmd line py -2.7 -m install [package_name]
'''
import numpy as np
import time
import itertools

'''===================================================================================================
Main program:
# Exercise 3.2.1
# Create a list of 1000 numbers. Convert the list to an iterable and iterate through it

# Exercise 3.2.2
# Create a list of 1000 numbers. Convert the list to a reversed iterable and iterate through it

# Exercise 3.2.4
# Modify the Fibonacci function from Exercise 1.3.2 to be a generator function. Note that the function 
# should no longer have any input parameter since making it a generator allows it to return the infinite 
# sequence. Do the following:
# a. Display the first and second values of the Fibonacci sequence.
# b. Iterate through and display the next 100 values of the sequence

# Exercise 3.2.5
# Generator expressions:
# a. Create a list comprehension that contains the square of all numbers from 0-5,000,000, using range
# Sum this list, using the built-in sum function
# b. Port the above to a generator expression, using xrange. Sum this generator expression, using the 
# built-in sum function
# c. Compare the total time taken to build and sum each. Which one is faster? What are the benefits of 
# using the generator instead of the list comprehension? Why

# Exercise 3.2.6
# Create three generator expressions and use itertools.chain to attach them together. Print out 
# the result as a list

# Exercise 3.2.7
# Create three generator expressions and zip them together. Print out the result as a list

# Exercise 3.2.8
# Create three generator expressions and use the appropriate itertools function to get all the 
# combinations of the values. Print out the result as a list

# Exercise 3.2.9
# Create a list of ten names. Loop through the list and output each name in the following format

Implementations:
Write comments
==================================================================================================='''

def main():
	# Exercise 3.2.1
	# Create a list of 1000 numbers. Convert the list to an iterable and iterate through it
	print('\n====================================Exercise 3.2.1=====================================\n');
	print('Converting a 1000 list to an iterable function ... \n');
	Ls=list(np.random.randint(1, 1000, 1000));
	LsIter=iter(Ls);
	for i in range(1000):
		print(LsIter.next())
	raw_input('Program pause. Press enter to continue.\n');

	# Exercise 3.2.2
	# Create a list of 1000 numbers. Convert the list to a reversed iterable and iterate through it
	print('\n====================================Exercise 3.2.2=====================================\n');
	print('Converting a 1000 list to a reverse iterable function ... \n');
	LsRevIter=iter(reversed(Ls))
	for i in range(1000):
		print(LsRevIter.next())
	raw_input('Program pause. Press enter to continue.\n');

	# Exercise 3.2.4
	print('\n====================================Exercise 3.2.4=====================================\n');
	print('Step a: a. Displaying the first and second values of the Fibonacci sequence ... \n');
	f=genFibo();
	print('The first Fibo value is {0} and the second Fibo value is {1}. \n'.\
		format(f.next(), f.next()))
	print('Step b:  Iterate through and display the next 100 values of the sequence. \n');
	for i in range(100):
		print(f.next());
	raw_input('Program pause. Press enter to continue.\n');

	# Exercise 3.2.5
	print('\n====================================Exercise 3.2.5=====================================\n');
	print('Comparing range and xrange function ... \n');
	s=time.time();
	suum=sum([i**2 for i in range(5000000)])
	e=time.time(); 
	s2=time.time();
	suum=sum(i**2 for i in xrange(5000000))
	e2=time.time();
	elap=e-s; elap2=e2-s2;
	print('The range list compre takes time {}s; the xrange generator expression takes time {}s. \n'.
		format(elap, elap2));
	print('The xrange generator expression method takes less time as it enable lazy evaluation (aka only evaluate when necessary). \n');
	raw_input('Program pause. Press enter to continue.\n');

	# Exercise 3.2.6
	print('\n====================================Exercise 3.2.6=====================================\n');
	print('Running itertools.chain ... \n');
	rates_1=iter(list(np.random.normal(0.5, 0.2, 100)));
	rates_2=iter(list(np.random.normal(0.5, 0.2, 100)));
	rates_3=iter(list(np.random.normal(0.5, 0.2, 100)));
	allRates=itertools.chain(rates_1, rates_2, rates_3);
	print(list(allRates)); print('');
	raw_input('Program pause. Press enter to continue.\n');

	# Exercise 3.2.7
	print('\n====================================Exercise 3.2.7=====================================\n');
	print('Running itertools.izip ... \n');
	rates_1=iter(list(np.random.normal(0.5, 0.2, 100)));
	rates_2=iter(list(np.random.normal(0.5, 0.2, 100)));
	rates_3=iter(list(np.random.normal(0.5, 0.2, 100)));
	zipRates=itertools.izip(rates_1, rates_2, rates_3);
	print(list(zipRates)); print('');
	raw_input('Program pause. Press enter to continue.\n');

	# Exercise 3.2.8
	print('\n====================================Exercise 3.2.8=====================================\n');
	print('Running itertools.product ... \n');
	rates_1=iter(list(np.random.normal(0.5, 0.2, 10)));
	rates_2=iter(list(np.random.normal(0.5, 0.2, 10)));
	rates_3=iter(list(np.random.normal(0.5, 0.2, 10)));
	prodRates=itertools.product(rates_1, rates_2,rates_3);
	print(list(prodRates)); print('');
	raw_input('Program pause. Press enter to continue.\n');

	# Exercise 3.2.9
	print('\n====================================Exercise 3.2.9=====================================\n');
	print('Running enumerate ... \n');
	names=['Alex','Ben','Clare','Dave','Ford','Ginger','Henry','Jack','Kent','Que','Ross'];
	for idx, name in enumerate(names):
		print('Name {idx}: {name}'.format(idx=idx, name=name));
	print('');
	raw_input('Program pause. Press enter to continue.\n');


def genFibo():
	a=0; b=1
	while True:
		tmp=a+b; a=b; b=tmp;
		yield a 

if __name__=='__main__':
	main()