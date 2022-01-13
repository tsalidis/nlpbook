package chapter_4;

import java.util.Scanner;

public class JavaTokenizer 
{
  static void PrintTokens(String input, String regexp, Object[] tokens)
  {
    int      ctoks  = 0;
    
    System.out.print("\""+input+"\" --> "+String.format("%-26s",regexp)+" --> [");
    for (Object tok : tokens)
    {
      if (ctoks > 0)
        System.out.print(" ");    
      System.out.print(tok);
      ctoks++;
    }
    System.out.println("] "+ctoks+" tokens");
  }
  
  public static void main(String[] args)
  {
    final String  TEXT_1  = "Ένα, δύο, τρία, τέσσερα, πέντε, έξι.";
    Scanner scanner = new Scanner(TEXT_1);
    int     ctoks   = 0;

    System.out.print("\""+TEXT_1+"\" --> {");
    while (scanner.hasNext())
    {
      if (ctoks > 0)
        System.out.print(" ");
      System.out.print("["+scanner.next()+"]");
      ctoks++;
    }
    System.out.println("} "+ctoks+" tokens.");

    scanner.close();
    
    final String  TEXT_2  = "Ένα, δύο! τρία-τέσσερα πέντε/έξι.";
    
    scanner = new Scanner(TEXT_2).useDelimiter("[-,/!. ]");
    ctoks = 0;
    
    System.out.print("\""+TEXT_2+"\"    --> {");
    while (scanner.hasNext())
    {
      if (ctoks > 0)
        System.out.print(" ");
      System.out.print("["+scanner.next()+"]");
      ctoks++;
    }
    System.out.println("} "+ctoks+" tokens.");
    
    scanner.close();
    
    scanner = new Scanner(TEXT_2).useDelimiter(String.format("((?<=%1$s)|(?=%1$s))", "[-,/!. ]"));
    ctoks = 0;
    
    System.out.print("\""+TEXT_2+"\"    --> {");
    while (scanner.hasNext())
    {
      if (ctoks > 0)
        System.out.print(" ");
      String token = scanner.next();

      if (token.trim().isEmpty())
        continue;
      
      System.out.print("["+token+"]");
      ctoks++;
    }
    System.out.println("} "+ctoks+" tokens.");
    
    scanner.close();
  }
}
