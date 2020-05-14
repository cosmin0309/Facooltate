import java.io.BufferedReader;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Calendar;
import java.util.Date;
import java.util.Scanner;

public class SingletonServiceAdeverinte {
    private static  SingletonServiceAdeverinte single_instance = null;

    public String filePath;

    public String row;

    public ArrayList<Calendar> date = new ArrayList<Calendar>() ; //Creez o lista pentru a salva toti studentii

    private SingletonServiceAdeverinte(){
        filePath = "src\\adeverinte_csv.txt";
    }

    public static SingletonServiceAdeverinte getInstance(){
        if (single_instance == null)
            single_instance = new SingletonServiceAdeverinte();
        return single_instance;
    }

    public void readingCSVFile() throws IOException {
        BufferedReader csvReader = new BufferedReader(new FileReader(this.filePath));
        row = csvReader.readLine();
        while((row = csvReader.readLine()) != null){
            String[] data = new String[10];
            data = row.split(" ");
            Date data_de_adaugat = new Date(Integer.parseInt(data[2]) - 1900, Integer.parseInt(data[1]), Integer.parseInt(data[0]));
            Calendar calendar_de_adaugat = Calendar.getInstance();
            calendar_de_adaugat.setTime(data_de_adaugat);
            date.add(calendar_de_adaugat);
        }
    }
    public Calendar writingCSVFile() throws IOException {
        FileWriter csvWriter = new FileWriter("src\\adeverinte_csv.txt", true);
        Scanner sc = new Scanner(System.in);
        System.out.println("Data: ");
        String data = sc.nextLine();
        String[] data_de_adaugat = data.split(" ");
        Calendar calendar_de_adaugat = Calendar.getInstance();
        Date data_de_adauga2 = new Date(Integer.parseInt(data_de_adaugat[2]) - 1900, Integer.parseInt(data_de_adaugat[1]), Integer.parseInt(data_de_adaugat[0]));
        calendar_de_adaugat.setTime(data_de_adauga2);
        csvWriter.append(data);
        csvWriter.append("\n");
        csvWriter.flush();
        csvWriter.close();
        return calendar_de_adaugat;
    }
}
