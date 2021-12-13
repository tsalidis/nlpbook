
class GreekHyphenator:

  def __init__(self):
    self.NUM_PHONEMES4SYL = 3
    self.vowels = ('Α', 'Ά', 'α', 'ά', 
                   'Ε', 'Έ', 'ε', 'έ', 
                   'Η', 'Ή', 'η', 'ή',
                   'Ι', 'Ί', 'ι', 'ί', 'ϊ', 'ΐ', 
                   'Ο', 'Ό', 'ο', 'ό',
                   'Υ', 'Ύ', 'υ', 'ύ', 'ϋ', 'ΰ',
                   'Ω', 'Ώ', 'ω', 'ώ'
                  )
    self.accentVowels = ('Ά', 'ά', 
                         'Έ', 'έ', 
                         'Ή', 'ή',
                         'Ί', 'ί', 'ΐ', 
                         'Ό', 'ό',
                         'Ύ', 'ύ', 'ΰ',
                         'Ώ', 'ώ'
                        )
    self.bigramVowels = ( "αη", "αή", "αι", "αί", "αϊ", "αυ", "αύ",
                          "ει", "εί", "ευ", "εύ", 
                          "ια", "ιά", "ιε", "ιέ", "ιο", "ιό", "ιω", "ιώ",
                          "οι", "οί", "ου", "ού", "οη", "οή",
                          "υα", "υά", "υι", "υί", "υο", "υό", "υω", "υώ",
                        )
    self.trigramVowels = ( "εια", "ειε", "ειο", "ειω",
                           "οια", "οιε", "οιο"
                         )
    self.fourgramVowels = ( "ειου", "ειού",
                            "οιου", "οιού"
                          )
    self.bigramConsonants = ( "βγ", "βδ", "βλ", "βρ",
                              "γδ", "γκ", "γλ", "γν", "γρ",
                              "δρ",
                              "θλ", "θν", "θρ",
                              "κβ", "κλ", "κν", "κρ", "κτ",
                              "μν", "μπ",
                              "ντ",
                              "πλ", "πν", "πρ", "πτ",
                              "σβ", "σγ", "σθ", "σκ", "σλ", "σμ", "σν", "σπ", "στ", "σφ", "σχ",
                              "τζ", "τμ", "τρ", "τσ",
                              "φθ", "φκ", "φλ", "φρ", "φτ", "φχ",
                              "χθ", "χλ", "χν", "χρ", "χτ"
                            )
    
    print("")
    
    
  def __isVowel(self,ch):
    return ch in self.vowels
    
  def __isAccentVowel(self,ch):
    return ch in self.accentVowels

  def __isConsonant(self,ch):
    return ch not in self.vowels

  def __isValidVowelBigram(self,bigram):
    return bigram in self.bigramVowels
  
  def __isValidVowelTrigram(self,trigram):
    return trigram in self.trigramVowels
  
  def __isValidVowelFourgram(self,fourgram):
    return fourgram in self.fourgramVowels
  
  def __isValidConsonantBigram(self,bigram):
        return bigram in self.bigramConsonants

