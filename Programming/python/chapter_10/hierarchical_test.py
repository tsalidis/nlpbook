import numpy as np
import matplotlib.pyplot as plt

from hierarchical import HierarchicalClustering

# Δημιουργία τεχνητών δεδομένων
np.random.seed(42)

cluster1 = np.random.randn(50, 2) + np.array([2, 2])
cluster2 = np.random.randn(50, 2) + np.array([-2, -2])
cluster3 = np.random.randn(50, 2) + np.array([2, -2])

X = np.vstack((cluster1, cluster2, cluster3))

# Εκπαίδευση του μοντέλου
hc = HierarchicalClustering(n_clusters=3, linkage_method='single')
hc.fit(X)

# Ετικέτες ομάδων
labels = hc.predict()

# Οπτικοποίηση των clusters
plt.figure(figsize=(8, 6))
plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis')
plt.title("Ιεραρχική Ομαδοποίηση")
plt.xlabel("x1")
plt.ylabel("x2")
plt.show()

# Οπτικοποίηση του δενδρογράμματος
hc.plot_dendrogram()
