import java.util.*;

class Solution {

	public static void main(String[] args) {

		Scanner userInput = new Scanner(System.in);
		int entries = Integer.parseInt(userInput.nextLine());
		HashMap<String, String> map = new HashMap<String, String>();

		for (int i = 1; i <= entries; i ++) {
			String key = userInput.nextLine();
			String value = userInput.nextLine();
			map.put(key, value);			
		}

		for (int i = 1; i <= entries; i++) {
			String target = userInput.nextLine();
			String value = map.get(target);
			if (value == null) {
				System.out.println("Not found");
			} else {
				System.out.println(target + "=" + map.get(target));
			}			
		}

	}
}