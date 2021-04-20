# SQL queries for clustering
Several different queries used for getting information about clusters.
# createClusterTable
Has the code for how the different clusters were made from the K means clustering output. There are a total of 8 different cluster tables that were made:
- TABLE english_clusters: a table of titles with an assigned cluster number for all english titles. There is a total of 4 clusters.
- TABLE english_clusters6: like english_clusters except there are 6 clusters.
- TABLE litform_clusters9: like english_clusters, but there are 9 clusters meant to reflect the different genre listings we have in tag008
- TABLE litform_clusters11: like litform_clusters9 except there are 11 clusters
- TABLE 1500s_cl: a table with titles assigned a cluster number for all english titles in the 1500s, there are 3 clusters
- TABLE 1600s_cl: a table with titles assigned a cluster number for all english titles in the 1600s, there are 4 clusters
- TABLE 1600s_3cl: a table with titles assigned a cluster number for all english titles in the 1600s, there are 3 clusters
- TABLE 1700s_cl: a table with titles assigned a cluster number for all english titles in the 1700s, there are 3 clusters

# queries
Has several different different queries that I used to understand the first table, english_clusters. I used these queries for the other tables aswell and just modified the 
table names in the query to match the table I was studying. The results and interpretations of these queries are in the shared google drive.

# subject_in_cluster
Has an example query that I used to get the data that can be found in graph_data. To get the data for different centuries and different cluster numbers I just change the
associated words and spots with what I was looking for.

