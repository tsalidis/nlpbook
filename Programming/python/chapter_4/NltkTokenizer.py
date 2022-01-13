
from nltk import word_tokenize

text1 = "ένα,δύο,τρία,τέσσερα,πέντε,έξι"

print(word_tokenize(text1))

text2 = "ένα,δύο-τρία/τέσσερα!πέντε.έξι"

print(word_tokenize(text2))

print(word_tokenize(text2,language="greek"))

from nltk import regexp_tokenize

print(regexp_tokenize(text2,'\w+|[-,/.!]'))
