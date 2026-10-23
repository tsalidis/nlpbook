from sklearn.cluster import KMeans

from gensim.downloader import load
model = load("glove-wiki-gigaword-50")

words = ["king", "queen", "man", "woman", "dog", "cat", "apple", "orange"]
X = [model[w] for w in words]

kmeans = KMeans(n_clusters=4, random_state=42)
labels = kmeans.fit_predict(X)

for word, label in zip(words, labels):
    print(word, "-> cluster", label)