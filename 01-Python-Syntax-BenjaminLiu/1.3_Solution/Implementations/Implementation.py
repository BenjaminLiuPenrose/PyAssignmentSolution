
#!/usr/bin/env python
# -*- coding: utf-8 -*- 
'''
Student name: Beier (Benjamin) Liu
Date:
Exercise xxx:

Remark:
Python 2.7 is recommended
Before running please install packages
Using cmd line py -2.7 -m install [package_name]
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
def con(num):
	book={1:'Sun', 2: 'Mon', 3: 'Tue', 4: 'Wed', 5: 'Thur', 6: 'Fir', 7: 'Sat'};
	if (num>0 and num<7):
		day=book[num];
	else:
		day='Wrong number, number should be from 1 to 7';
	return (num, day)

# Exercise 1.3.2 implementation
# Write a function that returns the Fibonacci sequence as a list. The function should take a parameter called N 
# and return the entire sequence of Fibonaccis, from 0-N. You may use either iterative or recursive programming 
# techniques (bonus if you implement both!).
# Note that we will generalize the above, to allow it to return an infinite sequence, in Level 3, 
# where we discuss Python generators.
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
		Fibo.append(b)
		return Fibo, b, a+b;


# Exercise 1.3 implementation
# Write comments