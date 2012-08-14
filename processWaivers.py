#!/usr/bin/env python
# encoding: utf-8
"""
processwaivers.py

Created by Ed Pham on 2011-11-18.
Copyright (c) 2011 __MyCompanyName__. All rights reserved.
"""

import sys
import os
import re
		
# retrieveDraft()
# Used to read the processed draft results from the processDraft.py
# and store it into the program to process the waivers.
def retrieveDraft():
	draft = open(sys.argv[1], 'r')
	size = int(draft.readline())

	players = {}
	teamNames = []
	count = 0

	while True:
		line = draft.readline()
		if not line: break
	
		if count != 0:
			line = line.split()
			players[' '.join(line[0:3])] = line[-1]
		else:
			teamNames.append(line[:-1])
	
		count = count + 1
		if count == size + 1: count = 0

	draft.close()
	return players, teamNames, size

# retrieveWaivers()
# Used to read the waiver results from the league.
def retrieveWaivers():
	readFile = open(sys.argv[2], 'r')
	waivers = []
	
	while True:
		line = readFile.readline().split()
		if not line: break
		if re.search('\d+\.', line[0]) != None: line = line[1:]
		line = ' '.join(line)
		if re.search('Unsuccessful', line) == None: waivers.append(line)
				
	readFile.close()
	return waivers

def processWaivers(waivers, teams, players):
	freeAgents = {}
	
	for waiver in waivers:
		teamName = ''
		player = ''
		price = ''
		
		for team in teams:
			if re.search(team, waiver, re.I) != None: teamName = team
		
		pattern = re.compile(teamName, re.I)
		processed = pattern.sub('', waiver.replace('*', '')).split()
	
		player = ' '.join(processed[0:3])
		
		if processed[2] == 'D/ST':
			price = processed[3]
		else:
			price = processed[4]
		
		if player not in players: 
			players[player] = price
			freeAgents[player] = price
		
	return players, freeAgents
			
def outputResults(players, name, size):
	output = open(name, 'w')
	output.write(str(size) + '\n')
	for player in players: output.write(player + '\t' + players.get(player) +'\n')
	output.close()
			
players, teams, size = retrieveDraft()
waivers = retrieveWaivers()
processed, FAs = processWaivers(waivers, teams, players)
outputResults(processed, sys.argv[3], size)
