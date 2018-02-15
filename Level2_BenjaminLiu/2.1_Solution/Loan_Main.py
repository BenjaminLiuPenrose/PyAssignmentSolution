# -*- coding: utf-8 -*- 
#!/usr/bin/env python
'''
Student name: Beier (Benjamin) Liu
Date: 2/14/2018
Exercise 2.1.2 - 2.1.5

Remark:
Python 2.7 is recommended
Before running please install packages
Using cmd line py -2.7 -m install [package_name]
'''
from Implementations.Loans.Loan import *
from Implementations.Timer import *

'''===================================================================================================
Main program:
# Exercise 2.1.2
# Create a basic Loan class exactly as demonstrated in the lecture (including the setter/getter property methods). 
# Then, extend it with methods that return the following (refer to the slides for any necessary formulas):
# a. The monthly payment amount of the Loan (monthlyPayment). Even though monthlyPayment is likely to be equal for 
# all months, you should still define this with a dummy ‘period’ parameter, since it’s possible some loan types will 
# have a monthly payment dependent on the period.
# b. The total payments of the Loan (totalPayments). This is principal plus interest.
# c. The total interest of the Loan (totalInterest).

# Exercise 2.1.3
# Interest due at time T on a loan depends on the outstanding balance. Principal due is the monthly payment 
# less the interest due. Conceptually, these are recursive calculations as one can determine the interest/principal 
# due at time T if one knows the balance at time T-1 (which, in turn, can be determined if one knows the balance 
# at time T-2).
# For each of the below functions, implement two versions: A recursive version (per the above statement) and a 
# version that uses the formulas provided in the slides:
# a. The interest amount due at a given period (interestDue).
# b. The principal amount due at a given period (principalDue).
# c. The balance of the loan at a given period (balance).
# Use your Timer class to time each version of each function; what do you observe? What happens as the time period increases?

# Exercise 2.1.4
# To demonstrate understanding of class-level methods, do the following:
# a. Implement a class-level method called calcMonthlyPmt, in the Loan base class. This should calculate a monthly 
# payment based on three parameters: face, rate, and term.
# b. Create a class-level function, in the Loan base class, which calculates the balance (calcBalance). Input 
# parameters should be face, rate, term, period.
# c. Test the class-level methods in main.
# d. Modify the object-level methods for monthlyPayment and balance to delegate to the class-level methods.
# e. Test the object-level methods to ensure they still work correctly.
# f. What are the benefits of class-level methods? When are they useful?

# Exercise 2.1.5
# To demonstrate understanding of static-level methods, do the following:
# a. Create a static-level method in Loan called monthlyRate. This should return the monthly interest 
# rate for a passed-in annual rate
# b. Create another static-level method that does the opposite (returns an annual rate for a passed-in monthly rate).
# c. Test the static-level method in main.
# d. Modify all the Loan methods that rely on the rate to utilize the static-level rate functions.
# e. What are the benefits of static-level methods? When are they useful?

Implementations:
See file 2.1_Solution\Implementations\Loans\Loan.py
==================================================================================================='''

