#!/usr/bin/env python
# -*- coding: utf-8 -*- 
'''
Student name: Beier (Benjamin) Liu
Date: 2/10/2017
Exercise 1.2
'''
import copy
import time
from faker import Faker
import numpy as np

'''===================================================================================================
File content:
Implementations for Exercise 1.2
Implementations for 1.2_Main.py
==================================================================================================='''

# Exercise 1.2.1 implementation
# Keeps asking the user for a number, until the user enters the letter s.
# calculate and display the average of the numbers
def meanOfInput():
	ls=[];
	# asking the user for a number, until the user enters the letter s
	while 1:
		try:
			tmp=raw_input('Please enter a number(s to stop): \n');
			if (tmp=='s' and len(ls)!=0):
				break;
			if (tmp=='s' and len(ls)==0):
				print('Please enter at least one number.\n');
			tmp=float(tmp);
			ls.append(tmp);
		except Exception as e:
			print('Error message: '+str(e)+'\n');

	# calculate and display the average of the numbers with a for loop
	ttl=0; cnt=0;
	for num in ls:
		ttl+=num;
		cnt+=1;
	print('The average of entered values is '+str(ttl/float(cnt))+'\n');

# Exercise 1.2.2 implementation
# Output details see Exercise 1.2.2 implementation numOperationsDemo(). Rmk: use Ctrl+F numOperationsDemo()
def numOperationsDemo(lst=None):
	if not lst:
		ls=[12, 13.5, 0, 22, 16.6, 8.8, 99, 196, -5, -3.3];
	else:
		ls=copy.deepcopy(lst);

	print('The original list is: '+str(ls)+'\n');

	# Display the first two numbers from the list (using indexing)
	print('Step a: The first two numbers in the list are '+str(ls[0])+' and '+str(ls[1])+'\n');

	# Display the last two numbers
	print('Step b: The last two numbers in the list are '+str(ls[-1])+' and '+str(ls[-2])+'\n');

	# Display all the numbers besides the last number, using a single print statement
	print('Step c: Displaying all the numbers besides the last number: '+str(ls[0:-1])+'\n');

	# Display all the numbers besides the first number, using a single print statement
	print('Step d: Displaying all the numbers besides the first number: '+str(ls[1:])+'\n');

	# Display all the numbers besides the first two and last three numbers, using a single print
	print('Step e: Displaying all the number bsides first two and last three: '+str(ls[3:-3])+'\n');

	# Append one number to the end of the list
	num=5;
	print('Step f: Appending number '+str(num)+' to the end of the list ... ');
	ls.append(num);
	print('The new list is '+str(ls)+'\n');

	# Append five numbers to the end of the list, using a single operation
	ls2=[2,3,4,5,6];
	print('Step g: Appending five numbers (2,3,4,5,6) to the end of the list ... ');
	ls.extend(ls2);
	print('The new list is '+str(ls)+'\n');

	# Insert one number right after the third number in the list
	num2=num; 
	print('Step h: Inserting number '+str(num2)+' right after the third number to the end of the list ... ');
	ls.insert(num2, 3);
	print('The new list is '+str(ls)+'\n');

	# Modify the fourth-to-last number in the list
	print('Step i: Modifying the fourth-to-last number in the list ... ');
	for i in range(len(ls)):
		if i>=3:
			ls[i]=i+6;
	print('The new list is '+str(ls)+'\n')

	# Display the list backwards, using splicing
	print('Displaying the list backwards, using splicing ... ');
	print(list(reversed(ls))); print('');

	# Display every second item in the list
	print('Displaying every second item in the list');
	print([item for i,item in enumerate(ls) if i%2==0]); print('');

	# Display every second item in the list, backwards
	print('Displaying every second item in the list');
	print([item for i,item in enumerate(list(reversed(ls))) if i%2==0]); print('');

# Exercise 1.2.3 implementation
# Create a list of all even integers 1-1000. Write a loop that prints all numbers in the above list, separated by commas
# function returns number list and printing message
def genEvenLs():
	evenLs=[i for i in range(1, 1000+1) if i%2==0];
	message='';
	for idx,item in enumerate(evenLs):
		if idx==len(evenLs)-1:
			message=message+str(item)+'\n';
			break;
		item=str(item)+', ';
		message+=item;
	return evenLs, message

# Exercise 1.2.4 implementation
# Create a list of all odd integers 1-1000. Write a loop that prints all numbers in the above list, separated by commas
# function returns number list and printing message
def genOddLs():
	oddLs=[i for i in range(1,1000+1) if i%2==1];
	message='';
	for idx,item in enumerate(oddLs):
		if idx==len(oddLs)-1:
			message=message+str(item)+'\n';
			break;
		item=str(item)+', ';
		message+=item;
	return oddLs, message

# Exercise 1.2.5 implementation
# Create an aggregate list [pairs=(odd, even)] from 3) and 4) and print it out, separated by commas
# function returns number list and printing message
def aggreLs():
	evenLs, dummy=genEvenLs(); oddLs, dummy=genOddLs(); message='';
	aggreLs=list(zip(oddLs, evenLs));
	for o, e in aggreLs:
		if (o==max(oddLs) or e==max(evenLs)):
			item=str(o)+', '+str(e)+'\n';
			message+=item;
			break;
		item=str(o)+', '+str(e)+', ';
		message+=item;
	return aggreLs, message

