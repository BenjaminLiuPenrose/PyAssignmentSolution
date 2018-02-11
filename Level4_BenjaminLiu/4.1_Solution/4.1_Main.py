# -*- coding: utf-8 -*- 
#!/usr/bin/env python
'''
Student name: Beier (Benjamin) Liu
Date:
Exercise 4.1.1 - 4.1.4

Remark:
Python 2.7 is recommended
Before running please install packages
Using cmd line py -2.7 -m install [package_name]
'''

'''===================================================================================================
Main program:
This is the demo program for Exercise 4.1.1 to 4.1.4

Implementations:
No external implementation required for Exercise 4.1.1 t0 4.1.4
==================================================================================================='''

def main():
	# Exercise 4.1.1
	# Use the following string for each of the below exercises: “ The Python course is the best course that I have ever taken. “
	print('\n====================================Exercise 4.1.1=====================================\n');
	s=' The Python course is the best course that I have ever taken.  ';

	# a) Display the length of the string
	print('Step a: Display the length of the string ... \n');
	print('The length of the string is {}. \n'.format(len(s)));
	raw_input('Program pause. Press enter to continue.\n');

	# b) Find the index of the first 'o’ in the string
	print('Step b: Finding the index of the first o in the string ... \n');
	print('The index of the first o in the string is {}. \n'.format(s.find('o')));
	raw_input('Program pause. Press enter to continue.\n');

	# c) Trim off the leading spaces only
	print('Step c: Trimming off the leading spaces only ... \n');
	print('After trimming off the leading spaces is: \n{} \n'.format(s.lstrip()));
	raw_input('Program pause. Press enter to continue.\n');

	# d) Trim off the trailing spaces only
	print('Step d: Trimming off the trailing spaces only ... \n');
	print('After trimming off the trailing spaces is: \n{} \n'.format(s.rstrip()));
	raw_input('Program pause. Press enter to continue.\n');

	# e) Trim off both the leading and trailing spaces
	print('Step e: Trimming off both the leading and trailing spaces ... \n');
	print('Aftering trimming off the l & t spaces is: \n{} \n'.format(s.strip()));
	s=s.strip(); #change s to the trimmed version
	raw_input('Program pause. Press enter to continue.\n');

	# f) Fully capitalize the string
	print('Step f: Fully capitalizing the string ... \n');
	print('Aftering capitalizing the string is: \n{} \n'.format(s.upper()));
	raw_input('Program pause. Press enter to continue.\n');

	# g) Fully lowercase the string
	print('Step g: Fully lowercasing the string ... \n');
	print('Aftering lowercasing the string is: \n{} \n'.format(s.lower()));
	raw_input('Program pause. Press enter to continue.\n');

	# h) Display the number of occurrence of the letter 'd’ and of the word 'the’
	print('Step h: Counting the number of occurrence of the letter d and of the word the ... \n');
	print('The frequency of the letter d is {}. \n'.format(s.count('d')));
	print('The frequency of the word the is {}. \n'.format(s.count('the')));
	raw_input('Program pause. Press enter to continue.\n');

	# i) Display the first 15 characters of the string
	print('Step i: Display the first 15 characters of the string ... \n');
	print('The first 15 chars of the string: \n{} \n'.format(s[:15]));
	raw_input('Program pause. Press enter to continue.\n');

	# j) Display the last 10 characters of the string
	print('Step j: Displaying the last 10	 characters of the string ... \n');
	print('The last 10 chars of the string is: \n{} \n'.format(s[-11:-1]));
	raw_input('Program pause. Press enter to continue.\n');

	# k) Display characters 5-23 of the string
	print('Step k: Displaying characters 5-23 of the string ... \n');
	print('The 5 - 23 of the string is: \n{} \n'.format(s[4:23]));
	raw_input('Program pause. Press enter to continue.\n');

	# l) Find the index of the first occurrence of the word course
	print('Step l: Finding the index of the first occurrence of the word course ... \n');
	print('The index of the first word course is {}. \n'.format(s.find('course')));
	raw_input('Program pause. Press enter to continue.\n');

	# m) Find the index of the second occurrence of the word course
	print('Step m: Finding the index of the second occurrence of the word course ... \n');
	print('The index of the second word course is {}. \n'.format(s.find('course', s.find('course')+1)));
	raw_input('Program pause. Press enter to continue.\n');

	# n) Find the index of the second to last occurrence of the letter 't’, between the 7th and 33rd
	# characters in the string
	print('Step n: Finding the index of second to last occurrence of the letter t ... \n');
	cnt=0;
	ls=[idx+6 for idx, item in enumerate(s[6:33]) if item=='t' ]
	print('The index second to last occurence of t is {}. \n'.format(ls[1:]));
	raw_input('Program pause. Press enter to continue.\n');

	# o) Replace the period (.) with an exclamation point (!)
	print('Step o: Replacing the period (.) with an exclamation point (!) ... \n');
	print('After replacing . with !, the string is {}. \n'.format(s.replace('.','!')));
	raw_input('Program pause. Press enter to continue.\n');

	# p) Replace all occurrences of the word 'course’ with 'class’
	print('Step p: Replacing all occurrences of the word course with class ... \n');
	print('After replacing course with class the string is {}. \n'.format(s.replace('course','class')));
	raw_input('Program pause. Press enter to continue.\n');

	# Exercise 4.1.2
	print('\n====================================Exercise 4.1.2=====================================\n');
	fpath='C:\\Users\\Me\\Desktop\\MyTable.csv';

	# a) Extract the filename with extension from the path
	print('Step a: Extracting the filename with extension from the path ... \n');
	print('The extrated filename is: \n{} \n'.format(fpath.split('\\')[-1]))

	# b) Extract the file extension only
	print('Step b: Extracting the file extension ... \n');
	fname=fpath.split('\\')[-1];
	print('The extrated filename is: \n{} \n'.format(fname.split('.')[-1]))

	# c) Add another folder (can name it whatever you’d like) between 'Desktop’ and the filename
	print('Step c: Adding another folder between Desktop and the filename ... \n');
	fpath_modi_ls=fpath.split('\\'); 
	fpath_modi_ls.insert(len(fpath_modi_ls)-1, 'Dummy Folder'); 
	fpath_modi='\\'.join(fpath_modi_ls);
	print('The new dir is: \n{} \n'.format(fpath_modi));
	raw_input('Program pause. Press enter to continue.\n');

	# Exercise 4.1.3
	print('\n====================================Exercise 4.1.3=====================================\n');
	ls=['C:', 'Users', 'Me', 'Desktop', 'MyTable.csv'];

	# a) Join the list together to create a valid pathname
	print('Step a: Joining the list together to create a valid pathname ... \n');
	print('The pathname is: \n{} \n'.format('\\'.join(ls)));

	# b) Insert another folder into the list, between ‘Desktop’ and ‘MyTable.csv’ 
	# and join the resulting list to create a valid pathname
	print('Step b: Insert another folder into the list and getting new pathname ... \n');
	ls.insert(len(ls)-1, 'Dummy Folder');
	print('The new pathname is: \n{} \n'.format('\\'.join(ls)));
	raw_input('Program pause. Press enter to continue.\n');

	# Exercise 4.1.4
	print('\n====================================Exercise 4.1.4=====================================\n');
	print('Step a: Getting user information and displaying the information ... \n');
	print('The pathname is: \n{} \n'.format('\\'.join(ls)));
	name=raw_input('Please enter your name: \n');
	while 1:
		try:
			age=int(raw_input('Please enter your age: \n'));
			break
		except Exception as e:
			print('Sorry sir, input is invalid. Please enter a number age.');
	country=raw_input('Please enter your country of residence: \n');

	# a) Display the information with format flags
	print('%s is %i years old and lives in %s\n' %(name, age, country));
	# a) Display the information with format numeric placeholders
	print('{0} is {1} years old and lives in {2}\n'.format(name, age, country));
	# a) Display the information with format keyword placeholders
	print('{name} is {age} years old and lives in {country}\n'.format(name=name, age=age, country=country));

	# b) Display the number with one decimal place with format flags
	print('%s is %.1f years old and lives in %s\n' %(name, age, country));
	# b) Display the number with one decimal place with format numeric placeholders
	print('{0} is {1:.1f} years old and lives in {2}\n'.format(name, age, country));
	# b) Display the number with one decimal place with format keyword placeholders
	print('{name} is {age:.1f} years old and lives in {country}\n'.format(name=name, age=age, country=country));
	print('The method of format function and keyword placeholders is more readable and clear, but it is lengthy\n');
	raw_input('Exercise 4.1.4 to 4.1.4 demo finished successfully! Press any key to exit.\n');

if __name__=='__main__':
	main()
