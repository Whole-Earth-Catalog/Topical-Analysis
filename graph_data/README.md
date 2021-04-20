# Data for graphing
The full tsvs and csvs (with duplicates in centuries) are in the tsv and csv files. These files have the top 20 subjects for each cluster in each century. An example for how to get this data is in the sql folder.

The clusters without duplicate subjects within the century are in no_dupes. To see the output
of remove_duplicates.py look at out.txt (it has stats on what was removed). 

## remove_duplicates.py
String based deduplication of subjects within a century and creates files in no_dupes without the duplicates. This is a good example of a quick python script that helps with cleaning data.
