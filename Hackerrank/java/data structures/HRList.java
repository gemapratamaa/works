import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;
import java.util.List;

class Solution {

    public static void main(String[] args) {

        Scanner userInput = new Scanner(System.in);
        int n = Integer.parseInt(userInput.nextLine());
        
        String[] elements = userInput.nextLine().split(" ");
        List<String> l = new ArrayList<String>(Arrays.asList(elements));

        int q = Integer.parseInt(userInput.nextLine()); 

        for (int i = 1; i <= 2 * q; i++) {
            if (i % 2 == 0) {
                String[] commands = userInput.nextLine().split(" ");
                int len = commands.length;
                if (len == 2) {
                    l.add(Integer.parseInt(commands[0]), commands[1]);
                } else if (len == 1) {
                    l.remove(Integer.parseInt(commands[0]));
                }
            } else {
                String dummy = userInput.nextLine();
            }
        }

        for (String s : l) {
            System.out.print(s + " ");
        }
    }
}