import unicodedata


text = "Το NLP αναλύει κείμενα, π.χ. «Καλημέρα!» 😊"

# Κανονικοποίηση του κειμένου σε NFC
normalized_text = unicodedata.normalize("NFC", text)

# Διατηρούμε γράμματα, συνδυαστικά διακριτικά και διαστήματα.
filtered_text = "".join(
    character
    for character in normalized_text
    if unicodedata.category(character).startswith(("L", "M"))
    or character.isspace()
).strip()

print("Αρχικό κείμενο:")
print(text)

print("\nΚείμενο με γράμματα και διαστήματα:")
print(filtered_text)
