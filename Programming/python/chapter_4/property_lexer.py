from typing import Any

import ply.lex as lex


tokens = (
    "KEYVALUE",
)

states = (
    ("continuation", "exclusive"),
)

# Χαρακτήρες που αγνοούνται στην αρχική κατάσταση.
t_ignore = " \t"
t_continuation_ignore = " \t"

current_key: str | None = None
current_value_lines: list[str] = []


def t_COMMENT(t: Any):
    r"\#[^\n]*"
    pass


def t_EMPTYLINE(t: Any):
    r"\n+"
    t.lexer.lineno += len(t.value)
    pass


def t_KEYVALUE(t: Any):
    r"[a-zA-Z_][a-zA-Z0-9_.-]*[ \t]*=[ \t]*[^\n#\\]*(?:\\)?"
    global current_key, current_value_lines

    key, value = t.value.split("=", 1)
    current_key = key.strip()
    current_value_lines = [value.rstrip("\\").strip()]

    if t.value.rstrip().endswith("\\"):
        t.lexer.begin("continuation")
        return None

    t.value = (current_key, current_value_lines[0])
    return t


def t_continuation_CONTLINE(t: Any):
    r"[^\n#\\]+(?:\\)?"
    global current_value_lines

    value_line = t.value.rstrip("\\").strip()
    current_value_lines.append(value_line)

    if not t.value.rstrip().endswith("\\"):
        t.lexer.begin("INITIAL")
        t.type = "KEYVALUE"
        t.value = (current_key, " ".join(current_value_lines))
        return t

    return None


def t_continuation_newline(t: Any):
    r"\n+"
    t.lexer.lineno += len(t.value)


def t_continuation_error(t: Any):
    print(f"Σφάλμα στη συνέχεια τιμής: {t.value[0]}")
    t.lexer.skip(1)


def t_error(t: Any):
    print(f"Άγνωστος χαρακτήρας: {t.value[0]}")
    t.lexer.skip(1)


lexer = lex.lex()