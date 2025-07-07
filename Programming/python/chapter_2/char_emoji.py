import emoji

text = "Καλημέρα! 😀 Πώς είσαι σήμερα; 🌞✨"

# Ανίχνευση emoji
emojis_in_text = [c for c in text if c in emoji.EMOJI_DATA]

print("Emoji που βρέθηκαν στο κείμενο:")
print(emojis_in_text)

# Αφαίρεση emoji με κανονική έκφραση
def remove_emoji(s):
    return emoji.replace_emoji(s, replace='')

clean_text = remove_emoji(text)

print("\nΚείμενο χωρίς emoji:")
print(clean_text)
