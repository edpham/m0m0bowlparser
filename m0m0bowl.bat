python processDraft.py %1_raw_draftresults.txt %1_processed_draftresults.txt %2
python processWaivers.py %1_processed_draftresults.txt %1_raw_waiverwireresults.txt %1_processed_waivermoves.txt
python processCompleteRosters.py %1_processed_waivermoves.txt %1_raw_currentrosters.txt > %1_processed_currentrosters.txt
pause