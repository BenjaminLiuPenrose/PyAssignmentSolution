# -*- coding: utf-8 -*- 
#!/usr/bin/env python
'''
Student name: Beier (Benjamin) Liu
Date: 

Remark:
Python 2.7 is recommended
'''
import os, time, logging
import copy, math
import functools, itertools
import numpy as np 
from datetime import timedelta
logging.getLogger().setLevel(logging.DEBUG)
'''===================================================================================================
File content:

==================================================================================================='''
class Timer(object):
	_warnThreshold=60;

	def __init__(self, timerName):
		self._timerName=timerName;
		self._elap=None; 
		self._s=None;
		self._e=None;
		self._state=False; # False stands for the timer is not activated
		self._history=[];
		self._config=None;

	def __enter__(self):
		self.start()
		return self 
	def __exit__(self, type, value, traceback):
		self.end();
		return True

	@property
	def timerName(self):
		return self._timerName
	@timerName.setter
	def timerName(self, itimerName):
		self._timerName=itimerName;
	@property
	def s(self):
		return self._s
	@property
	def e(self):
		return self._e
	@property
	def state(self):
		return self._state

	@classmethod
	def getWarnThreshold(cls):
		return cls._warnThreshold
	@classmethod
	def setWarnThreshold(cls, iwarnThreshold):
		cls._warnThreshold=iwarnThreshold;

	def getConfig(self):
		return self._config
	def configureTimerDisplay(self, *args):
		self._config=args;

	def start(self):
		if self._state==False:
			self._s=time.time();
			self._state=True;
		else :
			logging.error('Warning: The Timer is already started. The function call start() is invalid.');

	def end(self):
		try :
			self._e=time.time();
			self._elap=self._e-self._s;
			self._history.append(self._elap);
			if self._elap > self._warnThreshold:
				logging.warning('Time elapsed exceeds 60s. {} : {} seconds. \n'.format(self._timerName, self._elap))
			else :
				logging.info('Timer stops. {} : {} seconds. \n'.format(self._timerName, self._elap));
			if self._config==None:
				self.display('secs');
			else :
				self.display(*self._config)
		except Exception as e:
			logging.exception('{} \nPlease use start() before using end().'.format(e));
		self._s=None;
		self._e=None;
		self._state=False;

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
			logging.exception('Error message: {}'.format(e));
			logging.error('No time elapsed to display.');

	def retrieve(self, numLast=0):
		try:
			re=self._history[-1-numLast];
			return re
		except Exception as e:
			logging.info('Error message: {}'.format(e));
			logging.info('No timer history found. \n');

