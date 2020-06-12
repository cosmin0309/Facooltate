import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import model.SecretarSef;

public class SingletonServiceSecretarSef {

    private static SingletonServiceSecretarSef single_instance = null;

    public String filePath;

    public String row;

    public SecretarSef secrSef;

    private SingletonServiceSecretarSef() throws IOException {
        filePath = "src\\secretarsef_csv.txt";
        BufferedReader csvReader = new BufferedReader(new FileReader(this.filePath));
        row = csvReader.readLine();
        row = csvReader.readLine();
        secrSef = new SecretarSef(row, "1, 2, 3, 4", "Toate");
    }
    public static SingletonServiceSecretarSef getInstance() throws IOException {
        if (single_instance == null)
            single_instance = new SingletonServiceSecretarSef();
        return single_instance;
    }


}


