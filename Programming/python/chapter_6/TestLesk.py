from nltk.wsd import lesk
from nltk.wsd import 
from nltk import word_tokenize

sent = 'I went to the bank to deposit my money'

words = word_tokenize(sent)
syns = lesk(words, 'bank', 'n')

print(syns)
print(syns.definition())

syns = adapted_lesk(words, 'bank', 'n')