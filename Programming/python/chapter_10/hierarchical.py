import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import linkage, dendrogram, fcluster

class HierarchicalClustering:
    def __init__(self, n_clusters=3, linkage_method='single'):
        self.n_clusters = n_clusters
        self.linkage_method = linkage_method
        self.linkage_matrix = None
        self.labels_ = None

    def fit(self, X):
        # Υπολογισμός του πίνακα συνδέσεων
        # self.linkage_matrix = linkage(X, method=self.linkage_method)
        self.linkage_matrix = linkage(X, method=self.linkage_method, metric='cosine')

        # Ανάθεση τελικών ετικετών cluster
        self.labels_ = fcluster(
            self.linkage_matrix,
            t=self.n_clusters,
            criterion='maxclust'
        ) - 1  # για αρίθμηση από το 0

    def predict(self, X=None):
        return self.labels_

    def plot_dendrogram(self, figsize=(10, 5)):
        if self.linkage_matrix is None:
            raise ValueError("Το μοντέλο δεν έχει εκπαιδευτεί ακόμα.")
        plt.figure(figsize=figsize)
        dendrogram(self.linkage_matrix)
        plt.title("Δενδρόγραμμα Ιεραρχικής Ομαδοποίησης")
        plt.xlabel("Δείγματα")
        plt.ylabel("Απόσταση")
        plt.show()