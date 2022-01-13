package chapter_4;

import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class RegularExpressionTest1 
{
  public static void main(String[] args) 
  {
    Pattern pattern    = Pattern.compile("γλωσσολογία", Pattern.CASE_INSENSITIVE | Pattern.UNICODE_CASE);
    Matcher matcher    = pattern.matcher("Υπολογιστική Γλωσσολογία!");
    boolean matchFound = matcher.find();
    
    if(matchFound) 
    {
      System.out.println("Η λέξη 'γλωσσολογία' βρέθηκε");
    } 
    else 
    {
      System.out.println("Η λέξη 'γλωσσολογία' δεν βρέθηκε");
    }
  }
}
