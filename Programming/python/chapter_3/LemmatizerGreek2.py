import stanza

# 1. Download the Modern Greek language models (only needed once)
stanza.download("el")

# 2. Initialize the Greek neural pipeline
nlp = stanza.Pipeline("el")

# 3. Process your Greek text
text = "Οι καθηγητές έγραψαν τις απαντήσεις τους στους πίνακες."
doc = nlp(text)

# 4. Extract linguistic features (e.g., Lemmatization and Part-of-Speech tagging)
for sentence in doc.sentences:
    for word in sentence.words:
        print(f"Word: {word.text:<12} | Lemma: {word.lemma:<12} | POS: {word.upos}")
