# tbx_write_demo.py
from lxml.builder import ElementMaker
from lxml import etree

TBX_NS = "urn:iso:std:iso:30042:ed-2"
E = ElementMaker(namespace=TBX_NS, nsmap={None: TBX_NS, "xcs": "urn:iso:std:iso:30042:ed-2"})

# Παράδειγμα εσωτερικής δομής
taxonomy = [
    {"id": "c1", "labels": {"en": "Literature", "el": "Λογοτεχνία"}, "broader": None},
    {"id": "c2", "labels": {"en": "Novel", "el": "Μυθιστόρημα"}, "broader": "c1"},
]

# Κατασκευή TBX tree
concept_entries = []
for node in taxonomy:
    langsets = []
    for lang, label in node["labels"].items():
        langsets.append(
            E.langSet(E.tig(E.term(label)), **{"{http://www.w3.org/XML/1998/namespace}lang": lang})
        )
    children = langsets[:]
    if node["broader"]:
        children.append(E.descrip(node["broader"], type="broaderConcept"))
    concept_entries.append(E.conceptEntry(*children, id=node["id"]))

tbx = E.tbx(
    E.tbxHeader(E.fileDesc(E.titleStmt(E.title("Mini Taxonomy")))),
    E.text(E.body(*concept_entries)),
    type="TBX-Basic"
)

# Αποθήκευση σε αρχείο .tbx (XML)
xml_bytes = etree.tostring(tbx, pretty_print=True, xml_declaration=True, encoding="UTF-8")
with open("mini_taxonomy.tbx", "wb") as f:
    f.write(xml_bytes)

print("Saved: mini_taxonomy.tbx")
