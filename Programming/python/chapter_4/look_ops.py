import re

text = "Η τιμή του προϊόντος είναι 20€ και η έκπτωση είναι 5€. Η λέξη '20' εμφανίζεται επίσης μόνη της."

# 1. Positive Lookahead: Βρες αριθμούς πριν από €
pattern1 = r"\d+(?=€)"
matches1 = re.findall(pattern1, text)
print("Positive lookahead (πριν από '€'):", matches1)

# 2. Positive Lookbehind: Βρες λέξεις μετά τη λέξη 'του'
pattern2 = r"(?<=του )\w+"
matches2 = re.findall(pattern2, text)
print("Positive lookbehind (μετά από 'του'):", matches2)

# 3. Negative Lookahead: Βρες λέξεις που ΔΕΝ ακολουθούνται από €
pattern3 = r"\b\w+\b(?!€)"
matches3 = re.findall(pattern3, text)
print("Negative lookahead (λέξεις που δεν ακολουθούνται από  '€'):", matches3)

# 4. Negative Lookbehind: Βρες αριθμούς που ΔΕΝ προηγούνται από το €
pattern4 = r"(?<!€)\d+"
matches4 = re.findall(pattern4, text)
print("Negative lookbehind (ΔΕΝ προηγείται '€'):", matches4)
