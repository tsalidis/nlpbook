import unicodedata

UNICODDE_GREEK_COPTIC_BLOCK_START = 0x0370
UNICODE_GREEK_COPTIC_BLOCK_END    = 0x03FF

UNICODDE_GREEK_EXTENDED_BLOCK_START = 0x1F00
UNICODE_GREEK_EXTENDED_BLOCK_END    = 0x1FFF

UNICODDE_ANSII_BLOCK_START = 0x0000
UNICODE_ANSII_BLOCK_END    = 0x007F

def print_unicode_block(block,beg,end):
  print(f"\nUnicode Block: {block}")
  for i in range(beg,end):
    ch = chr(i)
    cat = unicodedata.category(ch)
    nam = unicodedata.name(ch,'Unknown')
    print(f'Code Point: {hex(i)}, Character: {ch}, Name: {nam}, Category: {cat}')
    

print_unicode_block("ANSII", UNICODDE_ANSII_BLOCK_START, UNICODE_ANSII_BLOCK_END)
print_unicode_block("GREEK COPTIC", UNICODDE_GREEK_COPTIC_BLOCK_START, UNICODE_GREEK_COPTIC_BLOCK_END)
print_unicode_block("GREEK EXTENDED",UNICODDE_GREEK_EXTENDED_BLOCK_START, UNICODE_GREEK_EXTENDED_BLOCK_END)
