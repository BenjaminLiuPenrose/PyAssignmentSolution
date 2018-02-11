# -*- coding: utf-8 -*- 
#!/usr/bin/env python
'''
Student name: Beier (Benjamin) Liu
Date:
Exercise 4.1.5

Remark:
Python 2.7 is recommended
'''
import time 
import logging

'''===================================================================================================
File content:
# Exercise 4.1.5 implementation
# Convert your Timer class’ print statement to use format flags or the format function, instead of concatenating strings
==================================================================================================='''

# Exercise 4.1.5 implementation
class Timer(object):
	def __init__(self):
		self._t=None; # t elapsed
		self._t0=None; # start time
		self._tn=None; # end time
		self._state=False; # False stands for the timer is not activated
		self._history=[]; # timer record

	def start(self):
		if self._state==False:
			self._t0=time.time();
			self._state=True;
		else :
			logging.warn('Warning: The Timer is already started. The function call start() is invalid. \n');

	def end(self):
		try :
			self._tn=time.time();
			self._t=self._tn-self._t0;
			self._history.append(self._t);
			print( 'Timer stops and the seconds elapsed are {}'.format(self._t) ); # modification 
		except Exception as e:
			print('Please use start() before using end(). \n');
		self._t0=None;
		self._state=False;

	def display(self, *args):
		try :
			m, s = divmod(self._history[-1], 60)
			h, m = divmod(m, 60)
			if 'seconds' in args:
				print('Seconds: {} \n'.format(s)); # modification
			if 'minutes' in args:
				print('Minutes: {} \n'.format(m)); # modification
			if 'hours' in args:
				print('Hours: {} \n'.format(h)); # modification
		except Exception as e:
			print('Error message: {}'.format(e)); # modification
			print('No time elapsed to display. \n');

	def retrieve(self, numLast=0):
		try:
			re=self._history[-1-numLast];
			return re
		except Exception as e:
			print('Error message: {}'.format(e)); # modification
			print('No timer history found. \n');
