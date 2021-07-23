
class Word:
  """Word type defined as class"""
  
  def __init__(self,word,pos='Noun'):
    """Initializes an instance with word string and pos"""
    self.word = word
    self.pos  = pos
  
  def describe(self):
    print(f"word: {self.word} pos: {self.pos}")


  def capitalize(self):
    return self.word.title()


class UnknownWord(Word):
  def __init__(self,word):
    super().__init__(word)
    
  def describe(self):
    print(f"unknown word: {self.word} pos: {self.pos}")
  