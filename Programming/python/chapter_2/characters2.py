import unicodedata

BASIC_LATIN_START = 0x0000
BASIC_LATIN_END = 0x007F

GREEK_AND_COPTIC_START = 0x0370
GREEK_AND_COPTIC_END = 0x03FF

GREEK_EXTENDED_START = 0x1F00
GREEK_EXTENDED_END = 0x1FFF


def print_unicode_block(
    block_name: str,
    start: int,
    end: int,
) -> None:
    """Εμφανίζει βασικές ιδιότητες των κωδικών σημείων ενός μπλοκ."""

    print(f"\nUnicode Block: {block_name}")

    # Το end + 1 απαιτείται, επειδή το άνω όριο της range δεν περιλαμβάνεται.
    for code_point in range(start, end + 1):
        character = chr(code_point)
        category = unicodedata.category(character)
        name = unicodedata.name(character, "UNASSIGNED")

        if category == "Cn":
            display_character = "<μη εκχωρημένο>"
        elif character.isprintable():
            display_character = character
        else:
            display_character = "<μη εκτυπώσιμο>"

        print(
            f"Code Point: U+{code_point:04X}, "
            f"Character: {display_character}, "
            f"Name: {name}, "
            f"Category: {category}"
        )


print_unicode_block(
    "BASIC LATIN",
    BASIC_LATIN_START,
    BASIC_LATIN_END,
)

print_unicode_block(
    "GREEK AND COPTIC",
    GREEK_AND_COPTIC_START,
    GREEK_AND_COPTIC_END,
)

print_unicode_block(
    "GREEK EXTENDED",
    GREEK_EXTENDED_START,
    GREEK_EXTENDED_END,
)
