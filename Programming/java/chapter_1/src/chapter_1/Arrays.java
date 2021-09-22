package chapter_1;

public class Arrays
{
	public static void main(String[] args)
	{
		int[] a   = new int[100];
		int   b[] = new int[100];
		int[] c   = { 1, 2, 4, 55, 99 };
		String[] names = { "Apple", "Microsoft", "Oracle" };
		String[] company_names = names;
		
		for (int i=0; i < names.length; i++)
			System.out.println(names[i]);

		for (String name : company_names)
			System.out.println(name);
	}
}
