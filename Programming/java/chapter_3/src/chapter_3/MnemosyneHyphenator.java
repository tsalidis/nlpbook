package chapter_3;

import com.neurolingo.NLP.NLPTools.hyphenator.Hyphenator;

public class MnemosyneHyphenator
{
  public static void main(String[] args)
  {
    String hyphDict = "../../../mnemosyne/dicts/gr_hyph.lex";
    
    String[] testWords = { "διαβατήριο", "βιασμός",
        "καλά", "έχω", "αηδόνι", "ουρανός", "ναύτης", "ατμός", "έρχομαι", "αστράφτω", "σφυρίχτρα", "άνθρωπος", "φεγγάρι", "σύννεφο",
        "δουλειά", "άδειες", "άδειος", "αργαλειού", "άδειων", "λειώνω", "ίδιες", "ίδιος", "καινούργιου", "παιδιού", "ματιών", "κάποια", "οποιεσδήποτε",
        "ποιος", "τέτοιους", "μυαλό", "δυο", "σταχυού", "Καρυωτάκης", "σταχυών", "εχθρός", "αργαλειού", "σπρωγμένος", "οσφυοκάμπτης", "γκραβούρα", "άστρο",
        "έξαψη", "ταψιού", "απέκκριση", "κορόιδο", "βόηθα", "παιδιού", "διαβατήριο", "βιασμός", "αλλοιώνω"  
    };
        
    if (args.length == 1)
      hyphDict = args[0];
    
    try
    {
      Hyphenator hyphenator = new Hyphenator(hyphDict);
      
      for (String word : testWords)
      {
        String hyphWord = hyphenator.Hyphenate(word);

        System.out.printf("Word: <%s>, Hyphenated Word: <%s>\n",word,hyphWord);
      }
      
    }
    catch(Exception e)
    {
      e.printStackTrace();
    }
  }
}
