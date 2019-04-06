import java.util.*;
import java.io.*;
public class NewlineTest {
	
	public static void main(String[] args) throws Exception {

		/*
		Scanner s = new Scanner();
		String[] pesanSplit = new File("test.txt").split("[\\r\\n]+");
		
		ArrayList<String> x = new ArrayList<String>();
		while (s.hasNextLine()) {
  			x.add(s.nextLine());
  			//x += "\n";
		}
		*/

		File file = new File("test.txt"); 
    	Scanner sc = new Scanner(file); 
  	
  		String res = "";
  		ArrayList<String> al = new ArrayList<String>();
	    while (sc.hasNextLine()) {

	      	res += sc.nextLine() + "\n"; 
	    	//al.add(sc.nextLine());
	  	} 


	  	String[] lines = res.split("\\r?\\n");

	  	for (String line : lines) {
	  		System.out.println(line);
	  	}
		//System.out.println(res);
		//System.out.println(al);
	}
}