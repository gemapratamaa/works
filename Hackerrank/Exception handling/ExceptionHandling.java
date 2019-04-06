import java.util.Scanner;

class MyCalculator {
    public long power(int a, int b) throws Exception {
    	if (a == 0 && b == 0) {
    		throw new Exception("n and p should not be zero.");
    	} else if (a < 0 || b < 0) {
    		throw new Exception("n or p should not be negative.");
    	}
    	
        long product = 1;
        for (int i = 1; i <= b; i++) {
        	product = product * a;
        }
        return product;
    }
}

class Solution {
    public static final MyCalculator my_calculator = new MyCalculator();
    public static final Scanner in = new Scanner(System.in);
    
    public static void main(String[] args) {
        while (in .hasNextInt()) {
            int n = in .nextInt();
            int p = in .nextInt();
            
            try {
                System.out.println(my_calculator.power(n, p));
            } catch (Exception e) {
                System.out.println(e);
            }
        }
    }
}