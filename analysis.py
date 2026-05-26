# Perform Clustering Analysis using K-Means

from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt

# Sample data
X = np.array([
    [1, 2],
    [1.5, 1.8],
    [5, 8],
    [8, 8],
    [1, 0.6],
    [9, 11]
])

# Create K-Means model
kmeans = KMeans(n_clusters=2, random_state=0)

# Train the model
kmeans.fit(X)

# Get cluster labels
labels = kmeans.labels_

# Get cluster centers
centers = kmeans.cluster_centers_

# Print results
print("Cluster Labels:")
print(labels)

print("\nCluster Centers:")
print(centers)

# Plot clusters
plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='rainbow')
plt.scatter(centers[:, 0], centers[:, 1], color='black', marker='x', s=200)

plt.title("K-Means Clustering")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()