package chapter_1;

/**
 * Προτάσεις επανάληψης στην Java 
 * @version 1.0 28/06/2021
 * @author Χρήστος Τσαλίδης
 *
 */
public class Loops
{
	public static void main(String[] args)
	{
		int  i=0;
		
		while (i < 10)
		{
			System.out.println("i="+i);
			i++;
		}

		while (i < 10)
		{
			System.out.println("while (i < 10");
		}
		
		do
			System.out.println("do ... while (i < 10");
		while (i < 10);
		
		
		// Print 0 - 4 
		for (i=0; i < 5; i++)
			System.out.println("i="+i);
		
		
		outer:
		while (i < 20)
		{
			// print 11=15
			while (i > 10)
			{
				System.out.println("i="+i);
				
				if (i == 15)
					break outer;
				break;
			}
			
			i += 1;
		}
	}
}
