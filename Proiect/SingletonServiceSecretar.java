import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;

public class SingletonServiceSecretar {
    private static  SingletonServiceSecretar single_instance = null;

    public String filePath;

    public String row;

    public ArrayList<Secretar> secretari = new ArrayList<Secretar>(); //Creez o lista pentru a salva toti studentii

    private SingletonServiceSecretar(){
        filePath = "src\\secretari_csv.txt";
    }

    public static SingletonServiceSecretar getInstance(){
        if (single_instance == null)
            single_instance = new SingletonServiceSecretar();
        return single_instance;
    }

    public void readingCSVFile() throws IOException {
        BufferedReader csvReader = new BufferedReader(new FileReader(this.filePath));
        row = csvReader.readLine();
        while((row = csvReader.readLine()) != null){
            String[] data = row.split(", ");
            Secretar secretar_de_adaugat = new Secretar(data[0], data[2], data[1]);
            secretari.add(secretar_de_adaugat);
        }
    }

}
