# -*- coding: utf-8 -*- 
#!/usr/bin/env python
'''
Student name: Beier (Benjamin) Liu
Date:
Exercise 3.3.1 to 3.3.4

Remark:
Python 2.7 is recommended
Before running please install packages
Using cmd line py -2.7 -m install [package_name]
'''
import copy
import logging
import math
from Implementations.Loans.Loan import *
logging.getLogger().setLevel(logging.DEBUG)

'''===================================================================================================
Main program:
# Exercise 3.3.1
# Create code that takes a numerator and denominator input from the user. Output the quotient in 
# decimal form. Handle the divide-by-zero case gracefully, using exception handling

# Exercise 3.3.2
# Extend exercise 1) to handle the situation when the user inputs something other than a number, using
# exception handling. If the user does not enter a number, the code should provide the user with 
# an error message and ask the user to try again

# Exercise 3.3.3
# Create a function that calculates the factorial of an input number. If the input value is invalid, raise
# an exception. Test this out in main(), and handle the exception. Provide several examples, using 
# explicit error handling and general error handling (catching all error types)

# Exercise 3.3.4
# Modify all the applicable Loan classes from Level 2 so that if an incorrect Asset type is passed-into 
# the __init__ function, an exception is raised (instead of printing the message to the user). Test this 
# out in main, and handle the exception

Implementations:
Implementations are followed by main() function
Implementations can be found at 3_Solution\Implementations\Loans\Loan.py
==================================================================================================='''

def main():
	# Exercise 3.3.1
	print('\n====================================Exercise 3.3.1=====================================\n');
	print('Running my demo for Exercise 3.3.1 ... \n');
	while 1:
		numerator=raw_input('Please enter the desired numerator: \n');
		denominator=raw_input('Please enter the desired denominator: \n');
		numerator=float(numerator);
		denominator=float(denominator);
		try :
			quotient=numerator/denominator;
			logging.info('The quotient is {}. \n'.format(round(quotient, 4)));
			break
		except Exception as e:
			logging.exception('{} \n'.format(e));
			logging.error('Please enter a non zero number for the denominator. Please try again, sir. \n')
	raw_input('Program pause. Press enter to continue.\n');

	# Exercise 3.3.2
	print('\n====================================Exercise 3.3.2=====================================\n');
	print('Running my demo for Exercise 3.3.2 ... \n');
	while 1:
		numerator=raw_input('Please enter the desired numerator: \n');
		denominator=raw_input('Please enter the desired denominator: \n');
		try :
			numerator=float(numerator);
			denominator=float(denominator);
		except Exception as e:
			logging.exception('{} \n'.format(e));
			logging.error('Please enter numbers for numerator and denominator. Please try again, sir. \n')
		try :
			quotient=numerator/denominator;
			logging.info('The quotient is {}. \n'.format(round(quotient, 4)));
			break
		except Exception as e:
			logging.exception('{} \n'.format(e));
			logging.error('Please enter a non zero number for the denominator. Please try again, sir. \n')
	raw_input('Program pause. Press enter to continue.\n');

	# Exercise 3.3.3
	print('\n====================================Exercise 3.3.3=====================================\n');
	print('Running my factorial function ... \n');
	factorial();
	raw_input('Program pause. Press enter to continue.\n');

	# Exercise 3.3.4
	print('\n====================================Exercise 3.3.4=====================================\n');
	print('Running my logging.exception in class Loan ... \n');
	loan=Loan(asset=12, face=1000000, rate=.0375, term=36);
	raw_input('Demo finished successfully. Press any key to exit.\n');

def factorial():
	while 1:
		n=raw_input('Please enter your desired number: \n');
		try :
			n=int(n);
		except Exception as e:
			logging.exception('{} \n'.format(e));
			logging.error('Only integer is valid. Please enter again. \n');
		if n >= 0:
			if n>1000000 :
				logging.warning('The input value is too large to compute. The process can be slow. \n');
			factorial=math.factorial(n);
			logging.info('The factorial of {} is {}. \n'.format(n, factorial));
			break
		else :
			logging.error('Only positive integer is valid. Please enter again. \n');


if __name__=='__main__':
	main()