package chapter_4;

import java.util.List;
import java.util.regex.Pattern;
import java.util.stream.Collectors;

public class SplitTokenizer 
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
    String  text1 = "ένα,δύο,τρία,τέσσερα,πέντε,έξι";
    String  delim = ",";
    
    String[] tokens = text1.split(delim);
    
    PrintTokens(text1,delim,tokens);

    delim = "(?<=,)";
    tokens = text1.split(delim);
    PrintTokens(text1,delim,tokens);

    delim = "(?=,)";
    tokens = text1.split(delim);
    PrintTokens(text1,delim,tokens);
    
    delim = "((?<=,)|(?=,))";
    tokens = text1.split(delim);
    PrintTokens(text1,delim,tokens);

    String  text2 = "ένα,δύο-τρία/τέσσερα!πέντε.έξι";

    delim  = "[-,/!.]"; 
    tokens = text2.split(delim);
    PrintTokens(text2,delim,tokens);
    
    delim = String.format("((?<=%1$s)|(?=%1$s))", delim);
    tokens = text2.split(delim);
    PrintTokens(text2,delim,tokens);
    
    List<String> strings = Pattern.compile(delim)
        .splitAsStream(text2)
        .collect(Collectors.toList());
    PrintTokens(text2,delim,strings.toArray());
  }
}
