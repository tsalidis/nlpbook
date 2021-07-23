
import word

wrd1 = word.Word("παίζω","Verb")
wrd2 = word.Word("παιχνίδι")

wrd1.describe()
print(wrd1.capitalize())

wrd2.describe()
print(wrd2.capitalize())

from word import UnknownWord

wrd3 = UnknownWord("Άμαζον")
wrd3.describe()
