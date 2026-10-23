# tbx_read_demo.py
from lxml import etree

# Παράδειγμα TBX (συνήθως βρίσκεται σε .tbx αρχείο)
tbx_xml = """
<tbx xmlns:xcs="urn:iso:std:iso:30042:ed-2" xmlns="urn:iso:std:iso:30042:ed-2" type="TBX-Basic">
  <tbxHeader>
    <fileDesc><titleStmt><title>Mini Taxonomy</title></titleStmt></fileDesc>
  </tbxHeader>
  <text>
    <body>
      <conceptEntry id="c1">
        <langSet xml:lang="en">
          <tig><term>Literature</term></tig>
        </langSet>
        <langSet xml:lang="el">
          <tig><term>Λογοτεχνία</term></tig>
        </langSet>
      </conceptEntry>
      <conceptEntry id="c2">
        <langSet xml:lang="en">
          <tig><term>Novel</term></tig>
        </langSet>
        <langSet xml:lang="el">
          <tig><term>Μυθιστόρημα</term></tig>
        </langSet>
        <!-- ιεραρχική σχέση (προαιρετικά μέσω admin/termNote ανά schema) -->
        <descrip type="broaderConcept">c1</descrip>
      </conceptEntry>
    </body>
  </text>
</tbx>
"""

NS = {"tbx": "urn:iso:std:iso:30042:ed-2"}
root = etree.fromstring(tbx_xml.encode("utf-8"))

# 1) Λίστα εννοιών (conceptEntry) και όροι ανά γλώσσα
for ce in root.xpath(".//tbx:conceptEntry", namespaces=NS):
    cid = ce.get("id")
    labels = {}
    for ls in ce.xpath("./tbx:langSet", namespaces=NS):
        lang = ls.get("{http://www.w3.org/XML/1998/namespace}lang")
        term = ls.xpath(".//tbx:term/text()", namespaces=NS)
        labels[lang] = term[0] if term else ""
    broader = ce.xpath("./tbx:descrip[@type='broaderConcept']/text()", namespaces=NS)
    print(f"Concept {cid}: labels={labels} broader={broader[0] if broader else None}")
