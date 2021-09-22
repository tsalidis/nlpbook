package chapter_2;

import java.text.NumberFormat;
import java.util.Locale;

public class LocaleFormatNumber
{
  public static void main(String[] args) 
  {
    double d = 123456.789;
    long   n = 123456789;

    NumberFormat nf = NumberFormat.getInstance(new Locale("en", "US"));
    String dval = nf.format(d);
    String nval = nf.format(n);

    System.out.println(dval);
    System.out.println(nval);

    NumberFormat nf2 = NumberFormat.getInstance(new Locale("el", "GR"));
    String dval2 = nf2.format(d);
    String nval2 = nf2.format(n);

    System.out.println(dval2);
    System.out.println(nval2);
  }
}
