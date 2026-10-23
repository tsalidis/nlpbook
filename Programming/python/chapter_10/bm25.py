import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from rank_bm25 import BM25Okapi

corpus = [
  "Today 29 May 2022 marks 100 years since the birth of Iannis Xenakis (1922-2001), architect mathematician & one of the 20th century’s most influential European composers especially known for his stochastic music",
  "Athens Ioannina Kalamata Kozani Thessaloniki & Trikala are the 6 cities chosen by the EU to participate in a project that will assist 100 cities to become climate neutral & smart by 203020 years earlier than the goal set by the EU",
  "2022 has been declared as Literary Year of Iakovos Kambanellis a writer and spiritual man with iconic literary works unsurpassed theatrical texts timeless screenplays and iconic songs with music by Mikis Theodorakis",
  "Ad astra Vangelis The film composer contributed scores to explorations by our Juno Mission to Jupiter Here ride along with the NASA Solar System spacecraft around Jupiter and moon Ganymede with sound up",
  "Speaker Pelosi May 18 Greece has been the wellspring of democratic principles for centuries They were a source of inspiration to the founding of America Now the United States and Greece work together as democratic nations"
]

query = "Ad astra"

# ----------------------
# TF-IDF
# ----------------------
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(corpus)

# Μετατροπή query σε vector
query_vec = vectorizer.transform([query])

# Υπολογισμός cosine similarity
tfidf_scores = (tfidf_matrix @ query_vec.T).toarray().flatten()

# ----------------------
# BM25
# ----------------------
# Tokenization
tokenized_corpus = [doc.split(" ") for doc in corpus]
tokenized_query = query.split(" ")

bm25 = BM25Okapi(tokenized_corpus)
bm25_scores = bm25.get_scores(tokenized_query)

print(f"Scores for query: {query}")

print("\nTF-IDF Scores:")
for i, score in enumerate(tfidf_scores):
    print(f"Doc {i}: {score:.4f} -> {corpus[i]}")

print("\nBM25 Scores:")
for i, score in enumerate(bm25_scores ):
  print(f"Doc {i}: {score:.4f} -> {corpus[i]}")

# ----------------------
# Ταξινόμηση αποτελεσμάτων
# ----------------------
print("\nTop document for (TF-IDF):")
print(corpus[np.argsort(-tfidf_scores)[0]])

print("\nTop document for (BM25):")
print(corpus[np.argsort(-bm25_scores)[0]])
