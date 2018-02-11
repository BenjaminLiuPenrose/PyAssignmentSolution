# -*- coding: utf-8 -*- 
#!/usr/bin/env python
'''
Student name: Beier (Benjamin) Liu
Date:
Exercise 4.2.1 to 4.2.2

Remark:
Python 2.7 is recommended
# context manager for Timer class
'''
import time 
import logging
logging.getLogger().setLevel(logging.DEBUG)

'''===================================================================================================
File content:
This file contants modification to Timer class required by 
# Exercise 4.2.1 implementation
# Modify your Timer class to use a logging statement (info level) instead of a print statement

# Exercise 4.2.2 implementation
# Modify your Timer class as follows:
# a. Add a class-level warnThreshold variable, which defaults to 1 minute.
# b. When printing the time taken, use a warn-level log statement instead of info-level 
# if the time taken exceeds the warn threshold
==================================================================================================='''

# Exercise 4.2.1 and 4.2.2 implementation
class Timer(object):
	# Add a class-level warnThreshold variable, which defaults to 1 minute
	self._warnThreshold=60;

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
			logging.error('Warning: The Timer is already started. The function call start() is invalid. \n'); # modification 

	def end(self):
		try :
			self._tn=time.time();
			self._t=self._tn-self._t0;
			self._history.append(self._t);
			# warn-level log statement instead of info-level if the time taken exceeds the warn threshold
			if self._t < self._warnThreshold:
				logging.info('Timer stops and the seconds elapsed are {}'.format(self._t)); # modification 
			else :
				logging.warn('The elapsed time is {0}s, which has exceeded the threshold {1}s'\
					.format(self._t, self._warnThreshold));
		except Exception as e:
			logging.exception('Please use start() before using end(). \n'); # modification 
		self._t0=None;
		self._state=False;

	def display(self, *args):
		try :
			m, s = divmod(self._history[-1], 60)
			h, m = divmod(m, 60)
			if 'seconds' in args:
				logging.info('Seconds: {} \n'.format(s)); # modification
			if 'minutes' in args:
				logging.info('Minutes: {} \n'.format(m)); # modification
			if 'hours' in args:
				logging.info('Hours: {} \n'.format(h)); # modification
		except Exception as e:
			logging.exception('Error message: {}'.format(e)); # modification
			logging.info('No time elapsed to display. \n'); # modification 

	def retrieve(self, numLast=0):
		try:
			re=self._history[-1-numLast];
			return re
		except Exception as e:
			logging.exception('Error message: {}'.format(e)); # modification
			logging.info('No timer history found. \n'); # modification 
