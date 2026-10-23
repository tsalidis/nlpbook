from gensim.models import KeyedVectors

# Φόρτωση προεκπαιδευμένων embeddings (π.χ. Word2Vec)
# model = KeyedVectors.load_word2vec_format("model.bin", binary=True)

# Για απλότητα, χρησιμοποιούμε ένα μικρό ενσωματωμένο μοντέλο
from gensim.downloader import load
model = load("glove-wiki-gigaword-50")

# Υπολογισμός ομοιότητας
similarity = model.similarity("king", "queen")
print("Similarity (king, queen):", similarity)

# Εύρεση πιο παρόμοιων λέξεων
print(model.most_similar("king", topn=5))