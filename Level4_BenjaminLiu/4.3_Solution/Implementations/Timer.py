# -*- coding: utf-8 -*- 
#!/usr/bin/env python
'''
Student name: Beier (Benjamin) Liu
Date: 2/18/2018
Exercise 4.2.1 and 4.2.2

Remark:
Python 2.7 is recommended
'''
import time 
from datetime import timedelta
import logging
logging.getLogger().setLevel(logging.DEBUG)

'''===================================================================================================
File content:
# Exercise 4.2.1
# Modify your Timer class to use a logging statement (info level) instead of a print statement

# Exercise 4.2.2
# Modify your Timer class as follows:
# a. Add a class-level warnThreshold variable, which defaults to 1 minute.
# b. When printing the time taken, use a warn-level log statement instead of info-level if the 
# time taken exceeds the warn threshold
==================================================================================================='''

class Timer(object):
	_warnThreshold=60; # warnThreshold variable default is 1 min.

	def __init__(self, timerName):
		self._timerName=timerName;
		self._t=None; 
		self._t0=None;
		self._tn=None;
		self._state=False; # False stands for the timer is not activated
		self._history=[];
		self._config=None;

	def __enter__(self):
		self.start()
		return self 


	def __exit__(self, type, value, traceback):
		# logging.info('Exception has been handled. \n');
		self.end();
		return True

	@classmethod
	def getWarnThreshold(cls):
		return cls._warnThreshold

	@classmethod
	def setWarnThreshold(cls, ithreshold):
		cls._warnThreshold=ithreshold

	def configureTimerDisplay(self, *args):
		self._config=args;

	# Not preferred
	def start(self):
		if self._state==False:
			self._t0=time.time();
			self._state=True;
		else :
			logging.error('Warning: The Timer is already started. The function call start() is invalid. \n');

	# Not preferred
	def end(self):
		try :
			self._tn=time.time();
			self._t=self._tn-self._t0;
			self._history.append(self._t);
			if self_t > self._warnThreshold:
				logging.warning('Time elapsed exceeds 60s. {} : {} seconds. \n'.format(self._timerName, self._t))
			else :
				logging.info('Timer stops. {} : {} seconds. \n'.format(self._timerName, self._t));
			# if self._config==None:
			# 	self.display('secs');
			# else :
			# 	self.display(*self._config)
		except Exception as e:
			logging.error('Please use start() before using end(). \n');
		self._t0=None;
		self._state=False;

	# Not preferred
	def display(self, *args):
		try :
			m, s = divmod(self._history[-1], 60)
			h, m = divmod(m, 60)
			if 'secs' in args:
				logging.info('Seconds: {}'.format(s));
			if 'mins' in args:
				logging.info('Minutes: {}'.format(m));
			if 'hrs' in args:
				logging.info('Hours: {}'.format(h));
		except Exception as e:
			logging.error('Error message: {}'.format(e));
			logging.error('No time elapsed to display. \n');

	def retrieve(self, numLast=0):
		try:
			re=self._history[-1-numLast];
			return re
		except Exception as e:
			logging.info('Error message: {}'.format(e));
			logging.info('No timer history found. \n');
