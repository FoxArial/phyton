import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.cluster import MeanShift
data = pd.read_csv('lab8\Lab_08_Var_02 - Lab_08_Var_02.csv')
x = np.array(data['x'])
y = np.array(data['y'])

X_train_test = np.array(data)
mean_shift_cluster = MeanShift(bandwidth=8)
mean_shift_cluster.fit(X_train_test)

colors = mean_shift_cluster.labels_
data['Cluster'] = colors
for cluster_name in np.unique(colors):
    cluster_data = data[data['Cluster'] == cluster_name]
    plt.scatter(cluster_data['x'], cluster_data['y'], label = cluster_name)
plt.legend(loc='best')
plt.show()

