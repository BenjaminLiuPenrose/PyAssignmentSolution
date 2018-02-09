#!/usr/bin/env python
# -*- coding: utf-8 -*- 
'''
Student name: Beier (Benjamin) Liu
Date:
Exercise 1.2.1

Remark: 
Python 2.7 is recommended
Before running please install packages *numpy, *faker 
Using cmd line py -2.7 -m install [package_name]
'''
from Implementations.Implementation import *

'''===================================================================================================
Main program:
Write comments

Implementations:
See folder 1.2_Solution\Implementations
==================================================================================================='''

def main():
	# Exercise 1.2.1
	# Keeps asking the user for a number, until the user enters the letter s.
	# calculate and display the average of the numbers
	print('\n====================================Exercise 1.2.1=====================================\n');
	print('Running my meanOfInput function ... \n');
	meanOfInput();
	raw_input('Program pause. Press enter to continue.\n');
	
	# Exercise 1.2.2
	# Output details see Exercise 1.2.2 implementation numOperationsDemo(). Rmk: use Ctrl+F numOperationsDemo()
	print('\n====================================Exercise 1.2.2=====================================\n');
	print('Running my numOperationsDemo function ... \n');
	numOperationsDemo();
	raw_input('Program pause. Press enter to continue.\n');	

	# Exercise 1.2.3
	# Create a list of all even integers 1-1000. Prints all numbers in the above list, separated by commas
	print('\n====================================Exercise 1.2.3=====================================\n');
	print('Running my genEvenLs function ... \n');
	dummy, message=genEvenLs();
	print('Displaying the even numbers: \n');
	print(message);
	raw_input('Program pause. Press enter to continue.\n');	

	# Exercise 1.2.4
	# Create a list of all odd integers 1-1000. Prints all numbers in the above list, separated by commas
	print('\n====================================Exercise 1.2.4=====================================\n');
	print('Running my genOddLs function ... \n');
	dummy, message=genOddLs();
	print('Displaying the odd numbers: \n');
	print(message);	
	raw_input('Program pause. Press enter to continue.\n');	

	# Exercise 1.2.5
	# Create an aggregate list [pairs=(odd, even)] from 3) and 4) and print it out, separated by commas
	# function returns number list and printing message
	print('\n====================================Exercise 1.2.5=====================================\n');
	print('Running my aggreLs function ... \n');
	dummy, message=aggreLs();
	print('Displaying aggregate number [pairs=(odd, even)] list: \n');
	print(message);
	raw_input('Program pause. Press enter to continue.\n');	

	# Exercise 1.2.6
	# Print out the aggregate list [pairs=(odd, even)] from 5), backwards and separated by commas
	# function returns number list and printing message
	print('\n====================================Exercise 1.2.6=====================================\n');
	print('Running my aggreRevLs function ... \n');
	dummy, message=aggreRevLs();
	print('Displaying reversed number [pairs=(odd, even)] list: \n');
	print(message)
	raw_input('Program pause. Press enter to continue.\n');	

	# Exercise 1.2.7
	# List comprehension that results in a list of the squares of all numbers 0 through 100:
	# a. Filter the resulting list, to create another list that only contains numbers greater than 1000.
	# b. Filter further, to create another list that only contains even numbers (hint: use the Modulus operator)
	print('\n====================================Exercise 1.2.7=====================================\n');
	print('Running my genSquaredLs function ... \n');
	genSquaredLs();
	raw_input('Program pause. Press enter to continue.\n');	

	# Exercise 1.2.8
	# Create two lists: The first list should be called ‘players’, and contain at least ten unique names. 
	# The second list should be called ‘injured_players’, and contain a few names of players from the first list. 
	# Create a list comprehension which results in a list containing all active (non-injured) players.
	print('\n====================================Exercise 1.2.8=====================================\n');
	print('Running my playersLs function ... \n');
	playersLs();
	raw_input('Program pause. Press enter to continue.\n');	

	# Exercise 1.2.9
	# Exercise 1.2.9
	# Create a list of names, and a second list of ages which correspond to a name in the first list:
	# a. Zip them together and print the result.
	# b. Using a list comprehension, create a list that contains all the names for which the corresponding age 
	# is greater than or equals to 18. (Hint: Use zip as necessary. Can you also do this without zip? Which is better?)
	print('\n====================================Exercise 1.2.9=====================================\n');
	print('Running my goodList function ... \n');
	goodList();
	raw_input('Program pause. Press enter to continue.\n');	

	# Exercise 1.2.10
	# Exercise 1.2.10
	# Write a list comprehension that results in a list of all numbers 0 through 10,000,000.
	# a. Using a loop, filter the resulting list, to create another list that only contains numbers ending with the digit 0.
	# b. Do the same as a) using a list comprehension.
	# Use the time.time function to capture the time taken for each version. Which is quicker? Why?
	print('\n====================================Exercise 1.2.10=====================================\n');
	print('Running my timeComp function ... \n');
	timeComp();
	raw_input('Program pause. Press enter to continue.\n');	

	# Exercise 1.2.11	
	# Exercise 1.2.11
	# Create a list of lists of any type. Use the double list-comprehension syntax, as described in the lecture, 
	# to create a flattened single list.
	# Note that this can be useful in situations where one has a function that returns a list of items, 
	# and calls the function many times, resulting in a large list of lists (which can then be flattened, for simplicity)
	print('\n====================================Exercise 1.2.3=====================================\n');
	print('Running my unrollingLs function ... \n');
	unrollLs=unrollingLs();
	print('Dispalying the unrolled list: \n');
	print(unrollLs); print('');
	raw_input('Program pause. Press enter to continue.\n');	




if __name__=='__main__':
	main()