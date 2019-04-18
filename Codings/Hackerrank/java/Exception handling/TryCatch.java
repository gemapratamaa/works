import java.io.*;
import java.util.*;
class Solution {

    public static void main(String[] args) {
        try {
            Scanner sc = new Scanner(System.in);
            int x = Integer.parseInt(sc.nextLine());
            int y = Integer.parseInt(sc.nextLine());
            System.out.println(x / y);
        } catch (ArithmeticException ae) {
            System.out.println("java.lang.ArithmeticException: / by zero");
        } catch (Exception e) {
            System.out.println("java.util.InputMismatchException");
        }
    }
}