def main():
	# Exercise 2.1.2
	# Create a loan for the whole demo with face=1000000, APR=.035 and term=360 months
	loan=Loan(None, face=1000000, rate=0.035, term=360);

	# a) Use a method to compute monthly payment
	print('\n====================================Exercise 2.1.2=====================================\n');
	print('Step a: Running my monthlyPayment method ... \n');
	pmt=round(loan.monthlyPayment(period=24), 2); #period is a dummy variable 
	print('The monthly payment is {}. \n'.format(pmt));
	raw_input('Program pause. Press enter to continue.\n');

	# b) Use a method to compute total payment
	print('Step b: Running my totalPayments method ... \n');
	pmtTtl=round(loan.totalPayments(period=24), 2);
	print('The total payment is {}. \n'.format(pmtTtl));
	raw_input('Program pause. Press enter to continue.\n');

	# c) Use a method to compute total interest
	print('Step c: Running my totalInterest method ... \n');
	instTtl=round(loan.totalInterest(), 2);
	print('The total interest is {}. \n'.format(instTtl));
	raw_input('Program pause. Press enter to continue.\n');

	# Exercise 2.1.3
	print('\n====================================Exercise 2.1.3=====================================\n');
	# Create three timers for interest due, principal due and balance computation respectively
	t_inst=Timer(); t_prin=Timer(); t_bala=Timer();
	print('Part 1: Running my formulas evaluation approach ... \n');
	print('Step a: Running my interestDueFoml method ... ');
	t_inst.start(); instDue=loan.interestDueFoml(period=24); t_inst.end();
	print('The interest due for period {} is {}. '.format(24, round(instDue, 2)));
	print('Step b: Running my principalDueFoml method ... ');
	t_prin.start(); principalDue=loan.principalDueFoml(period=24); t_prin.end();
	print('The principal due for period {} is {}. '.format(24, round(principalDue, 2)));
	print('Step c: Running my balanceFoml method ... ');
	t_bala.start(); balance=loan.balanceFoml(period=24); t_bala.end();
	print('The balance for period {} is {}. \n'.format(24, round(balance, 2)));
	raw_input('Program pause. Press enter to continue.\n');

	print('Part 2: Running my recursive approach ... \n');
	print('Step a: Running my interestDueRecur method ... ');
	t_inst.start(); instDue=loan.interestDueRecur(period=24); t_inst.end();
	print('The interest due for period {} is {}. '.format(24, round(instDue)));
	print('Step b: Running my principalDueRecur method ... ');
	t_prin.start(); principalDue=loan.principalDueRecur(period=24); t_prin.end();
	print('The principal due for period {} is {}. '.format(24, round(principalDue)));
	print('Step c: Running my balanceRecur method ... ');
	t_bala.start(); balance=loan.balanceRecur(period=24); t_bala.end();
	print('The balance for period {} is {}. \n'. format(24, round(balance)));
	raw_input('Program pause. Press enter to continue.\n');

	print('Part 3: Comparing two costs of approachs to Implementations of method balance ... \n');
	t_1=Time(); t_2=Timer();
	for perid in range(360+1):
		t_1.start(); balance=loan.balanceFoml(period=perid); t_1.end();
		t_2.start(); balance=loan.balanceRecur(period=perid); t_2.end();
	raw_input('Program pause. Press enter to continue.\n');

	print('Part 4: Comparing two costs of approachs ... \n');
	print('Costs of formula approach are {}, {}, {} respectively. ' \
		.format(t_inst.retrieve(1), t_prin.retrieve(1), t_bala.retrieve(1)));
	print('Costs of recursive approach are {}, {}, {} respectively. ' \
		.format(t_inst.retrieve(0), t_prin.retrieve(0), t_bala.retrieve(0)));
	print('As period increases, the cost of recursive method increases rapidly')
	raw_input('Program pause. Press enter to continue.\n');

	# Exercise 2.1.4
	print('\n====================================Exercise 2.1.4=====================================\n');
	# a) Implement a class-level method called calcMonthlyPmt, in the Loan base class. This should calculate a monthly 
	# payment based on three parameters: face, rate, and term
	print('Step a: Running my calcMonthlyPmt class method ... \n');
	pmt=Loan.calcMonthlyPmt(face=1000000, rate=0.035, term=360);
	print('The monthly payment is {}. \n'.format(round(pmt, 2)));
	raw_input('Program pause. Press enter to continue.\n');

	# b) Create a class-level function, in the Loan base class, which calculates the balance (calcBalance). Input 
	# parameters should be face, rate, term, period
	print('Step b: Running my calcBalance class method ... \n');
	balance=Loan.calcBalance(face=1000000, rate=0.035, term=360, period=24);
	print('The balance is {}. \n'.format(round(balance, 2)));
	raw_input('Program pause. Press enter to continue.\n');

	# c) Test the class-level methods in main
	print('Step c: Test the class-level methods in main. \n');
	print('This part is shown in step (a) and (b). \n');
	raw_input('Program pause. Press enter to continue.\n');

	# d) Modify the object-level methods for monthlyPayment and balance to delegate to the class-level methods
	# e) Test the object-level methods to ensure they still work correctly.
	print('Step d and e: Running my monthlyPayment2 object-level method ... \n');
	pmt=Loan.monthlyPayment2(loan, period=24);
	print('The monthly payment is {}. \n'.format(round(pmt, 2)));
	raw_input('Program pause. Press enter to continue.\n');

	# f) What are the benefits of class-level methods? When are they useful?
	print('Step f: The benefits of class-level methods. \n');
	print('The class methods can be called on the class itself and does not know about any object istance. \
		It applied to all past, present and future objects of the class. ');
	print('Useful for methods that are related to the class but not logically meant to perform on a \
		instantiated object. ');
	raw_input('The demo successfully finished. Press press any key to exit.\n');

	# Exercise 2.1.5
	# Write comments
	print('\n====================================Exercise 2.1.5=====================================\n');
	# a) Create a static-level method in Loan called monthlyRate. This should return the monthly interest 
	# rate for a passed-in annual rate
	print('Step a: Running my monthlyRate static method ... \n');
	monthlyRate();
	raw_input('Program pause. Press enter to continue.\n');

	# b) Create another static-level method that does the opposite (returns an annual rate for a passed-in monthly rate)
	print('Step b: Running my annualRate static method ... \n');
	annualRate();
	raw_input('Program pause. Press enter to continue.\n');

	# c) Test the static-level method in main.
	print('Step c: Test the static-level methods in main. \n');
	print('This part is shown in step (a) and (b). \n');
	raw_input('Program pause. Press enter to continue.\n');

	# d) Modify all the Loan methods that rely on the rate to utilize the static-level rate functions
	# Create a new class Loan2 to modify all the Loan2 methdos that rely on rate with help of static rate functions
	loan2=Loan2(None, 1000000, 0.035, 360);
	print('The monthly payment is '+str(loan2.monthlyPayment(period=24))+'\n');
	print('The total payment is '+str(loan2.totalPayments(period=24))+'\n');
	print('The total interest is '+str(loan2.totalInterest())+'\n');
	print('The interest due for period 24 is '+str(loan2.interestDueFoml(period=24))+'\n');
	print('The principal due for period 24 is '+str(loan2.principalDueFoml(period=24))+'\n');
	print('The balance for period is '+str(loan2.balanceFoml(period=24))+'\n');
	print('The interest due for period 24 is '+str(loan2.interestDueRecur(period=24))+'\n');
	print('The principal due for period 24 is '+str(loan2.principalDueRecur(period=24))+'\n');
	print('The balance due for period 24 is '+str(loan2.balanceRecur(period=24))+'\n');

	# e) What are the benefits of static-level methods? When are they useful?
	print('Step e: The benefits of static-level methods. \n');
	print('The static-level methods will not aware of any object instantiate \
		of over even the class itself.');
	print('Useful for grouping related functions together which may not logically from a class. ');
	raw_input('The demo successfully finished. Press press any key to exit.\n');


if __name__=='__main__':
	main()
