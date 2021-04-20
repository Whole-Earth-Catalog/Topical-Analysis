# Topical-Analysis

This repository houses code for the clustering over time project conducted by Samyu and Vasco in Spring 2021. 

The structure of the code is as follows:
## clustering.py
This Python file can be run using the following command structure: ```python3 clustering.py [tsv file to import data from] [number of clusters (k)] [elbow plot figurename]```

The TSV file to import data from will need to be in the following format for this code to work:
id | title 

The number of clusters is selected before the code is run; the [elbow plot](https://en.wikipedia.org/wiki/Elbow_method_(clustering)) is helpful in making this selection. 

The code is commented to show each of its portions (reading in data, elbow plot creation-- which can be commented out if needed, running the k-means clustering algorithm and printing output)
Output is printed to console but can be piped into a file with the following syntax: ```python3 clustering.py [tsv file to import data from] [number of clusters (k)] [elbow plot figurename] > output_filename```

The data is outputted using the pandas print functionality in the following format:
row_number | id | cluster
