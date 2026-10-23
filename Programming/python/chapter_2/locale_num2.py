import locale

number_with_decimals = 123456.789
integer_number = 123456789

print("Locale: en_US.UTF-8")
locale.setlocale(locale.LC_ALL, "en_US.UTF-8")

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

print("\nLocale: el_GR.UTF-8")
locale.setlocale(locale.LC_ALL, "el_GR.UTF-8")

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
