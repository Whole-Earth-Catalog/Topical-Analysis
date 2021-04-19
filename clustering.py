import csv, matplotlib
import pandas as pd, time, sys
import matplotlib.pyplot as plt
import os
from sklearn.cluster import KMeans


def main():
  # reading in the data
  titles = []
  ids = []
  filename = sys.argv[1]
  with open(filename, newline='') as csvfile:
    tsvr = csv.reader(csvfile, delimiter='\t')
    for line in tsvr:
      try:
        title = line[1]
        titles.append(title)
        id = line[0]
        ids.append(id)
      except:
        pass

  #####################################################
  # making elbow plot to determine optimal k 
  # (can be commented out if not needed) 
  from sklearn.feature_extraction.text import TfidfVectorizer
  vectorizer = TfidfVectorizer(stop_words={'english'})
  X = vectorizer.fit_transform(titles)
  
  Sum_of_squared_distances = []
  K = range(2,10)

  for k in K:
    km = KMeans(n_clusters=k, max_iter=200, n_init=10)
    km = km.fit(X)
    Sum_of_squared_distances.append(km.inertia_)
  plt.plot(K, Sum_of_squared_distances, 'bx-')
  plt.xlabel('k')
  plt.ylabel('Sum_of_squared_distances')
  plt.title('Elbow Method For Optimal k')
  
  fig_name = sys.argv[3] + '.jpeg'
  plt.savefig(fig_name)
  plt.show()
  ######################################################
  # conducting the k means clustering
  true_k = int(sys.argv[2])
  model = KMeans(n_clusters=true_k, init='k-means++', max_iter=200, n_init=10)
  model.fit(X)
 
  labels=model.labels_
  title_cl=pd.DataFrame(list(zip(ids,labels)),columns=['title','cluster'])
  pd.set_option("display.max_rows", None, "display.max_columns", None)
  # output is printed! pipe out to a file if printing
  # to console is not necessary
  print(title_cl.sort_values(by=['cluster']))
  
# times the code if needed  
start_time = time.time()
main()
#print("--- %s seconds ---" % (time.time() - start_time))
