import unicodedata

text = "Το NLP αναλύει κείμενα, π.χ. «Καλημέρα!» 😊"

# Φιλτράρισμα: κρατάμε μόνο χαρακτήρες που η category αρχίζει με "L" (Letter)
letters_only = ''.join(
    c for c in text
    if unicodedata.category(c).startswith('L')
)

print("Αρχικό κείμενο:")
print(text)

print("\nΜόνο γράμματα:")
print(letters_only)
