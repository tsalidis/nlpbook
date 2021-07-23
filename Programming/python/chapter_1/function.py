
def print_default_pos():
  """Prints the default part of speech"""
  print("Noun")
  
def print_pos(pos):
  """Prints the pos"""
  print(f"pos={pos.title()}!")



print_default_pos()
print_pos("verb")


def print_morpho(word,pos,gender,case,number='singular'):
  """Prints the word with its morphological attributes"""
  print(f"word={word}, pos={pos}, gender={gender}, case={case}, number={number}")
  
print_morpho('παιχνιδιού','noun','neutral','genitive','singular')
print_morpho('παιχνιδιού',pos='noun',gender='neutral',case='genitive',number='singular')
print_morpho(pos='noun',gender='neutral',case='genitive',number='singular',word='παιχνιδιού')
print_morpho(pos='noun',gender='neutral',case='genitive',word='παιχνιδιού')



def get_morpho(word,pos,gender=None,case='',number=''):
  """Returns a string that describes the word with its morphological attributes"""
  if number:
    return f"word={word}, pos={pos}, gender={gender}, case={case}, number={number}"
  else:
    if case:
      return f"word={word}, pos={pos}, gender={gender}, case={case}"
    else:
      if gender:
        return f"word={word}, pos={pos}, gender={gender}"
      else:
        return f"word={word}, pos={pos}"


print(get_morpho('παιχνιδιού','noun','neutral','genitive','singular'))
print(get_morpho('και','conj'))


def get_morpho2(word, *attributes):
  """Returns a string that describes the word with its morphological attributes"""  
  morpho = f"word={word}"
  for attr in attributes:
    morpho += f", attribute={attr}"
  return morpho
print(get_morpho2('παιχνιδιού','noun','neutral','genitive','singular'))

def get_morpho3(word, **attributes):
  """Returns a string that describes the word with its morphological attributes"""
  attributes['word'] = word  
  morpho = f"word={word}"
  for k,v in attributes.items():
    morpho += f", {k}={v}"
  return morpho
print(get_morpho3('παιχνιδιού',pos='noun',gender='neutral',case='genitive',number='singular'))
