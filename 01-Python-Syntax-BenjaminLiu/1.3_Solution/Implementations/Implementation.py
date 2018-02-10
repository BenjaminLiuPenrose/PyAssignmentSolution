
# -*- coding: utf-8 -*-
#!/usr/bin/env python
'''
Student name: Beier (Benjamin) Liu
Date:
Exercise xxx:

Remark:
Python 2.7 is recommended
'''
import copy

'''===================================================================================================
Main program:
Write comments

Implementations:
Write comments
==================================================================================================='''

# Exercise 1.3.1 implementation
# Write a function that can print out the day of the week for a given number. I.e. Sunday is 1, Monday
#  is 2, etc. It should return a tuple of the original number and the corresponding name of the day.
# Function returns tuples of number and string 
def num2day(num):
	book={1:'Sun', 2: 'Mon', 3: 'Tue', 4: 'Wed', 5: 'Thur', 6: 'Fir', 7: 'Sat'};
	if (num>0 and num<8):
		day=book[num];
	else:
		day='Wrong number, number should be from 1 to 7';
	return (num, day)

# Exercise 1.3.2 implementation
# Write a function that returns the Fibonacci sequence as a list. The function should take a parameter called N 
# and return the entire sequence of Fibonaccis, from 0-N. You may use either iterative or recursive programming 
# techniques (bonus if you implement both!).
# Note that we will generalize the above, to allow it to return an infinite sequence, in Level 3, 
# where we discuss Python generators
# Function returns list
def iterGenFibo(N):
	Fibo=[]; n=copy.copy(N);
	a=1; b=1;
	if n==1:
		Fibo.append(a);
	# elif n==2:
	# 	Fibo.append(a); Fibo.append(b);
	else:
		Fibo.append(a); 
		for i in range(n-1):
			Fibo.append(b);
			tmp=a+b; a=b; b=tmp;
			
	return Fibo

def recurGenFibo(N):
	n=copy.copy(N);
	if n==1:
		Fibo=[1];
		return Fibo, 1, 1
	# elif n==2:
	# 	Fibo, a, b=recurGenFibo(n-1);
	# 	Fibo.append(b);
	# 	return Fibo, b, a+b 
	else:
		Fibo, a, b=recurGenFibo(n-1);
		Fibo.append(b);
		return Fibo, b, a+b

# Exercise 1.3.3 implementation
# Create a function that calculates the mean of a passed-in list
# Function returns a float
def mean(numLst):
	numLs=copy.deepcopy(numLst);
	return sum(numLs)/float(len(numLs));

# Exercise 1.3.4 implementation
# Create a function that calculates the variance of a passed-in list. This function should delegate to 
# the mean function (this means that it calls the mean function instead of containing logic to calculate 
# the mean itself, since mean is one of the steps to calculating variance)
# Function returns a float
def variance(numLst):
	numLs=copy.deepcopy(numLst); diff_s=0; mu=mean(numLs);
	for i in range(len(numLs)):
		diff_s += (numLs[i]-mu)**2;
	var=diff_s/float(len(numLs));
	return var 

# Exercise 1.3.5 implementation
# The previous exercise did not mention one crucial aspect of calculating the variance: Is it referring to sample 
# or population variance? Population variance has zero degrees of freedom whereas sample variance has one degree 
# of freedom. To this end, re-implement the variance function with an additional parameter called degOfFreedom, 
# which is used by the function to determine how to calculate the variance. This parameter should default to 1
# Function returns a float
def variance2(numLst, degOfFreedom=1):
	numLs=copy.deepcopy(numLst); diff_s=0; mu=mean(numLs);
	for i in range(len(numLs)):
		diff_s += (numLs[i]-mu)**2;
	var=diff_s/float(len(numLs)-degOfFreedom);
	return var 

# Exercise 1.3.6 implementation
# Create an alternative mean function to use *args instead of a taking a list of numbers. It should be invoked 
# as follows (for example):
# argsMean(1.3, 4.5, 6.7, 11.2, 100, 987.6)
# Test the function with variable numbers of arguments. It's also possible to pass a list or tuple into 
# this version of the function by using the * operator - you should attempt this as well
# Function returns float
def argsMean(*args):
	numLs=list(args);
	try:	
		if type(*args) is list or type(*args) is tuple:
			numLs=list(*args);
	except Exception as e:
		pass
	return sum(numLs)/float(len(numLs));


# Exercise 1.3.7 implementation
# Write a function that takes name, age as parameters. It should also take **kwargs. The function should 
# display the name, age, and any of ‘state’, ‘height’, and ‘weight’ that happen to exist in the kwargs. Call the 
# function with names, ages, and different combinations of keyword arguments (state, height, weight, hairColor, etc.)
def kwargsDemo(name, age, **kwargs):
	print('The name is '+name);
	print('The age is '+str(age));
	if kwargs.get('state')!=None:
		print('The state is '+str(kwargs.get('state')));
	if kwargs.get('height')!=None:
		print('The weight is '+str(kwargs.get('height')));
	if kwargs.get('weight')!=None:
		print('The weight is '+str(kwargs.get('weight')));
	print('');

# Exercise 1.3.8 implementation
# Extend the program from 8) to display all passed-in keyword arguments, no matter what the key is
def kwargsDemo2(name, age, **kwargs):
	for name, value in kwargs.iteritems():
		print('The '+str(name)+' is '+str(value));
	print('');
