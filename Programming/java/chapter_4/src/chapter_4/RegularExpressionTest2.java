package chapter_4;

public class RegularExpressionTest2 
{
  public static void main(String[] args) 
  {
    String  regexp_a  = "(\\w+)(\\s+)(\\w+)"; 
    String  regexp_g = "([α-ωάέίήόώϊϋΐΰ]+)(\\s+)([α-ωάέίήόώϊϋΐΰ]+)"; 
    String  TEXT_1   = "one      example";
    String  TEXT_2   = "ενα      παραδειγμα";
    
    String  trimmed_1 = TEXT_1.replaceAll(regexp_a ,"$1 $3");
    String  trimmed_2 = TEXT_2.replaceAll(regexp_g ,"$1 $3");
    
    System.out.printf("Old text: |%s|  New text: |%s|\n",TEXT_1,trimmed_1);
    System.out.printf("Old text: |%s|  New text: |%s|\n",TEXT_2,trimmed_2);
  }
}
