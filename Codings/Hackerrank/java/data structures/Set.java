import java.util.*;

class Solution {

	public static void main(String[] args) {
 
		Scanner userInput = new Scanner(System.in);
		int q = Integer.parseInt(userInput.nextLine());

		HashSet<String> hs = new HashSet<String>();

		for (int i = 0; i < q; i++) {

			String target = userInput.nextLine();
			hs.add(target);
			System.out.println(hs.size());
		}
	}
}