# Exercise 1.2.6 implementation
# Print out the aggregate list [pairs=(odd, even)] from 5), backwards and separated by commas
# function returns number list and printing message
def aggreRevLs():
	Ls, dummy=aggreLs(); message='';
	RevLs=list(reversed(Ls));
	cnt=0;
	for o, e in RevLs:
		cnt+=1
		if (cnt==len(RevLs)):
			item=str(o)+', '+str(e)+'\n';
			message+=item;
			break;
		item=str(o)+', '+str(e)+', ';
		message+=item;
	return RevLs, message	

# Exercise 1.2.7
# List comprehension that results in a list of the squares of all numbers 0 through 100:
# a. Filter the resulting list, to create another list that only contains numbers greater than 1000.
# b. Filter further, to create another list that only contains even numbers (hint: use the Modulus operator)
def genSquaredLs():
	squaredLs=[i**2 for i in range(1, 100+1)];
	print('Step a: Displaying numbers gretaer than 1000: \n');
	filter_1=[i for i in squaredLs if i>1000];
	print(filter_1); print('');
	print('Step b: Displaying even numbers: \n');
	filter_2=[i for i in squaredLs if i%2==0];
	print(filter_2); print('');
	return filter_1, filter_2

# Exercise 1.2.8
# Create two lists: The first list should be called ‘players’, and contain at least ten unique names. 
# The second list should be called ‘injured_players’, and contain a few names of players from the first list. 
# Create a list comprehension which results in a list containing all active (non-injured) players.
def playersLs():
	players=[]; injured_players=[];
	#Create players list
	try :
		fake=Faker()
		while len(list(set(players)))<10:
			players=[str(fake.name()) for i in range(50)];
	except Exception as e:
		print(str(e)+'\n');
		print('Default players list will be used. \n')
		players=['Elda Palumbo', 'Pacifico Giordano', 'Sig. Avide Guerra', 'Yago Amato', 'Eustachio Messina', \
		'Dott. Violante Lombardo', 'Sig. Alighieri Monti', 'Costanzo Costa', 'Nazzareno Barbieri', 'Max Coppola'];
	players=list(set(players));
	# rand_players=np.random.shuffle(players);

	# Create injured players list
	rand_num=np.random.randint(1,len(players));
	injured_players=np.random.choice(players, rand_num);

	print('Dispalying the players list: \n');
	print(players); print('');
	print('Displaying the injured players list: \n');
	print(injured_players); print('');

# Exercise 1.2.9
# Create a list of names, and a second list of ages which correspond to a name in the first list:
# a. Zip them together and print the result.
# b. Using a list comprehension, create a list that contains all the names for which the corresponding age 
# is greater than or equals to 18. (Hint: Use zip as necessary. Can you also do this without zip? Which is better?)
def goodList():
	names=[]; ages=[]; 
	# Create names list
	try :
		fake=Faker();
		size=np.random.randint(10,50);
		names=[str(fake.name()) for i in range(size)];
	except Exception as e:
		print(str(e)+'\n');
		print('Default names list will be used. \n');
		names=['Elda Palumbo', 'Pacifico Giordano', 'Sig. Avide Guerra', 'Yago Amato', 'Eustachio Messina', \
		'Dott. Violante Lombardo', 'Sig. Alighieri Monti', 'Costanzo Costa', 'Nazzareno Barbieri', 'Max Coppola'];
		size=len(names);

	# Create ages list
	for i in range(size):
		ages.append(np.random.randint(5,80));

	# Create zip list
	zipLs=list(zip(names,ages));
	print('Dispalying the (names, ages) list: \n');
	print(zipLs); print('');

	# Create list names for which the corresponding age is greater than or equals to 18
	resultLs=[names for name, age in zipLs if age>=18];
	print('Dispalying the name whose age is not less than 18: \n');
	priint(resultLs); print('');

# Exercise 1.2.10
# Write a list comprehension that results in a list of all numbers 0 through 10,000,000.
# a. Using a loop, filter the resulting list, to create another list that only contains numbers ending with the digit 0.
# b. Do the same as a) using a list comprehension.
# Use the time.time function to capture the time taken for each version. Which is quicker? Why?
def timeComp():
	numLs=[i+1 for i in range(10000000)];
	# Use loop method, cost records the method time cost
	start=time.time();
	zeroEndingLs=[];
	for i in numLs:
		if i%10==0:
			zeroEndingLs.append(i);
	end=time.time();
	cost=end-start;

	# Use LC method, cost2 records the method time cost
	start2=time.time();
	zeroEndingLs2=[i for i in numLs if i%10==0];
	end2=time.time();
	cost2=end2-start2;
	print('Loop method overall time cost is '+str(cost)+'\n');
	print('List comprehension method overall time cost is '+str(cost2)+'\n');



# Exercise 1.2.11
# Create a list of lists of any type. Use the double list-comprehension syntax, as described in the lecture, 
# to create a flattened single list.
# Note that this can be useful in situations where one has a function that returns a list of items, 
# and calls the function many times, resulting in a large list of lists (which can then be flattened, for simplicity)
def unrollingLs(lst=None):
	if not lst:
		# Create a list of list of integers with random 5-50 values
		ls=[];
		for i in range(20):
			ls.append([]);
			for j in range(20):
				ls[i].append(np.random.randint(5,50))
	else:
		ls=copy.deepcopy(lst);

	# Unroll the list
	unrollLs=[ls[i][j] for i in range(len(ls)) for j in range(len(ls[i]))];

	return unrollLs

