# owl_ontology_demo.py
from owlready2 import get_ontology, Thing, DatatypeProperty, ObjectProperty, default_world, \
                      FunctionalProperty, sync_reasoner  # sync_reasoner είναι προαιρετικό
from rdflib.namespace import RDF, RDFS, OWL, XSD

# 1) Δημιουργία οντολογίας
onto = get_ontology("http://nlpbook.org/library.owl#")

with onto:
    # Κλάσεις
    class Work(Thing): pass
    class Book(Work): pass
    class Person(Thing): pass
    class Author(Person): pass

    # Ιδιότητες
    class hasAuthor(ObjectProperty):
        domain = [Book]
        range  = [Author]

    class title(DatatypeProperty, FunctionalProperty):  # ένα title ανά έργο
        domain = [Work]
        range  = [str]

    class yearPublished(DatatypeProperty):
        domain = [Book]
        range  = [int]

# 2) Δημιουργία στιγμιοτύπων (individuals)
b1 = onto.Book("odyssey")
b1.title = "Οδύσσεια"
b1.yearPublished = [1997]  # π.χ. έκδοση
a1 = onto.Author("homer")
b1.hasAuthor = [a1]

b2 = onto.Book("algorithms")
b2.title = "Introduction to Algorithms"
b2.yearPublished = [2009]
a2 = onto.Author("cormen")
b2.hasAuthor = [a2]

# 3) (Προαιρετικό) Reasoning για παραγωγή συμπερασμάτων
# Απαιτεί Java reasoner (HermiT/Pellet) σε PATH. Αν δεν υπάρχει, σχολιάστε τις 2 γραμμές.
try:
    with onto:
        sync_reasoner()  # ελέγχει συνέπεια/δημιουργεί inferred τύπους
except Exception as e:
    print("Reasoner not available:", e)

# 4) Απλά «ερωτήματα» μέσω Python API
print("\nΌλα τα βιβλία:", list(onto.Book.instances()))
print("Συγγραφέας της Οδύσσειας:", b1.hasAuthor)
print("Τίτλοι έργων:", [w.title for w in onto.Work.instances() if w.title])

# 5) Αποθήκευση σε αρχείο OWL/RDF/XML ή TTL
onto.save(file="library.owl", format="rdfxml")
onto.save(file="library.ttl", format="ntriples")  # ή "turtle" αν υποστηρίζεται
print("\nSaved: library.owl, library.ttl")
