import numpy as np

class KMeans:
    def __init__(self, k=3, max_iters=100):
        self.k = k
        self.max_iters = max_iters
        self.centroids = None

    def fit(self, X):
        # Τυχαία επιλογή αρχικών κεντροειδών
        random_indices = np.random.choice(len(X), self.k, replace=False)
        self.centroids = X[random_indices]

        for _ in range(self.max_iters):
            # Ανάθεση σημείων σε clusters
            clusters = self._assign_clusters(X)

            # Υπολογισμός νέων κεντροειδών
            new_centroids = np.array([
                X[clusters == i].mean(axis=0) if len(X[clusters == i]) > 0 else self.centroids[i]
                for i in range(self.k)
            ])

            # Έλεγχος σύγκλισης
            if np.allclose(self.centroids, new_centroids):
                break

            self.centroids = new_centroids

    def predict(self, X):
        return self._assign_clusters(X)

    def _assign_clusters(self, X):
        # Υπολογισμός αποστάσεων από κάθε κεντροειδές
        distances = np.linalg.norm(X[:, np.newaxis] - self.centroids, axis=2)
        # Επιλογή κοντινότερου κέντρου
        return np.argmin(distances, axis=1)