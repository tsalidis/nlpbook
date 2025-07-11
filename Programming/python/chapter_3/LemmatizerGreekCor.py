import stanza

stanza.download("el")
nlp = stanza.Pipeline("el")  # Φόρτωση μοντέλου ελληνικών

sentence = "Οι καθηγητές έγραψαν τις απαντήσεις τους στους πίνακες."

doc = nlp(sentence)

lemma_corrections = {
    "γράπτω": "γράφω",
    "πίνακη": "πίνακας",
    "μου": "αυτός",
    "σ": "σε"
}

for sent in doc.sentences:
    for word in sent.words:
        lemma = lemma_corrections.get(word.lemma, word.lemma)
        print(f"{word.text} → {lemma}")
