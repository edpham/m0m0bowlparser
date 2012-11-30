#!/usr/bin/env python
# encoding: utf-8
"""
untitled.py

Created by Ed Pham on 2011-11-18.
Copyright (c) 2011 __MyCompanyName__. All rights reserved.
"""

import sys
import os

current = open(sys.argv[2], 'r')
players = open(sys.argv[1], 'r')

size = int(players.readline())
allPlayers = {}

for line in players:
	line = line.split()
	allPlayers[' '.join(line[0:3])] = line[3]
	
count = 0
teamName = ''

for line in current:
	if line.split() != []:
		if teamName == '': 
			teamName = ' '.join(line.split()[:-1])
			print teamName
		elif line.startswith('SLOT') or line.startswith('Propose'):
			pass
		else:
			if line.split() > 1:
				player = ' '.join(line.split()[1:4]).replace('*', '')
				print player + '\t' + allPlayers.get(player, '')
				if player != '': del allPlayers[player]
			else:
				pass
	else:
		teamName = ''
		print '\n****\n'
		
print '\nFREE AGENTS'

freeAgents = allPlayers.keys()
freeAgents.sort()

for player in freeAgents: print player + '\t' + allPlayers.get(player)	

players.close()
current.close()
