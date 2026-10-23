from property_lexer import lexer

with open("example.properties", encoding="utf-8") as f:
    data = f.read()

lexer.input(data)

for token in lexer:
    key, value = token.value
    print(f"KEY: '{key}' => VALUE: '{value}'")
