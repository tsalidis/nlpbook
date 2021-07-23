
public class Branches
{
	public static void main(String[] args)
	{
		int  a = 5, b = 8, c = 10;
		int  x = 6;
		
		if (x > a && x < b)
			System.out.println("1");
		
		if (x < 5)
			System.out.println("2");
		else if (x > 5 && x < 6)
			System.out.println("3");
		else if (x >=6 && x < 8)
			System.out.println("4");
		else
			System.out.println("5");
		
		switch (c-b+a)
		{
		case 1:
			System.out.println("6");
			break;
		case 2:
			System.out.println("7");
			break;
		case 3:
			System.out.println("8");
			break;
		case 4:
			System.out.println("9");
			break;
		case 5:
			System.out.println("10");
			break;
		case 6:
			System.out.println("11");
			break;
		case 7:
			System.out.println("12");
			break;
		case 8:
			System.out.println("13");
			break;
		case 9:
			System.out.println("14");
			break;
		default:
			System.out.println("15");
			break;	
		}
	}
}
