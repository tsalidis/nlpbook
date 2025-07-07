import locale

print("locale: en_US")
locale.setlocale(locale.LC_ALL, "en_US")
print(locale.format_string("%f", 123456.789,grouping=True, monetary=False))
print(locale.format_string("%d", 123456789,grouping=True, monetary=False))

print("\nlocale: el_GR")
locale.setlocale(locale.LC_ALL, "el_GR")
print(locale.format_string("%f", 123456.789,grouping=True, monetary=False))
print(locale.format_string("%d", 123456789,grouping=True, monetary=False))
