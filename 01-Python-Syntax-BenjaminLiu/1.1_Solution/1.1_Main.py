#!/usr/bin/env python
# -*- coding: utf-8 -*- 
'''
Student name: Beier (Benjamin) Liu
Date:
Exercise 1.1.1 - 1.1.8
'''
# encoding: utf-8

'''===================================================================================================
Main program:
1. Print 'Hello World!' on screen
2. Print 'Hello World' each word should appear on a different line
3. Print 'Hello World' each word is separated with a tab
4. Takes input from the user , and stores it in a variable, and print the stored value
5. Takes input from the user and print input value and its type
6. Output details see Exercise 1.1.6 implementation takeInput_3()
7. Takes two inputs from the user (the base and height) of a triangle. Output the area of the triangle
8. Takes two inputs from the user (the base and height) of a triangle. Output the area of the triangle again

Implementations:
Followed by main functions
==================================================================================================='''

def main():
	# Exercise 1.1.1
	# Print 'Hello World!' on screen
	print('\n==============================Exercise 1.1.1============================================\n')
	print('Running my helloWorld_1 function ... \n');
	helloWorld_1();
	raw_input('Program pause. Press enter to continue.\n');

	# Exercise 1.1.2
	# Print 'Hello World' each word should appear on a different line
	print('\n==============================Exercise 1.1.2============================================\n')
	print('Running my helloWorld_2 function ... \n');
	helloWorld_2();
	raw_input('Program pause. Press enter to continue.\n');

	# Exercise 1.1.3
	# Print 'Hello World' each word is separated with a tab
	print('\n==============================Exercise 1.1.3============================================\n');
	print('Running my helloWorld_3 function ... \n');
	helloWorld_3();
	raw_input('Program pause. Press enter to continue.\n');

	# Exercise 1.1.4
	# Takes input from the user , and stores it in a variable, and print the stored value
	print('\n==============================Exercise 1.1.4============================================\n');
	print('Running my takeInput_1 function ... \n');
	var=takeInput_1();
	print('\nValue '+str(var)+' is successfully stored.\n');
	raw_input('Program pause. Press enter to continue.\n');

	# Exercise 1.1.5
	# Takes input from the user and print input value and its type
	print('\n==============================Exercise 1.1.5============================================\n');
	print('Running my takeInput_2 function ... \n');
	takeInput_2();
	raw_input('Program pause. Press enter to continue.\n');

	# Exercise 1.1.6
	# Output details see Exercise 1.1.6 implementation takeInput_3(). Rmk: use Ctrl+F takeInput_3()
	print('\n==============================Exercise 1.1.6============================================\n');
	print('Running my takeInput_3 function ... \n');
	takeInput_3();
	raw_input('Program pause. Press enter to continue.\n');

	# Exercise 1.1.7
	# Takes two inputs from the user (the base and height) of a triangle. Output the area of the triangle
	# computeTriArea_1 is using function input()
	print('\n==============================Exercise 1.1.7============================================\n');
	print('Running my computeTriArea_1 function ... \n');
	computeTriArea_1();
	raw_input('Program pause. Press enter to continue.\n');

	# Exercise 1.1.8
	# Takes two inputs from the user (the base and height) of a triangle. Output the area of the triangle
	# computeTriArea_2 is using function raw_input()
	print('\n==============================Exercise 1.1.8============================================\n');
	print('Running my computeTriArea_2 function ... \n');
	computeTriArea_2();
	raw_input('Program pause. Press enter to continue.\n');

	print('Great, this is the end of this demo.');
	raw_input('End of exercise 1.1.1 - 1.1.8 demo. Press any key to exit.\n');

# Exercise 1.1.1 implementation
# Print 'Hello World!' on screen
def helloWorld_1():
	print('Hello World\n');

# Exercise 1.1.2 implementation
# Print 'Hello World' each word should appear on a different line
def helloWorld_2():
	print('Hello\nWorld\n');

# Exercise 1.1.3 implementation
# Print 'Hello World' each word is separated with a tab
def helloWorld_3():
	print('Hello\tWorld\n');

# Exercise 1.1.4 implementation
# Takes input from the user , and stores it in a variable, and print the stored value
def takeInput_1():
	while 1:
		try:
			var=input('Please input a value(string or char with "" or just a number): \n');
			break;
		except Exception as e:
			print('Error message: '+str(e));
			print('Invalid input. Please enter string or char with "" and do not enter space or nothing\n');
	return var

# Exercise 1.1.5 implementation
# Takes input from the user and print input value and its type
def takeInput_2():
	var=takeInput_1();
	print('\nThe entered value is '+str(var)+' and its type is '+str(type(var))+'\n');
	return var 

# Exercise 1.1.6 implementation
def takeInput_3():
	var=takeInput_1();
	# If the inputted value is a float or int, then output 'The inputted value is a number'
	if (isinstance(var, int) or isinstance(var, float)):
		print('\nThe inputted value is a number.\n');
		# if greater than 65, output 'the inputted number is less than 65'
		if var > 65.0:
			print('the inputted number is greater than 65.\n');
		# if less than 64, output "\'the inputted number is greater than 64'
		elif var < 64.0:
			print('the inputted number is less than 64.\n');
		# otherwise, output 'The inputted value is neither a number nor a string'
		else :
			print('the inputted number is between 64 and 65.\n');

	# Otherwise, if the inputted value is a string, then output 'The inputted value is a string'
	elif (isinstance(var, str)):
		print('\nThe inputted value is a string.\n');

	# Otherwise, output 'The inputted value is neither a number nor a string'
	else :
		print('\nThe inputted value is neither a number nor a string.\n');

# Exercise 1.1.7 implementation
# Takes two inputs from the user (the base and height) of a triangle. Output the area of the triangle
def computeTriArea_1():
	while 1:
		try:
			base=input('Please enter the base of triangle(please enter a number): \n');
			while not (isinstance(base, int) or isinstance(base, float)):
				print('Invalid base. Please enter a number.\n');
				base=input('Please enter the base of triangle again: \n');
			break;
		except Exception as e:
			print('Error message: '+str(e));
			print('Invalid base. Please enter a number.\n');
	while 1:
		try:
			height=input('Please enter the height of triangle(please enter a number): \n');
			while not (isinstance(height, int) or isinstance(height, float)):
				print('Invalid height. Please enter a number.\n');
				height=input('Please enter the height of triangle again: \n');
			break;
		except Exception as e:
			print('Error message: '+str(e));			
			print('Invalid base. Please enter a number.\n');
	print('\nThe triangle area of base '+str(base)+' and height '+str(height)+' is '+str(base*height/2.0)+'\n');

# Exercise 1.1.8 implementation
# Takes two inputs from the user (the base and height) of a triangle. Output the area of the triangle
def computeTriArea_2():
	base=raw_input('Please enter the base of triangle(please enter a number): \n');
	while 1:
		try:
			base=float(base);
			break;
		except Exception as e:
			print('Error message: '+str(e));
			print('Invalid base. Please enter a number.\n');
			base=raw_input('Please enter the base of triangle again: \n');
	height=raw_input('Please enter the height of triangle(please enter a number): \n');
	while 1:
		try:
			height=float(height);
			break;
		except Exception as e:
			print('Error message: '+str(e));
			print('Invalid height. Please enter a number.\n');
			height=raw_input('Please enter the height of triangle again: \n');
	print('\nThe triangle area of base '+str(base)+' and height '+str(height)+' is '+str(base*height/2.0)+'\n');


if __name__=='__main__':
	main()