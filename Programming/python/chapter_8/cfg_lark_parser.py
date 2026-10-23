from lark import Lark, Transformer

grammar = r"""
?start: s

s: np vp
np: DET N
vp: V np

DET: "ο" | "η" | "το"
N: "άνθρωπος" | "γυναίκα" | "βιβλίο"
V: "διαβάζει" | "βλέπει"

%import common.WS
%ignore WS
"""

# Explicitly say Earley + dynamic lexer (good with literal tokens / Unicode)
parser = Lark(grammar, start="s", parser="earley", lexer="dynamic")


class ToAST(Transformer):
    def np(self, items):
        det, noun = items
        return str(noun)
    def vp(self, items):
        verb, obj = items
        return str(verb), obj
    def s(self, items):
        subject, vp = items
        verb, obj = vp
        return ("SVO",
                ("subject", subject),
                ("verb", verb),
                ("object", obj))


text = "ο άνθρωπος διαβάζει το βιβλίο"
tree = parser.parse(text)
ast  = ToAST().transform(tree)

print(tree.pretty())  # Parse Tree
print(ast)            # AST as tuples
