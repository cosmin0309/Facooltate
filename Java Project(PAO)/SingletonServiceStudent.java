import java.io.BufferedReader;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Scanner;

public class SingletonServiceStudent {

    private static  SingletonServiceStudent single_instance = null;

    public String filePath;

    public String row;

    public ArrayList<Student> studenti = new ArrayList<Student>(); //Creez o lista pentru a salva toti studentii

    private SingletonServiceStudent(){
        filePath = "src\\studenti_csv.txt";
    }

    public static SingletonServiceStudent getInstance(){
        if (single_instance == null)
             single_instance = new SingletonServiceStudent();
        return single_instance;
    }

    public void readingCSVFile() throws IOException {
        BufferedReader csvReader = new BufferedReader(new FileReader(this.filePath));
        row = csvReader.readLine();
        while((row = csvReader.readLine()) != null){
            String[] data = new String[2];
            data = row.split(", ");
            Student stud_de_adaugat;
            stud_de_adaugat = new Student(data[0], Integer.parseInt(data[1]));
            studenti.add(stud_de_adaugat);
        }
        csvReader.close();
    }
    public Student writingCSVFile() throws IOException {
        FileWriter csvWriter = new FileWriter("src\\studenti_csv.txt", true);
        Scanner sc = new Scanner(System.in);
        System.out.println("Nume Student: ");
        String nume = sc.nextLine();
        System.out.println("Grupa Student: ");
        int grupa = sc.nextInt();
        csvWriter.append(nume);
        csvWriter.append(", ");
        csvWriter.append(String.valueOf(grupa));
        csvWriter.append("\n");
        csvWriter.flush();
        csvWriter.close();
        Student stud = new Student(nume, grupa);
        return stud;
    }
}
