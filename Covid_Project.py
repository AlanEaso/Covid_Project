import pandas as pd
#import numpy as np
import  matplotlib.pyplot as plt
from collections import Counter

from sklearn.cluster import KMeans

d= pd.read_csv('datset.csv' , engine='python')

x= d.iloc[:,[2,3,4]].values

kmean = KMeans(n_clusters=20)

y = kmean.fit_predict(x)
test=[[9.301426019,76.55348505,689624]]

h = kmean.predict(test)
print(y)
print(h)
print(kmean.labels_)

print(kmean.cluster_centers_)
print(Counter(kmean.labels_))

plt.scatter(x[:,0],x[:,1],c=y,cmap='rainbow')
plt.scatter(kmean.cluster_centers_[:,0],kmean.cluster_centers_[:,1], color="black")
plt.show()