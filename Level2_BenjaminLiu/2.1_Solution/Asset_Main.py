# -*- coding: utf-8 -*- 
#!/usr/bin/env python
'''
Student name: Beier (Benjamin) Liu
Date: 2/14/2018
Exercise 2.1.6

Remark:
Python 2.7 is recommended
'''
from Implementations.Assets.Asset import *

'''===================================================================================================
Main program:
# Exercise 2.1.6
# Create a class called Asset. This class will represent the Asset covered by the loan. The class 
# should do the following:
# a. Save an initial asset value upon object initialization (i.e. the initial value of a car).
# b. Create a method that returns a yearly depreciation rate (i.e., 10%).
# c. Create a method that calculates the monthly depreciation rate, from the yearly depreciation rate.
# d. Create a method that returns the current value of the asset, for a given period

Implementations:
See file 2.1_Solution\Implementations\Assets\Asset.py
==================================================================================================='''


def main():
	# Exercise 2.1.6
	print('\n====================================Exercise 2.1.6=====================================\n');
	# a) Save an initial asset value upon object initialization (i.e. the initial value of a car)
	print('Step a: Saving an initial asset value  ... \n');
	asset=Asset(initValue=1000000, yearlyDepre=0.36);
	print('The initial asset value is {}. \n'.format(asset.initValue))
	raw_input('Program pause. Press enter to continue.\n');

	# b) Create a method that returns a yearly depreciation rate
	print('Step b: Using my yearlyDepre method  ... \n');
	print('The yearly depreciation rate is {}. \n'.format(asset.yearlyDepre))
	raw_input('Program pause. Press enter to continue.\n');

	# c) Create a method that calculates the monthly depreciation rate, from the yearly depreciation rate
	print('Step c: Using my monthlyToYearly method  ... \n');
	print('The monthly depreciation rate is {}. \n'.format(Asset.yearlyToMonthly(asset.yearlyDepre)))
	raw_input('Program pause. Press enter to continue.\n');

	# d) Create a method that returns the current value of the asset, for a given period
	print('Step d: Using my getPresValue method  ... \n');
	print('The present value of asset at month {} is {}. \n'.format(12, round(asset.getPresValue(period=12), 2)));
	raw_input('Program pause. Press enter to continue.\n');

if __name__=='__main__':
	main()
