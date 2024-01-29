public class Jack
{
	public static void main(String[] args)
	{
		house();
		malt();
		rat();
		cat();
		dog();
		cow();
		maiden();
	}
	
	public static void house()
	{
		System.out.println("This is the house that Jack built.");
		System.out.println();
	}
	
	public static void malt()
	{
		System.out.println("This is the malt");
		verse1();
	}
	
	public static void rat()
	{
		System.out.println("This is the rat,");
		verse2();
	}
	
	public static void cat()
	{
		System.out.println("This is the cat,");
		verse3();
	}
	
	public static void dog()
	{
		System.out.println("This is the dog,");
		verse4();
	}
	
	public static void cow()
	{
		System.out.println("This is the cow with the crumpled horn,");
		verse5();
	}
	
	public static void maiden()
	{
		System.out.println("This is the maiden all forlorn");
		verse6();
	}
	
	public static void verse1()
	{
		System.out.println("That lay in the house that Jack built.");
		System.out.println();
	}
	
	public static void verse2()
	{
		System.out.println("That ate the malt");
		verse1();
	}
	
	public static void verse3()
	{
		System.out.println("That killed the rat,");
		verse2();
	}
	
	public static void verse4()
	{
		System.out.println("That worried the cat,");
		verse3();
	}
	
	public static void verse5()
	{
		System.out.println("That tossed the dog,");
		verse4();
	}
	
	public static void verse6()
	{
		System.out.println("That milked the cow with the crumpled horn,");
		verse5();
	}
}
