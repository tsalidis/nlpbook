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

locale_cases = [
  (
    "Ελληνικό locale",
    ["el_GR.UTF-8", "el_GR.utf8", "el_GR", "Greek_Greece.1253"],
  ),
  (
    "Αμερικανικό αγγλικό locale",
    ["en_US.UTF-8", "en_US.utf8", "en_US", "English_United States.1252"],
  ),
]

for label, candidates in locale_cases:
  try:
    selected_locale = set_first_available_locale(candidates)

    print(f"\n{label}: {selected_locale}")
    for key, value in locale.localeconv().items():
      print(f"{key}: {value}")

  except locale.Error as error:
    print(f"\n{label}: {error}")
