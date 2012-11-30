This is my code for processing all the data for the m0m0 Bowl League. 

To get the sample data, you need to run the following commands:
python processDraft.py 2012_raw_draftresults.txt 2012_processed_draftresults.txt
python processWaivers.py 2012_processed_draftresults.txt 2012_raw_waiverwireresults.txt 2012_processed_waivermoves.txt
python processCompleteRosters.py 2012_processed_waivermoves.txt 2012_raw_currentrosters.txt > 2012_processed_currentrosters.txt

NOTE: Yes, the file names are complete pain in the ass, but better too descriptive than no idea what they do at all.

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