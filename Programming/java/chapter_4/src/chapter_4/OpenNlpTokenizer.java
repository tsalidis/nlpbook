package chapter_4;

import opennlp.tools.tokenize.SimpleTokenizer;

public class OpenNlpTokenizer 
{
  public static void main(String[] args) 
  {
    final String  TEXT_1  = "Ένα, δύο, τρία, τέσσερα, πέντε, έξι.";
  
    SimpleTokenizer simpleTokenizer = SimpleTokenizer.INSTANCE;
    String tokenList[] = simpleTokenizer.tokenize(TEXT_1);
    int    ctoks = 0;
    
    System.out.print("\""+TEXT_1+"\" --> {");
    for (String token : tokenList) 
    {
      if (ctoks > 0)
        System.out.print(" ");
      System.out.print("["+token+"]");
      ctoks++;
    }
    System.out.println("} "+ctoks+" tokens");

    final String  TEXT_2  = "Ένα, δύο! τρία-τέσσερα πέντε/έξι.";
    
    tokenList = simpleTokenizer.tokenize(TEXT_2);
    ctoks = 0;
    
    System.out.print("\""+TEXT_2+"\"    --> {");
    for (String token : tokenList) 
    {
      if (ctoks > 0)
        System.out.print(" ");
      System.out.print("["+token+"]");
      ctoks++;
    }
    System.out.println("} "+ctoks+" tokens");
  }
}
