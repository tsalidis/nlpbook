package chapter_3;

public class GreekHyphenator
{
  private static final char HYPHEN_CHAR    = '-';

  private static final char VOWEL_TYPE     = 'v';
  private static final char CONSONANT_TYPE = 'c';
  private static final char HYPHEN_TYPE    = HYPHEN_CHAR;

  private static boolean isVowel(char ch)
  {
    boolean isv = false;

    switch (ch)
    {
      case 'α': case 'ά':
      case 'ε': case 'έ':
      case 'η': case 'ή':
      case 'ι': case 'ί': case 'ϊ': case 'ΐ':  
      case 'ο': case 'ό':
      case 'υ': case 'ύ': case 'ϋ': case 'ΰ':  
      case 'ω': case 'ώ':  
        isv = true;
        break;
    }

    return isv;
  }

  @SuppressWarnings("unused")
  private boolean isConsonant(char ch)
  {
    return !isVowel(ch);
  }

  private static boolean isValidVowelSequence(char chVowel1, char chVowel2)
  {
    boolean  val = false;

    switch (chVowel1)
    {
      case 'α': 
        switch (chVowel2)
        {
          case 'η': 
          case 'ή': 
          case 'ι': 
          case 'ί': 
          case 'υ': 
          case 'ύ': 
            val = true;
            break;
        }
      case 'ε': 
        switch (chVowel2)
        {
          case 'υ': 
            val = true;
            break;
          case 'ι': 
            val = true;
            break;
        }
      case 'ο': 
        switch (chVowel2)
        {
          case 'ι': 
          case 'υ': 
            val = true;
            break;
        }
        break;
    }

    return val;
  }

  private static boolean isValidConsonantSequence(char chConsonant1, char chConsonant2)
  {
    boolean valid = true;

    if (chConsonant1 == chConsonant2)
      valid = false;

    
    switch (chConsonant1)
    {
      case 'β':
        switch (chConsonant2)
        {
          case 'γ':
          case 'δ':
          case 'λ':
          case 'ρ':
            valid = false;
        }

//β. βγ, βδ, βλ, βρ
//γ. γδ, γκ, γκλ, γκρ, γλ, γν, γρ
//δ. δρ
//θ. θλ, θν, θρ
//κ. κβ, κλ, κν, κρ, κτ
//μ. μν, μπ, μπλ, μπρ
//ν. ντ, ντρ
//π. πλ, πν, πρ, πτ
//σ. σβ, σγ, σθ, σκ, σκλ, σλ, σμ, σμπ, σν, σπ, σπλ, σπρ, στ, στρ, σφ, σφρ, σχ
//τ. τζ, τμ, τρ, τσ
//φ. φθ, φκ, φλ, φρ, φτ, φχ
//χ. χθ, χλ, χν, χρ, χτ 
break;
      case 'ρ':
        switch (chConsonant2)
        {
          case 'χ':
            valid = false;
            break;
        }
    }

    return valid;
  }

  /**
   * Hyphenate a word.
   * @param word
   * @return the hyphenated word  
   */
  public static String hyphenate(String word)
  {
    String  hyphWord  = "";
    char    prevChar  = HYPHEN_CHAR, prevType = HYPHEN_TYPE;
    char    curChar   = HYPHEN_CHAR, curType  = HYPHEN_TYPE;
    int     prevHyphDistance = 0;

    for (int i=0; i < word.length(); i++)
    {
      curChar = word.charAt(i);
      curType = isVowel(curChar) ? VOWEL_TYPE : CONSONANT_TYPE;

      if (curType == VOWEL_TYPE)
      {
        if ( (prevType == HYPHEN_TYPE) || (prevType == CONSONANT_TYPE) )
        {
          hyphWord += curChar;

          prevHyphDistance++;
          prevChar = curChar;
          prevType = curType;
        }
        else // prevType == VOWEL_TYPE
        {
          if (!isValidVowelSequence(prevChar,curChar))
          {
            hyphWord += HYPHEN_CHAR;
            prevHyphDistance = 0;
          }

          hyphWord += curChar;

          prevHyphDistance++;
          prevChar = curChar;
          prevType = curType;
        }
      }
      else // curType == CONSONANT_TYPE
      {
        if ( ( prevType == HYPHEN_TYPE ) || (prevType == CONSONANT_TYPE) )
        {
          hyphWord += curChar;

          prevHyphDistance++;
          prevChar = curChar;
          prevType = curType;
        }
        else // prevType == VOWEL_TYPE
        {
          if (i+1 == word.length())
          {
            hyphWord += curChar;

            prevHyphDistance++;
            prevChar = curChar;
            prevType = curType;
          }
          else
          {
            char nextChar = word.charAt(i+1), nextType = isVowel(nextChar) ? VOWEL_TYPE : CONSONANT_TYPE;

            if ( (nextType == VOWEL_TYPE) || isValidConsonantSequence(curChar,nextChar) )
            {
              hyphWord += HYPHEN_CHAR;
              prevHyphDistance = 0;							

              hyphWord += curChar;
              prevType = curType;
            }
            else
            {
              hyphWord += curChar;

              if (nextType == CONSONANT_TYPE)
              {
                hyphWord += HYPHEN_CHAR;
                prevHyphDistance = 0;
                prevType = HYPHEN_TYPE;
              }
            }
          }
        }
      }
    }

    return hyphWord;
  }

  public static void main(String[] args)
  {
    String[] testWords = {"καλά", "έχω", "αηδόνι", "ουρανός", "ναύτης", "ατμός", "έρχομαι", "αστράφτω", "σφυρίχτρα", "άνθρωπος", "φεγγάρι", "σύννεφο",
        "δουλειά", "άδειες", "άδειος", "αργαλειού", "άδειων", "λειώνω", "ίδιες", "ίδιος", "καινούργιου", "παιδιού", "ματιών", "κάποια", "οποιεσδήποτε",
        "ποιος", "τέτοιους", "μυαλό", "δυο", "σταχυού", "Καρυωτάκης", "σταχυών", "εχθρός", "αργαλειού", "σπρωγμένος", "οσφυοκάμπτης", "γκραβούρα", "άστρο",
        "έξαψη", "ταψιού", "απέκκριση"};

    for (String word : testWords)
    {
      String hyphWord = hyphenate(word);

      System.out.printf("Word: <%s>, Hyphenated Word: <%s>\n",word,hyphWord);
    }
  }
}
