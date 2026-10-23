import numpy as np

from gensim.downloader import load
model = load("glove-wiki-gigaword-50")

def sentence_embedding(sentence, model):
    words = sentence.split()
    vectors = [model[w] for w in words if w in model]
    return np.mean(vectors, axis=0)


s1 = "the cat sits on the mat"
s2 = "a dog lies on the rug"

v1 = sentence_embedding(s1, model)
v2 = sentence_embedding(s2, model)

# cosine similarity
similarity = np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))
print("Sentence similarity:", similarity)