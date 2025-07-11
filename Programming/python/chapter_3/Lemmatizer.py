import spacy

nlp = spacy.load("en_core_web_sm")  # Μοντέλο αγγλικών
sentence = "The children are running faster than their parents."

doc = nlp(sentence)

for token in doc:
    print(f"{token.text} → {token.lemma_}")