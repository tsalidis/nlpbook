import spacy

nlp = spacy.load("el_core_news_sm")  # Μοντέλο για τα ελληνικά
doc = nlp("Η τεχνητή νοημοσύνη αλλάζει την επεξεργασία φυσικής γλώσσας.")
for token in doc:
    print(token.text, token.pos_)
