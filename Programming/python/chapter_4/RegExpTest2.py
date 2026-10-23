import re

# Δείγματα ελληνικών strings
κείμενα = [
    "Ο αριθμός είναι 12345",
    "Το όνομά μου είναι Νίκος.",
    "   Υπάρχουν κενά στην αρχή.",
    "Η διεύθυνση είναι οδός 28ης Οκτωβρίου 15.",
    "Αυτό_είναι_ένα_test123",
    "Δοκιμή χωρίς αριθμούς!",
    "Τηλ: 210-1234567",
]

print("== Μελέτη metacharacters ==")
# \d: οποιοδήποτε ψηφίο
for text in κείμενα:
    print("Ψηφία:", re.findall(r'\d+', text))

# \D: οποιοσδήποτε μη-ψηφιακός χαρακτήρας
for text in κείμενα:
    print("Μη-ψηφιακοί χαρακτήρες:", re.findall(r'\D+', text))

# \s: whitespace χαρακτήρες
for text in κείμενα:
    print("Κενά:", re.findall(r'\s+', text))

# \S: μη-whitespace χαρακτήρες
for text in κείμενα:
    print("Μη κενά:", re.findall(r'\S+', text))

# \w: alphanumeric χαρακτήρες και _
for text in κείμενα:
    print("Λέξεις με \w:", re.findall(r'\w+', text))

# \W: μη-alphanumeric χαρακτήρες
for text in κείμενα:
    print("Μη λέξεις με \W:", re.findall(r'\W+', text))

# \b: οριο λέξης
for text in κείμενα:
    print("Λέξεις με όριο:", re.findall(r'\b\w+\b', text))

print("\n== Μελέτη quantifiers ==")

quantifier_examples = [
    "ΑΑΑΑΑΑΑΑΑΑΑΑΑ",          # πολλά 'Α'
    "ΗΗΗΗΗΗΗΗΗΗΗΗ",          # πολλά 'Η'
    "Επαναλήψεις!!!",         # επαναλαμβανόμενα '!'
    "προϊόν",                # κανονική λέξη
    "σσσστ!",                # επανάληψη 'σ'
]

# * : 0 ή περισσότερες φορές
for text in quantifier_examples:
    print("Χαρακτήρες 'Α' * :", re.findall(r'Α*', text))

# + : 1 ή περισσότερες φορές
for text in quantifier_examples:
    print("Χαρακτήρες 'Η'+ :", re.findall(r'Η+', text))

# ? : 0 ή 1 φορά
for text in quantifier_examples:
    print("'σ'?:", re.findall(r'σ?', text))

# {n} : ακριβώς n φορές
for text in quantifier_examples:
    print("'Α' ακριβώς 3 φορές:", re.findall(r'Α{3}', text))

# {n,} : τουλάχιστον n φορές
for text in quantifier_examples:
    print("'Α' τουλάχιστον 5 φορές:", re.findall(r'Α{5,}', text))

# {n,m} : από n έως m φορές
for text in quantifier_examples:
    print("'σ' από 2 έως 4 φορές:", re.findall(r'σ{2,4}', text))
