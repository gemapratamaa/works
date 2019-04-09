import java.util.*;

class Solution {

	public static void main(String[] args) {

		Scanner in = new Scanner(System.in);
		int testCases = Integer.parseInt(in.nextLine());
		List<Student> studentList = new ArrayList<Student>();

		while (testCases > 0) {
			int id = in.nextInt();
			String fname = in.next();
			double cgpa = in.nextDouble();
			
			Student st = new Student(id, fname, cgpa);
			studentList.add(st);
			
			testCases--;
		}
      
      	Student[] studentArr = new Student[studentList.size()];
      	studentArr = studentList.toArray(studentArr);

      	selectionSort(studentArr);

      	for (Student student : studentArr) {
      		System.out.println(student.getFname());
      	}
	}

	public static void selectionSort(Student[] arr) {
        int n = arr.length;
        int minIndex;
        for(int i = 0; i < n; i++) {
            minIndex = i;
            for(int j = i + 1; j < n; j++) {
                if (arr[j].compareTo(arr[minIndex]) < 0) {
                    minIndex = j;
                }
            }
            Student temp = arr[minIndex];
            arr[minIndex] = arr[i];
            arr[i] = temp;
        }
    }

}

class Student {

	private int id;
	private String fname;
	private double cgpa;

	public Student(int id, String fname, double cgpa) {
		super();
		this.id = id;
		this.fname = fname;
		this.cgpa = cgpa;
	}

	public int getId() {
		return id;
	}

	public String getFname() {
		return fname;
	}

	public double getCgpa() {
		return cgpa;
	}

	public int compareTo(Student other) {
		if (this.getCgpa() < other.getCgpa()) {
			return 1;
		} else if (this.getCgpa() > other.getCgpa()) {
			return -1;
		} else {
			if (this.getFname().compareTo(other.getFname()) < 0) {
				return -1;
			} else if (this.getFname().compareTo(other.getFname()) > 0) {
				return 1;
			} else {
				if (this.getId() > other.getId()) {
					return -1;
				} else if (this.getId() < other.getId()) {
					return 1;
				}
			}
		}
		return 0;
	}

}