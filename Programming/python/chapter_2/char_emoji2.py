import emoji

text = "Καλημέρα! 😀 Πώς είσαι σήμερα; 🌞✨"

# Εντοπισμός των emoji στο κείμενο
emoji_matches = emoji.emoji_list(text)
emojis_in_text = [match["emoji"] for match in emoji_matches]

print("Emoji που βρέθηκαν στο κείμενο:")
print(emojis_in_text)

# Αφαίρεση των emoji
clean_text = emoji.replace_emoji(text, replace="")

print("\nΚείμενο χωρίς emoji:")
print(clean_text)
