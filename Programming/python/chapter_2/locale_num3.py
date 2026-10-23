import locale


def set_first_available_locale(candidates: list[str]) -> str:
    """Ενεργοποιεί το πρώτο διαθέσιμο locale από τη λίστα."""
    for candidate in candidates:
        try:
            locale.setlocale(locale.LC_ALL, candidate)
            return candidate
        except locale.Error:
            continue

    raise locale.Error(
        "Δεν βρέθηκε κανένα από τα ζητούμενα locales: "
        + ", ".join(candidates)
    )


number_with_decimals = 123456.789
integer_number = 123456789

locale_cases = [
    (
        "Αμερικανικό αγγλικό locale",
        ["en_US.UTF-8", "en_US.utf8", "en_US", "English_United States.1252"],
    ),
    (
        "Ελληνικό locale",
        ["el_GR.UTF-8", "el_GR.utf8", "el_GR", "Greek_Greece.1253"],
    ),
]

for label, candidates in locale_cases:
    try:
        selected_locale = set_first_available_locale(candidates)

        print(f"\n{label}: {selected_locale}")
        print(
            locale.format_string(
                "%.3f",
                number_with_decimals,
                grouping=True,
                monetary=False,
            )
        )
        print(
            locale.format_string(
                "%d",
                integer_number,
                grouping=True,
                monetary=False,
            )
        )

    except locale.Error as error:
        print(f"\n{label}: {error}")
