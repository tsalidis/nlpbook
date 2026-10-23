from dataclasses import dataclass
from typing import List, Optional

# --- Δομές Δέντρων ------------------------------------------------------------
@dataclass
class PTNode:  # Parse Tree node
    label: str
    children: List["PTNode"] = None
    token: Optional[str] = None  # για φύλλα με λέξη

    def __post_init__(self):
        if self.children is None:
            self.children = []

def pt_pretty(node: PTNode, indent: str = "", is_last: bool = True) -> str:
    branch = "└── " if is_last else "├── "
    s = indent + branch + (f'{node.label} → "{node.token}"' if node.token else node.label) + "\n"
    if node.children:
        for i, ch in enumerate(node.children):
            s += pt_pretty(ch, indent + ("    " if is_last else "│   "), i == len(node.children) - 1)
    return s

@dataclass
class ASTSentence:  # Abstract Syntax Tree
    subject: str
    verb: str
    obj: str

def ast_pretty(ast: ASTSentence) -> str:
    return (
        "Sentence\n"
        f"├── Subject: {ast.subject}\n"
        f"├── Verb:    {ast.verb}\n"
        f"└── Object:  {ast.obj}\n"
    )

# --- Λεξικό & Tokenizer -------------------------------------------------------
LEXICON = {
    "det": {"ο", "η", "το"},
    "n": {"άνθρωπος", "γυναίκα", "βιβλίο"},
    "v": {"διαβάζει", "βλέπει"},
}

def tokenize(text: str) -> List[str]:
    # απλή διάσπαση σε tokens: αφαίρεση απλής στίξης
    t = text.lower().replace("«", "").replace("»", "")
    for p in [".", ",", "!", "?", "·", ";", ":", "’", "'"]:
        t = t.replace(p, "")
    return t.split()

# --- Ο Parser (Recursive Descent) ---------------------------------------------
class Parser:
    def __init__(self, tokens: List[str]):
        self.tokens = tokens
        self.i = 0

    # βοηθητικά
    def la(self) -> Optional[str]:
        return self.tokens[self.i] if self.i < len(self.tokens) else None

    def match_word(self, expected_set: set, label: str) -> PTNode:
        w = self.la()
        if w is None or w not in expected_set:
            exp = "/".join(sorted(expected_set))
            got = "EOF" if w is None else w
            raise SyntaxError(f"Expected {label} ∈ {{{exp}}}, got '{got}' at position {self.i}")
        self.i += 1
        return PTNode(label, token=w)

    # Κανόνες γραμματικής:
    # S → NP VP
    def parse_S(self) -> PTNode:
        np_node = self.parse_NP()
        vp_node = self.parse_VP()
        return PTNode("S", [np_node, vp_node])

    # NP → DET N
    def parse_NP(self) -> PTNode:
        det = self.match_word(LEXICON["det"], "Det")
        noun = self.match_word(LEXICON["n"], "N")
        return PTNode("NP", [PTNode("Det", token=det.token), PTNode("N", token=noun.token)])

    # VP → V NP
    def parse_VP(self) -> PTNode:
        v = self.match_word(LEXICON["v"], "V")
        np2 = self.parse_NP()
        return PTNode("VP", [PTNode("V", token=v.token), np2])

    # Εκτέλεση πλήρους ανάλυσης
    def parse(self) -> PTNode:
        tree = self.parse_S()
        if self.la() is not None:
            raise SyntaxError(f"Extra tokens after parsing: '{self.la()}' at position {self.i}")
        return tree

# --- Από Parse Tree σε AST ----------------------------------------------------
def pt_to_ast_SVO(pt: PTNode) -> ASTSentence:
    """
    Περιμένουμε δομή:
      S
        NP(Det, N)
        VP(V, NP(Det, N))
    Εξάγουμε Subject=N, Verb=V, Object=N
    """
    assert pt.label == "S" and len(pt.children) == 2
    np, vp = pt.children
    # Subject
    subj_n = next(ch for ch in np.children if ch.label == "N").token
    # Verb
    v = next(ch for ch in vp.children if ch.label == "V").token
    # Object
    np2 = next(ch for ch in vp.children if ch.label == "NP")
    obj_n = next(ch for ch in np2.children if ch.label == "N").token
    return ASTSentence(subject=subj_n, verb=v, obj=obj_n)

# --- Demo ---------------------------------------------------------------------

if __name__ == "__main__":
    text = "Ο άνθρωπος διαβάζει το βιβλίο"
    tokens = tokenize(text)
    parser = Parser(tokens)
    parse_tree = parser.parse()
    print("PARSE TREE")
    print(pt_pretty(parse_tree))

    ast = pt_to_ast_SVO(parse_tree)
    print("AST")
    print(ast_pretty(ast))
