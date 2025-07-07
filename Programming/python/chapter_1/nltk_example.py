import nltk

nltk.download('punkt')
#nltk.download('punkt_tab')
from nltk.tokenize import word_tokenize

sentence = "Η υπολογιστική γλωσσολογία είναι συναρπαστική."
tokens = word_tokenize(sentence, language='greek')
print(tokens)
