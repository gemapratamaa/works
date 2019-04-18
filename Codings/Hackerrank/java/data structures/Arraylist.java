import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;

class Solution {

    public static void main(String[] args) {
        
        Scanner userInput = new Scanner(System.in);

        ArrayList<ArrayList<String>> al = new ArrayList<ArrayList<String>>();

        int firstLine = Integer.parseInt(userInput.nextLine());
        for (int i = 0; i < firstLine; i++) {
        	
        	String[] splitted = userInput.nextLine().split(" ");
        	ArrayList<String> strings = new ArrayList<String>(Arrays.asList(splitted));
        	al.add(strings);
        }

        int queries = Integer.parseInt(userInput.nextLine());
        for (int i = 0; i < queries; i++) {
        	String[] command = userInput.nextLine().split(" ");
        	int n1 = Integer.parseInt(command[0]);
        	int n2 = Integer.parseInt(command[1]);
        	try {
        		System.out.println(al.get(n1 - 1).get(n2));	
        	} catch (IndexOutOfBoundsException ioobe) {
        		System.out.println("ERROR!");
        	}
        	
        }
    }
}