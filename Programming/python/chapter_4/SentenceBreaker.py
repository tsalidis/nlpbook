
import nltk

## NLTK
#nltk.download('punkt')
fname = "../../data/lountemis.txt"
file = open(fname, "r", encoding="utf-8")

text = file.read();

#tokenizer = nltk.data.load("tokenizers/punkt/english.pickle")
tokenizer = nltk.data.load("tokenizers/punkt/greek.pickle")

sentences = tokenizer.tokenize(text)

print("###NLTK")
for sentence in sentences:
  print(f'[{sentence}]')
  
  
## SPACY
##python -m spacy download en_core_web_sm   

import spacy

#python -m spacy download el_core_news_sm
#model = spacy.load("en_core_web_sm")
model = spacy.load("el_core_news_sm")

doc = model(text)

sentences = [sen.text for sen in doc.sents]

print("\n###SpaCy")
for sentence in sentences:
  print(f'[{sentence}]')
