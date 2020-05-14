import java.io.IOException;

public class Main {
    public static void main(String[] args) throws IOException {
       Service serv = new Service();
       serv.menu2();
       //serv.menu();
       /* SingletonServiceSecretar serv = SingletonServiceSecretar.getInstance();
        serv.readingCSVFile();
        for(int i = 0; i < serv.secretari.size(); i++)
            System.out.println(serv.secretari.get(i).getNumeSecretar() + " " +
                    serv.secretari.get(i).getAnSecretar() + " " + serv.secretari.get(i).getSpecializareSecretar());
*/
      /*  SingletonServiceAdeverinte serv = SingletonServiceAdeverinte.getInstance();
        serv.readingCSVFile();
        for(int i = 0; i < serv.date.size(); i++)
            System.out.println(serv.date.get(i).get(Calendar.DAY_OF_MONTH) +
                    " " + serv.date.get(i).get(Calendar.MONTH) +
                    " " + serv.date.get(i).get(Calendar.YEAR));
        SingletonServiceSecretarSef servs = SingletonServiceSecretarSef.getInstance();
        System.out.println(servs.secrSef.getNumeSecretar() + " " + servs.secrSef.getAnSecretar() + " " + servs.secrSef.getSpecializareSecretar());

      SingletonServiceAdeverinte serv = SingletonServiceAdeverinte.getInstance();
      serv.writingCSVFile();*/



    }

}