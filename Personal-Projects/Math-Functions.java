import java.util.Scanner;


public class Square {

	public static int square(int num) {
		return num * num;
	}
	
	public static int totalsum(int sum) {
		return sum * (sum + 1) /2;
	}
	
	public static long factorial(long fact) {
		long factorial = 1;
		for(int i = 1; i <= fact; i++) {
			factorial = factorial * i;
		}
		return factorial;
	
		
	}
	public static void main(String[] args) {
		
		System.out.println("-------------Math Functions------------");
		System.out.println("---------------------------------------");
		Scanner sc = new Scanner(System.in);
		System.out.print("Insert Number to Square: ");
		int result = sc.nextInt();
		
		result = square(result);
		System.out.println(result);
		System.out.println("---------------------------------------");
		

		Scanner sc_2 = new Scanner(System.in);
		System.out.print("Insert Number to Find its Summation: ");
		System.out.println(totalsum(sc_2.nextInt()));
		System.out.println("---------------------------------------");
		
		
		Scanner sc_3 = new Scanner(System.in);
		System.out.print("Insert Number to Find its Factorial: ");
		long result_3 = sc_3.nextInt();
		
		result_3 = factorial(result_3)	;
		System.out.println(result_3);
		System.out.println("---------------------------------------");
		
		
		sc.close();
		sc_2.close();
		sc_3.close();
		
	}

}
