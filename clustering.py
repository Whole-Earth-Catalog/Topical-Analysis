import csv, matplotlib, pandas as pd
    
def clean(titles):
    cleaned = []
    ignoreList =[]
    punctList = [".", ",", "?", "!", ";", ":", "\"", "'", "…", "–", "--", "—", "[", "]", "{", "}"]
    importList("stopwords.txt", ignoreList)
    str = ""
    # a bit would be considered each paragraph/document, a token would be
    # considered a word in that paragraph
    for t in titles:
        str = ""
        t = t.lower()
        for token in t.split():
            for i in range(0, len(token)):
                # checks if any of the characters in the word are punctuation,
                # removes it if so 
                if(token[i] in punctList):
                    token = token.replace(token[i], ' ')
                if(token[i].isdigit()):
                    token = token.replace(token[i], ' ')      
            token = token.replace(" ", "")
            
            if "’" in token:
                if token.split("’")[0].lower() not in ignoreList:
                    str += token.split("’")[0] + " "
                if token.split("’")[1].lower() not in ignoreList:
                    str += token.split("’")[1] + " "
            elif token.lower() not in ignoreList:
                str += token + " "
        cleaned.append(str)
    return cleaned

# 'importList': creates a list of terms from a file
def importList(file, aList):
  with open(file) as f:
    for lines in f:
      aList.append(lines.strip("\n"))
    f.close()

titles = []
ids = []
with open('excerpt.tsv', newline='') as csvfile:
  tsvr = csv.reader(csvfile, delimiter='\t')
  for line in tsvr:
    try:
      title = line[1]
      titles.append(title)
      id = line[0]
      ids.append(id)
    except:
      pass

#cleaned = clean(titles)
from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer(stop_words={'english'})
X = vectorizer.fit_transform(titles)

import matplotlib.pyplot as plt
import os
from sklearn.cluster import KMeans
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
plt.show()
print("elbow plot made")

true_k = 5
model = KMeans(n_clusters=true_k, init='k-means++', max_iter=200, n_init=10)
model.fit(X)
print("model fit")
labels=model.labels_
title_cl=pd.DataFrame(list(zip(ids,labels)),columns=['title','cluster'])
pd.set_option("display.max_rows", None, "display.max_columns", None)
print(title_cl.sort_values(by=['cluster']))
