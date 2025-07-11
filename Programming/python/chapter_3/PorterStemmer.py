from nltk.stem import PorterStemmer

stemmer = PorterStemmer()

words = ["connection", "connected", "connecting", "connectivity", "reconnection"]

for word in words:
    stem = stemmer.stem(word)
    print(f"{word} → {stem}")
