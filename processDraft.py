#!/usr/bin/env python
# encoding: utf-8
"""
teamrosters.py

Created by Ed Pham on 2011-11-17.
Copyright (c) 2011. All rights reserved.
"""

import sys
import os

# teamRoster()
# Class used to store the team names and their rosters
class teamRoster:
	def __init__(self):
		self.name = ''
		self.roster = {}
	
	def setName(self, name):
		self.name = name
	
	def getName(self):
		return self.name
		
	def getRoster(self):
		return self.roster
		
	def addPlayer(self, name, price):
		self.roster[name] = price

# processRosters()
# Used to process the raw draft results from the ESPN drafts, parsing on player name,
# team name, and price only.
def processRosters(size, count):
	results = open(sys.argv[1], 'r')
	rosters = []
	roster = teamRoster()

	while True: 
		line = results.readline()
		line = line.replace('*', '').replace('\n', '')
		if not line: break

		if count == 0:
			roster.setName(line)	
		else: 
			line = line.split()
			roster.addPlayer(' '.join(line[1:4]), line[-1])

		count = count + 1
		
		if count == size + 1: 
			count = 0
			rosters.append(roster)
			roster = teamRoster()
	
	results.close()
	return rosters

# writeRosters()
# Used to write out the processed draft results to a .txt file
def writeRosters(draft, size):
	output = open(sys.argv[2], 'w')
	output.write(str(size) + '\n')
	
	for team in draft:
		output.write(str(team.getName()) + '\n')
		roster = team.getRoster()
		for player in roster: output.write(str(player) + '\t' + str(roster.get(player)) + '\n')
			
	output.close()
	

rostersize = input('Number of players on the roster? ')
count = 0

draft = processRosters(rostersize, count)
writeRosters(draft, rostersize)
	
