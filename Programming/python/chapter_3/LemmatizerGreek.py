import stanza

stanza.download("el")
nlp = stanza.Pipeline("el")  # Φόρτωση μοντέλου ελληνικών

sentence = "Οι καθηγητές έγραψαν τις απαντήσεις τους στους πίνακες."

doc = nlp(sentence)

for sent in doc.sentences:
    for word in sent.words:
        print(f"{word.text} → {word.lemma}")
