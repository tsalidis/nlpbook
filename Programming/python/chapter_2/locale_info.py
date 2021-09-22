import locale

print("Hellenic Greece locale")
locale.setlocale(locale.LC_ALL, "el_GR")
for key, value in locale.localeconv().items():
    print("%s: %s" % (key, value))
    
    
print("\nEnglish USA locale")
locale.setlocale(locale.LC_ALL, "en_US")
for key, value in locale.localeconv().items():
    print("%s: %s" % (key, value))
