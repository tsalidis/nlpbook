import nltk
from nltk import CFG

grammar = CFG.fromstring("""
S -> NP VP
NP -> DET N
VP -> V NP
DET -> 'ο' | 'η' | 'το'
N -> 'άνθρωπος' | 'γυναίκα' | 'βιβλίο'
V -> 'διαβάζει' | 'βλέπει'
""")

parser = nltk.parse.EarleyChartParser(grammar)
sent = "ο άνθρωπος διαβάζει το βιβλίο".split()
for t in parser.parse(sent):
    print(t)          # Parse tree σε bracketed μορφή
    t.pretty_print()  # ASCII δέντρο
