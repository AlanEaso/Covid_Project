import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
import hdbscan
import seaborn as sns     #for styling

sns.set_context('poster')
sns.set_style('white')
sns.set_color_codes()
plot_kwds={'alpha':0.25, 's':60, 'linewidths':0}
palette = sns.color_palette('deep', 12)

d = pd.read_csv('data3.csv', engine='python')
Y = [[9.26614, 80.6297, 689508]]
x_axis = Y[0][0]
y_axis = Y[0][1]
df = d.apply(pd.to_numeric, errors='coerce')
df = d.dropna(axis=1)
clusterer = hdbscan.HDBSCAN(min_cluster_size=15, prediction_data=True).fit(df)
test_labels, strengths = hdbscan.approximate_predict(clusterer, Y)

print(test_labels)
print(len(Counter(clusterer.labels_)), len(Counter(clusterer.probabilities_)))

pal = sns.color_palette('deep', len(clusterer.labels_))
print(pal[9])
colors = [sns.desaturate(pal[col], sat) for sat, col in zip(clusterer.probabilities_, clusterer.labels_)]
#plt.scatter(d.iloc[:,0], d.iloc[:,1], c=colors, **plot_kwds)
#plt.scatter(x_axis, y_axis, c='black', s=50)
#plt.show()


