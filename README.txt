processDraft.py
Command: python processDraft.py [raw_draft] [processed_draft]
[raw_draft] = the copied draft results.
[processed_draft] = the outputted processed draft results

processWaivers.py
Command: python processWaivers.py [processed_draft] [raw_waivers] [processed_waivers]
[processed_draft] = the outputted processed draft results from processDraft.py
[raw_waivers] = the copied waiver moves from ESPN for each week.
[processed_waivers] = all the waivers processed with the updated values for each player on the waivers.

processCompleteRosters.py
Command python processCompleteRosters.py [processed_waivers] [raw_completed_rosters] > [output]
[processed_waivers] = all the waivers processed with the updated values for each player on the waivers.
[raw_completed_rosters] = the copied current rosters of all the teams from ESPN.com
[output] = the final output of all the values of the players and the free agents.