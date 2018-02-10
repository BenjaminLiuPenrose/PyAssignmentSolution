# -*- coding: utf-8 -*-
#!/usr/bin/env python
'''
Student name: Beier (Benjamin) Liu
Date: 2/10/2017
Exercise 1.3

Remark:
Python 2.7 is recommended
'''
from Implementations.Implementation import *


'''===================================================================================================
Main program:
Demo Exercise 1.3.1 - 1.3.8 in a row

Implementations:
See folder 1.3_Solution\Implementations
==================================================================================================='''

def main():
	# Exercise 1.3.1
	# Write a function that can print out the day of the week for a given number. I.e. Sunday is 1, Monday
	#  is 2, etc. It should return a tuple of the original number and the corresponding name of the day.
	print('\n====================================Exercise 1.3.1=====================================\n');
	print('Running my num2day function ... \n');
	for i in range(1,7+1):
		print('Displaying day corresponding to '+str(i));
		print(num2day(i)); print('');
	raw_input('Program pause. Press enter to continue.\n');

	# Exercise 1.3.2
	# Write a function that returns the Fibonacci sequence as a list. The function should take a parameter called N 
	# and return the entire sequence of Fibonaccis, from 0-N. You may use either iterative or recursive programming 
	# techniques (bonus if you implement both!).
	# Note that we will generalize the above, to allow it to return an infinite sequence, in Level 3, 
	# where we discuss Python generators
	print('\n====================================Exercise 1.3.2=====================================\n');
	print('Running my iterGenFibo function ... \n');
	Fibo1=iterGenFibo(10);
	print('The first 10 Fibo number list by iteration menthod is: \n'+str(Fibo1)+'\n');
	print('Running my recurGenFibo function ... \n');
	Fibo2, dummy, dummy=recurGenFibo(10);
	print('The first 10 Fibo number list by recursion method is: \n'+str(Fibo2)+'\n');
	raw_input('Program pause. Press enter to continue.\n');

	# Exercise 1.3.3
	# Create a function that calculates the mean of a passed-in list
	print('\n====================================Exercise 1.3.3=====================================\n');
	print('Running my mean function ... \n');
	mu=mean([1,20,100,29,66,88,6,8]);
	print('The mean of list [1,20,100,29,66,88,6,8] is: \n'+str(mu)+'\n');
	raw_input('Program pause. Press enter to continue.\n');

	# Exercise 1.3.4
	# Create a function that calculates the variance of a passed-in list. This function should delegate to 
	# the mean function (this means that it calls the mean function instead of containing logic to calculate 
	# the mean itself, since mean is one of the steps to calculating variance)
	print('\n====================================Exercise 1.3.4=====================================\n');
	print('Running my variance function ... \n');
	var=variance([1,20,100,29,66,88,6,8]);
	print('The variance of list [1,20,100,29,66,88,6,8] is: \n'+str(var)+'\n');
	raw_input('Program pause. Press enter to continue.\n');

	# Exercise 1.3.5
	# The previous exercise did not mention one crucial aspect of calculating the variance: Is it referring to sample 
	# or population variance? Population variance has zero degrees of freedom whereas sample variance has one degree 
	# of freedom. To this end, re-implement the variance function with an additional parameter called degOfFreedom, 
	# which is used by the function to determine how to calculate the variance. This parameter should default to 1
	print('\n====================================Exercise 1.3.5=====================================\n');
	print('Running my variance2 function ... \n');
	var_p=variance2([1,20,100,29,66,88,6,8], 0);
	print('The population variance of list [1,20,100,29,66,88,6,8] is: \n'+str(var_p)+'\n');
	var_s=variance2([1,20,100,29,66,88,6,8]);
	print('The sample variance of list [1,20,100,29,66,88,6,8] is: \n'+str(var_s)+'\n');
	raw_input('Program pause. Press enter to continue.\n');

	# Exercise 1.3.6
	# Create an alternative mean function to use *args instead of a taking a list of numbers. It should be invoked 
	# as follows (for example):
	# argsMean(1.3, 4.5, 6.7, 11.2, 100, 987.6)
	# Test the function with variable numbers of arguments. It's also possible to pass a list or tuple into 
	# this version of the function by using the * operator - you should attempt this as well
	print('\n====================================Exercise 1.3.6=====================================\n');
	print('Running my argsMean function ... \n');
	mu1=argsMean(1,20,100,29,66,88,6,8);
	print('The mean of numbers seq 1,20,100,29,66,88,6,8 is: \n'+str(mu1)+'\n');
	mu2=argsMean([1,20,100,29,66,88,6,8]);
	print('The mean of numbers list [1,20,100,29,66,88,6,8] is: \n'+str(mu2)+'\n');
	mu3=argsMean((1,20,100,29,66,88,6,8));
	print('The mean of numbers tuple (1,20,100,29,66,88,6,8) is: \n'+str(mu3)+'\n');
	raw_input('Program pause. Press enter to continue.\n');

	# Exercise 1.3.7
	# Write a function that takes name, age as parameters. It should also take **kwargs. The function should 
	# display the name, age, and any of ‘state’, ‘height’, and ‘weight’ that happen to exist in the kwargs. Call the 
	# function with names, ages, and different combinations of keyword arguments (state, height, weight, hairColor, etc.)
	print('\n====================================Exercise 1.3.7=====================================\n');
	print('Running my kwargsDemo function ... \n');
	print('The person has extra attributes state, height, weight, hairColor, hobby: ');
	kwargsDemo(name='Alice', age=22, state='single', height='168 cm', weight='60 kg', hairColor='grey');
	print('The person has extra attributes state, height, hairColor: ');
	kwargsDemo(name='Bipshop', age=32, state='single', height='170 cm', hairColor='black');
	print('The person has extra attributes state, height, hairColor: ');
	kwargsDemo(name='Clare', age=25, height=170, hairColor='black');
	print('The person has extra attributes height hairColor: \n');
	kwargsDemo(name='Dave', age=26, hairColor='brown');
	raw_input('Program pause. Press enter to continue.\n');

	# Exercise 1.3.8
	# Write comments
	print('\n====================================Exercise 1.3.8=====================================\n');
	print('Running my kwargsDemo2 function ... ');
	print('The person has extra attributes state, height, weight, hairColor, hobby: ');
	kwargsDemo2(name='Alice', age=22, state='single', height='168 cm', weight='60 kg', hairColor='grey', hobby='poker');
	raw_input('Program pause. Press enter to continue.');

if __name__=='__main__':
	main()