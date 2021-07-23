
public class Operators
{
	static void BinaryOps()
	{
		int n = 1, k = 4;
		int x = n & k;
		int y = n | k;
		int z = n ^ k;
		int nn = ~n;

		System.out.println("Δυαδικοί τελεστές:");
		System.out.println("n="+n+" ("+Integer.toBinaryString(n)+"), k="+k +" ("+Integer.toBinaryString(k)+"), x=n & k, x=>"+x+" ("+Integer.toBinaryString(x)+")");
		System.out.println("n="+Integer.toBinaryString(n)+", k="+Integer.toBinaryString(k)+", y=n | k, y=>"+Integer.toBinaryString(y));
		System.out.println("n="+Integer.toBinaryString(n)+", k="+Integer.toBinaryString(k)+", z=n^k, z=>"+Integer.toBinaryString(z));
		System.out.println("n="+Integer.toBinaryString(n)+", k="+Integer.toBinaryString(k)+", nn=~n, nn=>"+Integer.toBinaryString(nn));
	}
	
	static void Priority()
	{
		int  n=10, k=5, l=3;
		int  x = n+k*l;

		System.out.println("Προτεραιότητα '*' έναντι '+':");		
		System.out.println("n="+n+", k="+k+", l="+l+", x=n+k*l x=>"+x);		
	}
	
	
	static void Strings()
	{
		String message = "Επεξεργασία";
		
		message = message + " Φυσικής";
		message +=  " Γλώσσας";
		
		System.out.println("Συνένωση κορδονιών:");
		System.out.println("message=\""+message+"\"");
	}
	
	public static void main(String[] args)
	{
		BinaryOps();
		System.out.println();
		Priority();
		System.out.println();
		Strings();
	}
}
