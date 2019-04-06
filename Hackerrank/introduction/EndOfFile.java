import java.io.*;
import java.util.*;

class Solution {

    public static void main(String[] args) {
        
        Scanner s = new Scanner(System.in);
        int counter = 1;

        while (s.hasNext()) {
            System.out.println(counter + " " + s.nextLine());
            counter++;
        }
    }
}

