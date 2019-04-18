import java.util.*;

public class TBA {
	
	public static void main(String[] args) {

		System.out.println("L2");

		for (int a = 0; a <= 10; a ++) {
			for (int b = 0; b <= 10; b ++) {
				if ((b <= 2*a) && (2*a <= 3*b)) {
					System.out.println("a = " + a + ", b = " + b);
				}
			}
		}

		System.out.println("\nL3");
		for (int k = 0; k <= 5; k ++) {
			for (int j = 0; j <= 5; j++) {
				for (int i = 0; i <= 5; i ++) {
					if (i + k + 2 == j) {
						System.out.println("i = " + i + ", j = " + j + " , k = " + k);
					}
				}
			}
		}

		System.out.println("\nL4");
		for (int d = 0; d <= 2; d ++) {
			for (int c = 0; c <= 2; c++) {
				for (int b = 0; b <= 2; b ++) {
					for (int a = 0; a <= 2; a ++) {
						if ((b + a) == (c + d)) {
							System.out.println("a = " + a + ", b = " + b + ", c = " + c + ", d = " + d);
						}
					}
				}
			}
		}


	}

}
