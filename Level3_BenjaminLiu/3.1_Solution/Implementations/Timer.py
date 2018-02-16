# -*- coding: utf-8 -*- 
#!/usr/bin/env python
'''
Student name: Beier (Benjamin) Liu
Date:
Exercise 2.1.1

Remark:
Python 2.7 is recommended
Before running please install packages
Using cmd line py -2.7 -m install [package_name]
'''
import time 
from datetime import timedelta
import warnings

'''===================================================================================================
File content:
# Exercise 2.1.1 implementation
# a. Create a class called Timer.
# b. Add a start method and end method. They should work as follows:
# c. Note that start should give an error if the Timer is already started and end should give an error if the 
# Timer is not currently running.
# d. Add the ability to configure the Timer to display either seconds, minutes, or hours.
# e. Add a method to retrieve the last timer result.
# f. Test your class thoroughly.
==================================================================================================='''

# Exercise 2.1.1 implementation
# a) Create a class called Timer
class Timer(object):
	def __init__(self):
		self._t=None; 
		self._t0=None;
		self._tn=None;
		self._state=False; # False stands for the timer is not activated
		self._history=[];

	# b) Add a start method and end method
	# c) Note that start should give an error if the Timer is already started and end should give an error if the 
	# Timer is not currently running
	def start(self):
		if self._state==False:
			self._t0=time.time();
			self._state=True;
		else :
			warnings.warn('Warning: The Timer is already started. The function call start() is invalid. \n');

	def end(self):
		try :
			self._tn=time.time();
			self._t=self._tn-self._t0;
			self._history.append(self._t);
			print( 'Timer stops and the seconds elapsed are '+str(self._t) );
		except Exception as e:
			# print('Error message: '+str(e));
			print('Please use start() before using end(). \n');
		self._t0=None;
		self._state=False;

	# d) Add the ability to configure the Timer to display either seconds, minutes, or hours
	def display(self, *args):
		try :
			m, s = divmod(self._history[-1], 60)
			h, m = divmod(m, 60)
			if 'seconds' in args:
				print('Seconds: '+str(s)+'\n');
			if 'minutes' in args:
				print('Minutes: '+str(m)+'\n');
			if 'hours' in args:
				print('Hours: '+str(h)+'\n');
		except Exception as e:
			print('Error message: '+str(e));
			print('No time elapsed to display. \n');

	# e) Add a method to retrieve the last timer result
	def retrieve(self, numLast=0):
		try:
			re=self._history[-1-numLast];
			return re
		except Exception as e:
			print('Error message: '+str(e));
			print('No timer history found. \n');
