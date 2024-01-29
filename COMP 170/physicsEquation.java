public class physicsEquation
{
	public static void main(String[] args)
	{
		double s0;
		double v0;
		double a;
		double t;
		double s;
		
		s0 = 12.0;
		v0 = 3.5;
		a = 9.8;
		t = 10.0;
		
		s = s0 + (v0 * t) + (0.5 * a * t * t);
		
		System.out.println("Initial position s0: " + s0);
		System.out.println("Initial velocity v0: " + v0);
		System.out.println("Given time t: " + t);
		System.out.println("Rate of acceleration a: " + a);
		System.out.println("Position s if a body in linear motion: " + s);
	}
}