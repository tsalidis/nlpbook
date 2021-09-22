import locale

locale.setlocale(locale.LC_ALL, "en_UN")
print(locale.format_string("%f", 123456.789,grouping=True, monetary=False))
print(locale.format_string("%d", 123456789,grouping=True, monetary=False))

locale.setlocale(locale.LC_ALL, "el_GR")
print(locale.format_string("%f", 123456.789,grouping=True, monetary=False))
print(locale.format_string("%d", 123456789,grouping=True, monetary=False))
