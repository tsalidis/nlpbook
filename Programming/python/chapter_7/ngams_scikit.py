# ngram_sklearn.py
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
import re

def basic_greek_tokenizer(s: str):
    # Απλός tokenizer για ελληνικά/λατινικά (μικρογράμματα)
    toks = re.findall(r"\w+", s.lower(), flags=re.UNICODE)
    return toks

def add_boundaries(text: str, n: int):
    # Προσθήκη boundary tokens για να "πιάνονται" n-grams αρχής/τέλους πρότασης
    toks = basic_greek_tokenizer(text)
    pad = ["<s>"]*(n-1)
    toks = pad + toks + ["</s>"]
    return " ".join(toks)

if __name__ == "__main__":
    corpus = [
        "Η Ευρώπη έχει πολλές χώρες και μεγάλες πόλεις.",
        "Οι πόλεις της Ευρώπης έχουν ιστορία και πολιτισμό.",
        "Η ιστορία της πόλης φαίνεται στα μνημεία.",
        "Ο πολιτισμός αναπτύσσεται στις μεγάλες πόλεις."
    ]

    # Προεπεξεργασία με boundary tokens για n=3 (θα καλύψει και 1..3)
    corpus_bounded = [add_boundaries(doc, 3) for doc in corpus]

    # Count n-grams 1..3
    vect = CountVectorizer(ngram_range=(3,3), analyzer="word", tokenizer=str.split, lowercase=False)
    X = vect.fit_transform(corpus_bounded)  # σparse πίνακας εγγράφου×χαρακτηριστικών
    vocab = vect.get_feature_names_out()
    counts = np.asarray(X.sum(axis=0)).ravel()  # συνολικές μετρήσεις στο corpus

    # Τα top 20 n-grams (1..3)
    top_idx = counts.argsort()[::-1][:20]
    print("Top n-grams (n=3):")
    for i in top_idx:
        print(f"{vocab[i]:<30} → {counts[i]}")

    # Παράδειγμα: όλα τα trigrams που ξεκινούν από "<s> η ευρώπη"
    target_prefix = "<s> η ευρώπη"
    mask = np.array([v.startswith(target_prefix) and len(v.split())==3 for v in vocab])
    idxs = np.where(mask)[0]
    print(f"\nTrigrams με prefix '{target_prefix}':")
    for i in idxs:
        print(f"{vocab[i]:<30} → {counts[i]}")
