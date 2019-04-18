import java.io.*;
import java.util.*;

public class Statprob {

	public static void main(String[] args) {
		try {
			Scanner s3 = new Scanner(new File("soal3.txt"));
            Scanner s2 = new Scanner(new File("soal2.txt"));
            Scanner s4 = new Scanner(new File("soal4.txt"));
			ArrayList<Double> soal3 = new ArrayList<Double>();
            ArrayList<Double> soal2 = new ArrayList<Double>();
            ArrayList<String> soal4 = new ArrayList<String>();
            ArrayList<Double> soal4tinggi = new ArrayList<Double>();
            ArrayList<Double> soal4berat = new ArrayList<Double>();
            ArrayList<Double> soal4BMI = new ArrayList<Double>();

            int[] population = {6289365,16239222,17461022,6862886,6088330,
                9983066,17232482,16991218,6614211,5772938,5553851,5287719};
            int[] suicides = {2297,5241,5507,1948,1091,1509,2292,2024,685,408,62,28};

            System.out.println("PEARSON COEFFICIENT: " + pearson(population, suicides));
            System.out.println("SPEARMAN RHO: " + spearman(population, suicides));

            System.out.println();

            while (s4.hasNextLine()) {
                soal4.add(s4.nextLine());
            }
            for (String s : soal4) {
                String[] split = s.split(" ");
                Double tinggi = (Double) Double.parseDouble(split[0]) / 100.0;
                Double berat = Double.parseDouble(split[1]); 
                soal4tinggi.add(tinggi);
                soal4berat.add(berat);
            }

            for (int i = 0; i < soal4tinggi.size(); i++) {
                Double tinggi = soal4tinggi.get(i);
                Double berat = soal4berat.get(i);
                Double bmi = berat / (tinggi * tinggi);
                soal4BMI.add(bmi);
            }
			while (s3.hasNextLine()) {
				soal3.add((Double) Double.parseDouble(s3.nextLine()));
			}

            while (s2.hasNextLine()) {
                soal2.add(Double.parseDouble(s2.nextLine()));
            }

            //Collections.sort(soal4BMI);
            //for (int i = 0; i < soal4BMI.size(); i++) {
            //    System.out.println((i + 1) + " : " + soal4BMI.get(i));
            //}
			
			Collections.sort(soal3);
            Collections.sort(soal2);
            System.out.println("MEAN: " + getMean(soal4BMI));
            System.out.println("VARIANCE: " + getVariance(soal4BMI));
            System.out.println("STD DEV: " + getStdDev(soal4BMI));

			//for (int i = 1; i <= soal3.size(); i++) {
			//	System.out.println(i + " : " + soal3.get(i-1));
			//}
            //for (int i = 1; i <= soal2.size(); i++) {
            //    System.out.println(i + " : " + soal2.get(i - 1));
            //}
			//System.out.println(soal3);
            for (int i = 20; i <= 1000; i+=60) {
                System.out.println(i);
            }
		} catch (Exception e) {
			System.out.println(e);
		}
	}

	public static double mode(Double[] array) {
        double mode = array[0];
        int maxCount = 0;
        for (int i = 0; i < array.length; i++) {
            double value = array[i];
            int count = 0;
            for (int j = 0; j < array.length; j++) {
                if (array[j] == value) count++;
                if (count > maxCount) {
                    mode = value;
                    maxCount = count;
                    }
                }
        }
        if (maxCount > 1) {
            return mode;
        }
        return 0;
    }

    public static double spearman(int[] x, int[] y) {
        Double n = Double.valueOf(x.length);
        List<Double> rankX = rankify(x, x.length);
        List<Double> rankY = rankify(y, y.length);
        List<Double> dSquared = new ArrayList<Double>();
        for (int i = 0; i < x.length; i ++) {
            double difference = rankX.get(i) - rankY.get(i);
            dSquared.add(difference * difference);
        }

        double sigmaDSquared = 0.0;
        for (Double d : dSquared) {
            sigmaDSquared += d;
            System.out.println(d);
        }
        System.out.println("D2 = " +sigmaDSquared);
        double rho = 1.0 - (6.0 * sigmaDSquared / (n*n*n - n));
        return rho;
    }

    public static double getMean(ArrayList<Double> array) {
    	double dataSum = 0.0;
    	for (Double x : array) {
    		dataSum += x;
    	}
    	return dataSum / array.size();
    }

    public static double getVariance(ArrayList<Double> array) {
    	double mean = getMean(array);
    	double sumDataMinusMean = 0.0;
    	for (Double x : array) {
    		double dataMinusMean = (x - mean) * (x - mean);
    		sumDataMinusMean += dataMinusMean;
    	}
    	return (sumDataMinusMean) / (array.size() - 1);
    }

    public static double getStdDev(ArrayList<Double> array) {
    	double variance = getVariance(array);
    	return Math.pow(variance, 0.5);
    }

    public static int[] reverse2(int[] array) {
        for (int i=0; i < array.length / 2; i++) {   
            int temp = array[i];
            array[i] = array[array.length - i - 1];
            array[array.length - i - 1] = temp;
        }
        return array;
    }

    public static List<Double> rankify(int A[], int n) { 
        Double R[] = new Double[n]; 
        for (int i = 0; i < n; i++) { 
            int r = 1, s = 1; 
            for (int j = 0; j < n; j++)  { 
                if (j != i && A[j] < A[i]) 
                    r += 1; 
                      
                if (j != i && A[j] == A[i]) 
                    s += 1;      
            } 
          
        R[i] = r + (double)(s - 1) /  2.0; 
        
        }  
        
        List<Double> reversed = Arrays.asList(R);
        Collections.reverse(reversed);
        return reversed;     
    } 

    public static double pearson(int[] x, int[] y) {
        ArrayList<Double> arrayListX = new ArrayList<Double>(); 
        ArrayList<Double> arrayListY = new ArrayList<Double>(); 
        for (Integer i : x) {
            arrayListX.add(Double.valueOf(i));
        }
        for (Integer i : y) {
            arrayListY.add(Double.valueOf(i));
        }
        int n = x.length;
        double xbar = getMean(arrayListX);
        double ybar = getMean(arrayListY);

        double xminxbaryminybar = 0.0;
        double xminxbarsquared = 0.0;
        double yminybarsquared = 0.0;

        for (int i = 0; i < x.length; i ++) {
            double xminxbar = x[i] - xbar;
            double yminybar = y[i] - ybar;
            xminxbaryminybar += (xminxbar * yminybar);
            xminxbarsquared += (xminxbar * xminxbar);
            yminybarsquared += (yminybar * yminybar);
        }   
        double product = xminxbarsquared * yminybarsquared;
        double root = Math.pow(product, 0.5);

        return xminxbaryminybar / root; 

    }
}
