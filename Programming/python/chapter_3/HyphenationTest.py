
from GreekHyphenator import GreekHyphenator

testWords = [ 
  "γάιδαρος", "αριθμητήριο", "τρυπιοχέρης", "τρόικα", "κορόιδο", "σόι", "νεράιδα",
    "πιάσιμο", "αηδόνι", "βόιδι", "μαϊμού", "έννοια", "παιδιά", "άδειος", "άδεια", "άδεια",
    "χάιδεψε", "κορόιδο", "ζεϊμπέκικο", "πλάι"
    ]

testWords2 = [ "διαβατήριο", "βιασμός",
        "καλά", "έχω", "αηδόνι", "ουρανός", "ναύτης", "ατμός", "έρχομαι", "αστράφτω", "σφυρίχτρα", "άνθρωπος", "φεγγάρι", "σύννεφο",
        "δουλειά", "άδειες", "άδειος", "αργαλειού", "άδειων", "λειώνω", "ίδιες", "ίδιος", "καινούργιου", "παιδιού", "ματιών", "κάποια", "οποιεσδήποτε",
        "ποιος", "τέτοιους", "μυαλό", "δυο", "σταχυού", "Καρυωτάκης", "σταχυών", "εχθρός", "αργαλειού", "σπρωγμένος", "οσφυοκάμπτης", "γκραβούρα", "άστρο",
        "έξαψη", "ταψιού", "απέκκριση", "κορόιδο", "βόηθα", "παιδιού", "διαβατήριο", "βιασμός", "αλλοιώνω"  
    ]

hyphenator = GreekHyphenator()

for word in testWords:
  hyphWord = hyphenator.hyphenate(word)
  print(f"Word: {word}, Hyphenated Word: {hyphWord}")
  
for word in testWords2:
  hyphWord = hyphenator.hyphenate(word)
  print(f"Word: {word}, Hyphenated Word: {hyphWord}")