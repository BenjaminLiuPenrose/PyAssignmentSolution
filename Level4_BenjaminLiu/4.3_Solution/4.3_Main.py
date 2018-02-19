# -*- coding: utf-8 -*- 
#!/usr/bin/env python
'''
Student name: Beier (Benjamin) Liu
Date: 2/18/2018
Exercise 4.3.1 to 4.3.8

Remark:
Python 2.7 is recommended
Before running please install packages *numpy
Using cmd line py -2.7 -m install [package_name]
'''
import os, time, logging
import shutil, fnmatch, datetime
import copy, math
import functools, itertools
import numpy as np 
from Implementations.Loans import *
from Implementations.LoanPool import *
from Implementations.Loan import *
logging.getLogger().setLevel(logging.INFO)

'''===================================================================================================
Main program:
# Exercise 4.3.1
# To practice file management, do the following in order (using Python code):
# a. Create a new directory.
# b. Rename the above directory.
# c. Delete the above directory.
# d. Create another directory and create two text files in this directory.
# e. Delete one of the text files from the above directory.
# f. Rename the remaining text file.
# g. Create a subdirectory within the above created directory.
# h. Move the remaining text file into the subdirectory.
# i. Remove the top level directory with all its contents (using a single function call)

# Exercise 4.3.2
# Write code that searches your entire computer for all files of extension py. Hint: Use os.walk 
# and any necessary string manipulation functions

# Exercise 4.3.3
# Write code that searches your entire computer for all pdf files which reside in any directory 
# (at any level) that contains the string ‘gr’ in its name

# Exercise 4.3.4
# Open a brand-new file and write to it (should write several lines)

# Exercise 4.3.5
# Open the file from 1) and read it. Display each line

# Exercise 4.3.6
# Open the file from 1) and append to it

# Exercise 4.3.7
# Create a program which does the following:
# a. Gives the user a choice of two options: (1) Add Loan, (2) Write file and exit.
# i. If user enters ‘1’, prompt the user for the type of Loan, its asset name/value, its face amount,
# rate, and term. Each prompt should occur one after the other. After the last prompt, save the entry 
# into a Loan object, notify the user that the loan has been recorded, and return to the main menu.
# ii. If user enters ‘2’, loop through all the entered loans and write them to a file. The file should 
# be in extension .csv. To do this properly, each sub-entry (loan type, asset name, asset value, amount, 
# rate, and term) should be separate by a comma. Each loan should be separated by a newline.
# b. To verify that your generated .csv is a valid .csv file, try opening it in Excel once it has been 
# generated. You should see four columns and the number of rows should reflect the number of loans

# Exercise 4.3.8
# As a follow-up, create a third option: (3) Read loan .csv file. This option should:
# a. Ask the user to enter a file path of the loan .csv file.
# b. Load the .csv file into Loan objects.
# c. Add an additional (fourth) option to display the WAR and WAM of all the loans

Implementations:
Implementations are followed by the main() function
==================================================================================================='''

def main():
	# Exercise 4.3.1
	print('\n====================================Exercise 4.3.1=====================================\n');
	print('Step a: creating new dir ... \n');
	os.getcwd();
	os.mkdir('LoanFiles');
	os.mkdir('LoanFiles\\MyCSVFiles');
	raw_input('Program pause. Press enter to continue.\n');

	print('Step b: renaming the dir ... \n');
	os.rename('LoanFiles\\MyCSVFiles','LoanFiles\\LoanFiles')
	raw_input('Program pause. Press enter to continue.\n');

	print('Step c: deleting the dir ... \n');
	os.rmdir('LoanFiles\\LoanFiles');
	raw_input('Program pause. Press enter to continue.\n');

	print('Step d: creating another new dir ... \n');
	os.mkdir('LoanFiles\\MyDir');
	with open('LoanFiles\\MyDir\\file1.txt', 'w') as f:
		f.write('Hello world.\n');
		f.write('Baruch Pre-MFE program is fantastic!\n');
	with open('LoanFiles\\MyDir\\file2.txt','w') as f:
		f.write('My first line.\n');
		f.write('My second line.\n');
	raw_input('Program pause. Press enter to continue.\n');

	print('Step e: deleting one txt file from MyDir ... \n');
	os.remove('LoanFiles\\MyDir\\file2.txt');
	raw_input('Program pause. Press enter to continue.\n');

	print('Step f: renaming another txt file from MyDir ... \n');
	os.rename('LoanFiles\\MyDir\\file1.txt','LoanFiles\\MyDir\\HelloWorld.txt');
	raw_input('Program pause. Press enter to continue.\n');

	print('Step g: creating a subdirectory within the above created directory ... \n');
	os.mkdir('LoanFiles\\MyDir\\DumLoanFiles')
	raw_input('Program pause. Press enter to continue.\n');

	print('Step h: moving the remaining text file into the subdirectory ... \n');
	src='LoanFiles\\MyDir'; dst='LoanFiles\\MyDir\\DumLoanFiles';
	for fname in os.listdir(src):
		if os.path.isfile(os.path.join(src, fname)):
			os.rename(os.path.join(src, fname), os.path.join(dst, fname))
	# shutil.move(src, dst);
	raw_input('Program pause. Press enter to continue.\n');

	print('Step i: remove the top level directory with all its contents (using a single function call) ... \n');
	shutil.rmtree('LoanFiles');
	raw_input('Program pause. Press enter to continue.\n');

	# Exercise 4.3.2
	# Write code that searches your entire computer for all files of extension py. Hint: Use os.walk 
	# and any necessary string manipulation functions
	print('\n====================================Exercise 4.3.2=====================================\n');
	print('Finding the files end with .py  ... \n');
	drive='C:'
	for root, dirs, files in os.walk(drive):
		for file in files:
			if file.endswith(".py"):
				print(os.path.join(root, file))
	raw_input('Program pause. Press enter to continue.\n');

	# Exercise 4.3.3
	# Write code that searches your entire computer for all pdf files which reside in any directory 
	# (at any level) that contains the string ‘gr’ in its name
	print('\n====================================Exercise 4.3.3=====================================\n');
	print('Finding the files end with .pdf and contain gr ... \n');
	drive='C:'
	for root, dirs, files in os.walk(drive):
		for file in files:
			if fnmatch.fnmatch(file, "*.pdf") and fnmatch.fnmatch(file, '[gr]'):
				print(os.path.join(root, file))
	raw_input('Program pause. Press enter to continue.\n');

	# Exercise 4.3.4
	# Open a brand-new file and write to it (should write several lines)
	print('\n====================================Exercise 4.3.4=====================================\n');
	print('Opening a brand new file ... \n');
	with open('newfile.txt','w') as f:
		f.write('My first line. \n');
		f.write('My second line. \n');
		f.write('My third line. \n');
	raw_input('Program pause. Press enter to continue.\n');

	# Exercise 4.3.5
	# Open the file from 1) and read it. Display each line
	print('\n====================================Exercise 4.3.5=====================================\n');
	print('Displaying each line ... \n');
	with open('newfile.txt','r') as f:
		print f.readline();
		print f.readline();
		print f.readline();
	raw_input('Program pause. Press enter to continue.\n');

	# Exercise 4.3.6
	# Open the file from 1) and append to it
	print('\n====================================Exercise 4.3.6=====================================\n');
	print('Appending new lines ... \n');
	with open('newfile.txt','a') as f:
		f.write('This is my fourth line. \n');
		f.write('This is my fifth line. \n');
		f.write('This is my sixth line. \n');
	raw_input('Program pause. Press enter to continue.\n');

	# Exercise 4.3.7 and 4.3.8
	print('\n====================================Exercise 4.3.7 and 4.3.8=====================================\n');
	print('Running my myProgram ... \n');
	myProgram();
	raw_input('Program pause. Press enter to continue.\n');

