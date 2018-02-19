# -*- coding: utf-8 -*- 
#!/usr/bin/env python
'''
Student name: Beier (Benjamin) Liu
Date: 
Exercise 

Remark:
Python 2.7 is recommended
'''
import time 
from datetime import timedelta
import logging
logging.getLogger().setLevel(logging.DEBUG)

'''===================================================================================================
File content:

==================================================================================================='''

class Timer(object):
	_warnThreshold=60;

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

	@property
	def timerName(self):
		return self._timerName

	@timerName.setter
	def timerName(self, iTimerName):
		self._timerName=iTimerName;

	@property
	def config(self):
		return self._config

	@property
	def t0(self):
		return self._t0

	@property
	def tn(self):
		return self._tn

	@property
	def state(self):
		return self._state

	@classmethod
	def getWarnThreshold(cls):
		return cls._warnThreshold

	@classmethod
	def setWarnThreshold(cls, iWarnThreshold):
		cls._warnThreshold=iWarnThreshold;

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
			if self._t > self._warnThreshold:
				logging.warning('Time elapsed exceeds 60s. {} : {} seconds. \n'.format(self._timerName, self._t))
			else :
				logging.info('Timer stops. {} : {} seconds. \n'.format(self._timerName, self._t));
			if self._config==None:
				self.display('secs');
			else :
				self.display(*self._config)
		except Exception as e:
			logging.exception('{} \nPlease use start() before using end(). \n'.format(e));
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
