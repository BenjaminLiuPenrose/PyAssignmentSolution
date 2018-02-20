# -*- coding: utf-8 -*- 
#!/usr/bin/env python
'''
Student name: Beier (Benjamin) Liu
Date: 18/2/2018
Exercise 6.1.3

Remark:
Python 2.7 is recommended
Before running please install packages *numpy
Using cmd line py -2.7 -m install [package_name]
'''
import os, time, logging
import copy, math
import functools, itertools
import numpy as np 
logging.getLogger().setLevel(logging.DEBUG)

'''===================================================================================================
File content:
# Exercise 6.1.3 PlayerGame Implementations
==================================================================================================='''

class Player(object):
	def __init__(self, name='Player One', typ='Hold'):
		self._name=name
		self._type=typ
		self._doorNum=None
		self._payoff=0

	@property
	def name(self):
		return self._name

	@name.setter
	def name(self, iName):
		logging.debug('You are trying to rename player to {}.'.format(iName));
		self._name=iName;

	@property
	def doorNum(self):
		return self._doorNum

	@doorNum.setter
	def doorNum(self, iDoorNum):
		logging.debug('You are trying to change to Door {}.'.format(iDoorNum));
		self._doorNum=iDoorNum;

	@property
	def payoff(self):
		return self._payoff

	@payoff.setter
	def payoff(self, iPayoff):
		logging.debug('You are trying to change payoff.');
		self._payoff=iPayoff; 

	def firstChoice(self):
		logging.debug('{} is making first choice ... '.format(self.name));
		self.doorNum=np.random.randint(1, 4);
		logging.debug('{} chooses Door {}'.format(self.name, self.doorNum));
		return self.doorNum

	def strategy(self):
		logging.debug('{} is considering whether or not to switch door ...'.format(self.name))
		switch=0;
		if self._type=='Switch':
			switch=1;
		# num=np.random.uniform(0,1)
		# if num>=0.5:
		# 	switch=1;
		# else :
		# 	switch=0;
		logging.debug('{} decides{}to change his choice.'.format(self.name, '' if switch==1 else ' not '));
		return switch


def Timer(func):
	@functools.wraps(func)
	def wrapped(*args, **kwargs):
		s=time.time()
		res=func(*args, **kwargs);
		e=time.time()
		logging.debug('{}: {} seconds.'.format(func, e-s))
		return res
	return wrapped



class Game(object):
	def __init__(self, player):
		pass
		if isinstance(player, Player):
			self._player=player;
		else:
			logging.error('The player does not belong to Player class.\n');
		self._payoff=0; # 1 for Lamborghini, 0 for o/w
		self._door={1:'Goat', 2:'Goat', 3:'Goat'}
		self._luckyDoor=None;

	@property
	def player(self):
		return self._player

	@player.setter
	def player(self, iPlayer):
		logging.debug('You are trying to change player.');
		self._player=iPlayer;

	@property
	def payoff(self):
		return self._payoff

	@payoff.setter
	def payoff(self, iPayoff):
		logging.debug('You are trying to change payoff.');
		self._payoff=iPayoff; 

	@property
	def luckyDoor(self):
		return self._luckyDoor

	@luckyDoor.setter
	def luckyDoor(self, iLuckyDoor):
		logging.debug('You are trying to change the luckyDoor.');
		self._luckyDoor=iLuckyDoor; 

	@property
	def door(self):
		return self._door 

	def gameInit(self):
		luckyDoor=np.random.randint(1, 4);
		self.door[luckyDoor]='Lamborghini';
		self.luckyDoor=luckyDoor
		return luckyDoor

	def openOneDoor(self, chDoor, luckyDoor):
		while 1:
			openDoor=np.random.randint(1, 4)
			if openDoor!=chDoor and openDoor!=luckyDoor:
				return openDoor

	def clearing(self, chDoor):
		if chDoor==self.luckyDoor:
			self.payoff=1;
		else :
			self.payoff=0;
		logging.debug('{} gets {}. The game payoff is {}.'.format(self.player.name, self.door[chDoor], self.payoff))
		return self.payoff

	@Timer
	def playGame(self):
		# Stage 1 
		# Randomly places the prize behind one of three doors.
		logging.debug('Game initialization stage. The host is setting the game.');
		luckyDoor=self.gameInit()
		logging.debug('Game begins. Welcome, {}.\nThere are three doors and the door numbers are 1, 2, 3. Please make your first choice.'.format(self.player.name));
		# Asks its player object to choose a door
		chDoor=self.player.firstChoice()
		# Figure out which door to ‘open
		logging.debug('Door {} is chosen. Let us check what is behind the door that is not chosen.'.format(chDoor));
		openDoor=self.openOneDoor(chDoor, luckyDoor)
		logging.debug('Door {} is open. Behind the door is {}.'.format(openDoor, self.door[openDoor]));

		# Stage 2
		logging.debug('{}, I will give you a chance to switch. Would you like to switch to the other door?'.format(self.player.name));
		switch=self.player.strategy()
		if switch==1:
			for i in [1, 2, 3]:
				if i!=openDoor and i!=chDoor:
					self.player.doorNum=i;
					chDoor=self.player.doorNum;
			logging.debug('{} decides to switch to Door {}'.format(self.player.name, chDoor))
		else :
			logging.debug('{} decides to keep the Door {}'.format(self.player.name, chDoor))

		# Stage 3 Check if the final chosen door is a winner or loser and return the Boolean result
		payoff=self.clearing(chDoor)
		self.player.payoff=payoff
		if payoff==1:
			logging.debug('{} wins the game.'.format(self.player.name))
		else :
			logging.debug('{} does not win the game.'.format(self.player.name))
		return True if payoff==1 else False
