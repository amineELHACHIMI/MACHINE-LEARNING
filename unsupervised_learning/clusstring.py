import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans

# 🔹 1. Real-like dataset (clusters hidden)
X, _ = make_blobs(
    n_samples=500,
    centers=4,
    cluster_std=1.2,
    random_state=42
)

# 🔹 2. KMeans model
kmeans = KMeans(n_clusters=4, random_state=42)
kmeans.fit(X)

# 🔹 3. results
labels = kmeans.labels_
centroids = kmeans.cluster_centers_

# 🔹 4. plotting clusters
colors = ['red', 'green', 'blue', 'purple']

for i in range(4):
    plt.scatter(
        X[labels == i][:, 0],
        X[labels == i][:, 1],
        color=colors[i]
    )

# 🔹 5. centroids
plt.scatter(
    centroids[:, 0],
    centroids[:, 1],
    color='black',
    marker='x',
    s=200
)

plt.title("Real Clustering (KMeans)")
plt.show()