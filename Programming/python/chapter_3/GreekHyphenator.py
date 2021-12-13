
class GreekHyphenator:

  def __init__(self):
    self.NUM_PHONEMES4SYL = 3
    self.NO_HYPH_POS      = -1
    self.HYPHEN_CHAR      = '-'
    
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

  def __getPhoneme (self, word, wpos, fVowel):
    phoneme = []
    while wpos < len(word):
      ch = word[wpos]
      if (fVowel and self.__isVowel(ch)) or (not fVowel and self.__isConsonant(ch)):
        phoneme.append(ch)
      else:
        break;
      wpos += 1
    return phoneme;
  
  def __appendPhoneme(self,hyphWord,phoneme,hpos):
    for idx in range(0,hpos):
      hyphWord += phoneme[idx]
    return hyphWord
  
  def __toString(self,phoneme):
    strPhoneme = ""
    for ch in phoneme:
      strPhoneme += ch
    return strPhoneme
  
  def __findHyphenInVowelsPhoneme(self,vowelPhoneme):
    hpos = self.NO_HYPH_POS
    
    strPhoneme = self.__toString(vowelPhoneme)
    lenPhoneme = len(strPhoneme)
    if lenPhoneme == 2:
      if not self.__isValidVowelBigram(strPhoneme):
        hpos = 1
    elif lenPhoneme == 3:
      if not self.__isValidVowelTrigram(strPhoneme):
        if not self.__isValidVowelBigram(strPhoneme[0:2]):
          hpos = 1;
        elif not self.__isAccentVowel(strPhoneme[2]):
          hpos = 2;
    elif lenPhoneme == 4:      
      if not self.__isValidVowelFourgram(strPhoneme):
        if not self.__isValidVowelTrigram(strPhoneme[0:3]):
          if not self.__isValidVowelBigram(strPhoneme[0:2]):
            hpos = 1;
          elif not self.__isAccentVowel(strPhoneme[2]):
            hpos = 2;
      else:
        hpos = 3
      
    return hpos

  def __findHyphenInConsonantsPhoneme(self,consonantPhoneme,fLastPhoneme):
    hpos = self.NO_HYPH_POS

    if not fLastPhoneme:
      if len(consonantPhoneme) >= 2:
        strPhoneme = self.__toString(consonantPhoneme)
        if not self.__isValidConsonantBigram(strPhoneme[0:2]):
          hpos = 1;
          
    return hpos
  
  def hyphenate(self,word):
    hyphWord  = ""
    
    WORD_LEN = len(word)
    hyph_pos = 0
    
    i = 0
    
    while i < WORD_LEN:
      """ Step 1. Read the phonemes of next syllable"""
      widx  = i
      onset = self.__getPhoneme(word, widx, False)
      widx += len(onset)
      nucleus = self.__getPhoneme(word, widx, True)
      widx += len(nucleus)
      coda = self.__getPhoneme(word, widx, False)
      
      """ Step 2. Append first phoneme with consonants"""
      hyphWord += self.__toString(onset)
      hyph_pos += len(onset)
      
      """Step 3 Find the hyphen in nucleus.""" 
      hpos = self.__findHyphenInVowelsPhoneme(nucleus);

      if hpos >= 0:
        """"append the first part of phoneme"""
        hyphWord = self.__appendPhoneme(hyphWord,nucleus,hpos);

        hyphWord += self.HYPHEN_CHAR;
        hyph_pos += hpos;
      else:  
        """vowels cannot be hyphenated"""
        hyphWord = self.__appendPhoneme(hyphWord,nucleus,len(nucleus));
        hyph_pos += len(nucleus)

        fLastPhoneme = hyph_pos+len(coda) == WORD_LEN;

        """Step 4. Check the existence of coda""" 
        hpos = self.__findHyphenInConsonantsPhoneme(coda,fLastPhoneme );

        if hpos >= 0:
          hyphWord = self.__appendPhoneme(hyphWord,coda,hpos);
          hyphWord += self.HYPHEN_CHAR;

          hyph_pos += hpos;
        elif not fLastPhoneme:
          hyphWord += self.HYPHEN_CHAR;
      i = hyph_pos       

    return hyphWord;