# Exercise 4.3.7 and 4.3.8 Implementation
def myProgram():
	loanPool=LoanPool()
	while 1 :
		n=raw_input('Welcome to main menu, please choose an option: 1 Add Loan; 2 Write File and Exit; 3 Read loan .csv file; 0 Exit the Program: \n');
		try :
			n=int(n)
		except Exception as e:
			logging.exception('{}. \nIn valid input. Please enter a number between 0 to 3.'.format(e));
		if n>=0 and n<=3:
			if n==0 :
				logging.info('Exiting the program. Have a nice day!\n')
				break
			elif n==1:
				loanPool.loan.append(addLoan())
				logging.debug(loanPool.loan) 
			elif n==2:
				logging.debug(loanPool.loan) 
				writeFile(loanPool)
				# logging.info('Exiting the program. Have a nice day!\n')
				# break
			else :
				while 1:
					try :
						pathfname=raw_input('Welcome to readLoan, please enter the path of your csv file: \n');
						readLoan(pathfname);
						break
					except Exception as e:
						logging.exception('{}. Please enter a valid path.\n'.format(e));

def addLoan():
	while 1:
		try :
			tp=raw_input('Welcome to add loan, please enter the type of loan:(variable for variable rate loan) \n');
			face=raw_input('Please enter loan face amount: \n');
			term=raw_input('Please enter loan term: \n');
			if tp=='variable':
				rateDict=raw_input('Please enter loan rate dict: \n');
				loan=VariableRateLoan(None, face, rateDict, term);
			else :
				rate=raw_input('Please enter loan rate: \n');
				loan=FixedRateLoan(asset=None, face=face, rate=rate, term=term)
			break
		except Exception as e:
			logging.exception('{}. \nIn valid input. Please enter number for face, rate and term.'.format(e));
	logging.info('Your loan has been recorded.\n')
	return loan 

def writeFile(loanPool):
	t=datetime.datetime.today()
	logging.debug(loanPool.loan)
	logging.info('Welcome to write files, the program is writing your csv files ... \n')
	with open('loanfile_{}.csv'.format(t.strftime('%Y%m%d_%H%M')),'w') as f:
		f.write('loan type, asset name, asset value, amount, rate, term\n');
		for l in loanPool.loan:
			lst=[str(type(l)), str(type(l.asset)), str(l.asset.initValue), str(l.face), str(l.rate(1)), str(l.term)];
			logging.debug(lst)
			f.write(', '.join(lst)); f.write('\n');
	logging.info('Your csv files are ready.\n')

def readLoan(pathfname):
	logging.info('Welcome to read loans, the program is reading the loans ... \n')
	loanPool=LoanPool()
	with open(pathfname, 'r') as f:
		f.readline()
		while 1:
			line=f.readline()
			if line=='':
				break
			else :
				lst=line.split(', ')
				logging.debug(lst)
				loan=Loan(None, float(lst[3]), float(lst[4]), float(lst[5]));
				loanPool.loan.append(loan)
	while 1:
		opt=raw_input('Do you want to dispaly WAR and WAM of all the loans?[y/n]: \n');
		if opt=='y':
			logging.info('The WAR is {}; the WAM is {}. \n'.format(loanPool.WAR(), loanPool.WAM()))
			break;
		elif opt=='n':
			break;
		else :
			logging.info('In valid input, please try again.')
	logging.info('Your csv loan data (LoanPool) is ready.\n')
	return loanPool

if __name__=='__main__':
	# myProgram()
	main()