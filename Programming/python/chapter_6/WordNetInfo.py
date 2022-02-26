
from nltk.corpus import wordnet

synsets = wordnet.synsets("cat")

print('\n*** Synsets for word "cat"')
for syns in synsets:
  print(syns)

print('\n*** First Synset for word "cat"')
syns = wordnet.synsets('cat')[0]
print(syns)

print('\n*** Synset for word "cat.n.01"')
syns = wordnet.synset('cat.n.01')
print(syns)

print('\n*** Definition for word "cat.n.01"')
print(wordnet.synset('cat.n.01').definition())

print('\n*** Examples for word "cat"')
for syns in synsets:
  if syns.examples():
    print(f'\n****** Examples for synset {syns.name()}')
    for ex in syns.examples():
      if ex:
        print(ex)

print('\n*** Lemmas for word "cat.n.01"')
print(wordnet.synset('cat.n.01').lemmas())

print('\n*** Lemma names for word "cat.n.01"')
print(wordnet.synset('cat.n.01').lemma_names())


print('\n*** Lemmas in Greek language for word "cat.n.01"')
print(wordnet.synset('cat.n.01').lemmas('ell'))

print('\n*** Synonyms for word "cat"')
for syns in synsets:
  for lemma in syns.lemmas():
    print(lemma.name())

print('\n*** Synonyms for word "cat" in Greek')
for syns in synsets:
  for lemma in syns.lemmas('ell'):
    print(lemma.name())

print('\n*** Antonyms for word "cat"')
for syns in synsets:
  for lemma in syns.lemmas():
    if lemma.antonyms():
      print(lemma.antonyms()[0].name())
    
syns_1 = wordnet.synset('cat.n.01')
syns_2 = wordnet.synset('lion.n.01')

print('\n*** Similarity between "cat" and "lion"')
print(syns_1.wup_similarity(syns_2)*100)
    
synsets = wordnet.synsets("cat", pos=wordnet.VERB)
print('\n*** Synsets for word "cat" with PoS = VERB')
for syns in synsets:
  print(syns)


print('\n*** Hypernyms for word "cat.n.01"')
for syns in syns_1.hypernyms():
  for lemma in syns.lemmas():
    print(lemma.name())

print('\n*** Hyponyms for word "cat.n.01"')
for syns in syns_1.hyponyms():
  for lemma in syns.lemmas():
    print(lemma.name())
    

