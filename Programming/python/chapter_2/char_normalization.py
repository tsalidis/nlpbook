import unicodedata

# Το γράμμα ά με δύο τρόπους
composed = 'ά'  # U+03AC (precomposed)
decomposed = '\u03B1\u0301'  # U+03B1 + U+0301 (α + τόνος)

print("Composed form:")
print([hex(ord(c)) for c in composed])

print("Decomposed form:")
print([hex(ord(c)) for c in decomposed])

# Κανονικοποίηση σε NFC (σύνθεση)
nfc = unicodedata.normalize('NFC', decomposed)
print("NFC normalized:")
print([hex(ord(c)) for c in nfc])

# Κανονικοποίηση σε NFD (διάσπαση)
nfd = unicodedata.normalize('NFD', composed)
print("NFD normalized:")
print([hex(ord(c)) for c in nfd])

# Έλεγχος ισότητας
print("Equal before normalization:", composed == decomposed)
print("Equal after NFC normalization:", nfc == composed)
print("Equal after NFD normalization:", nfd == decomposed)
