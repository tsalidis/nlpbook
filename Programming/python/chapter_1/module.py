
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


def get_morpho2(word, *attributes):
  """Returns a string that describes the word with its morphological attributes"""  
  morpho = f"word={word}"
  for attr in attributes:
    morpho += f", attribute={attr}"
  return morpho

def get_morpho3(word, **attributes):
  """Returns a string that describes the word with its morphological attributes"""
  attributes['word'] = word  
  morpho = f"word={word}"
  for k,v in attributes.items():
    morpho += f", {k}={v}"
  return morpho
