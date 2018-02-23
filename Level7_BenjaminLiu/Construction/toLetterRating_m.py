# -*- coding: utf-8 -*- 
#!/usr/bin/env python
'''
Student name: Beier (Benjamin) Liu
Date:
Project Part

Remark:
Python 2.7 is recommended
Before running please install packages *numpy
Using cmd line py -2.7 -m install [package_name]
'''
import os, time, logging
from math import exp, sqrt
import functools, itertools
import numpy as np 
logging.getLogger().setLevel(logging.DEBUG)

'''===================================================================================================
File content:
Write comments
==================================================================================================='''

'''===================================================================================================
Implementation for Part2 toLetterRating
==================================================================================================='''
def toLetterRating(DIRR):
	DIRR*=10000.0;
	letter=['Aaa','Aa1','Aa2','Aa3','A1','A2','A3','Baa1','Baa2','Baa3','Ba1','Ba2','Ba3','B1','B2','B3','Caa','Ca'];
	threshold=[0.06, 0.67,1.3,2.7,5.2,8.9,13.0,19.0,27.0,46.0,72.0,106.0,143.0,183.0,231.0,311.0,2500.0,10000.0];
	letter_rate='Unknown';
	cnt=0;
	while cnt < len(threshold):
		if DIRR < 0:
			letter_rate='N/A';
			break
		if DIRR <= threshold[cnt]:
			letter_rate=letter[cnt];
			break
		cnt+=1;
	return letter_rate