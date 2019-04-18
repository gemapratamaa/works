import java.text.SimpleDateFormat;
import java.util.Date;

public class TimeTest {
	
	public static void main(String[] args) throws Exception {

		Date date = new Date();
		SimpleDateFormat sdf0 = new SimpleDateFormat("yyyy-MM-dd");
		SimpleDateFormat sdf1 = new SimpleDateFormat("yyyy_MM_dd");
		SimpleDateFormat sdf2 = new SimpleDateFormat("yyyy MM dd");
		SimpleDateFormat sdf3 = new SimpleDateFormat("EEE, d MMMMM yyyy HH:mm:ss");


		//String dateStr = sdf0.parse("1998-12-08");
		String strDate3 = sdf3.format(date);
		System.out.println(strDate3);
		//System.out.println(dateStr);
	}
}