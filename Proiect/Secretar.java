import java.util.ArrayList;
import java.util.Calendar;
import java.util.Scanner;
public class Secretar {
    String numeSecretar;
    String anSecretar;
    String specializareSecretar;
    ArrayList<Adeverinta> adeverinte = new ArrayList<Adeverinta>();

    public Secretar() {
    }

    public Secretar(String numeSecretar, String anSecretar, String specializareSecretar) {
        this.numeSecretar = numeSecretar;
        this.anSecretar = anSecretar;
        this.specializareSecretar = specializareSecretar;
    }

    public String getNumeSecretar() {
        return numeSecretar;
    }

    public void setNumeSecretar(String numeSecretar) {
        this.numeSecretar = numeSecretar;
    }

    public String getAnSecretar() {
        return anSecretar;
    }

    public void setAnSecretar(String anSecretar) {
        this.anSecretar = anSecretar;
    }

    public String getSpecializareSecretar() {
        return specializareSecretar;
    }

    public void setSpecializareSecretar(String specializareSecretar) {
        this.specializareSecretar = specializareSecretar;
    }

    public Adeverinta getAdeverinte(int i) {
        return adeverinte.get(i);
    }

    public void setAdeverinte(Adeverinta adeverinta) {
        this.adeverinte.add(adeverinta);
    }

    public void sendFeedback(int i){
        System.out.println("De ce nu este valida?");
        Scanner sc = new Scanner(System.in);
        String deCe = sc.nextLine();
        this.adeverinte.get(i).setFeedBack(deCe);
        System.out.println("/*...Adeverinta studentului " + this.adeverinte.get(i).getStud().getNumeStudent() + " de la grupa "
                + this.adeverinte.get(i).getStud().getGrupa() + " a fost respinsa deoarece " + this.adeverinte.get(i).getFeedBack()+"...*/");
    }

    public Adeverinta validareAdeverinta(int i){
        System.out.println("Adeverinta studentului " + this.adeverinte.get(i).getStud().getNumeStudent() +
                " completata la data de " + this.adeverinte.get(i).getData().get(Calendar.DAY_OF_MONTH)+" "+ this.adeverinte.get(i).getData().get(Calendar.MONTH)
                        +" "+this.adeverinte.get(i).getData().get(Calendar.YEAR) + " este valida? (Yes/No)\n");
        Scanner sc = new Scanner(System.in);
        String eValida = sc.nextLine();

        if(eValida.equals("Yes")) {
            System.out.println("/*...Adeverinta studentului " + this.adeverinte.get(i).getStud().getNumeStudent() + " de la grupa "
                    + this.adeverinte.get(i).getStud().getGrupa() + " a fost validata...*/");
            this.adeverinte.get(i).setValida(true);
            return this.adeverinte.get(i);
        }
        else {
            this.sendFeedback(i);
            this.adeverinte.get(i).setValida(false);
            return this.adeverinte.get(i);
        }

    }

    public void sortAdeverinte(){
        System.out.println("Secretarul " + getNumeSecretar() + " isi sorteaza adeverintele in functie de data fiecareia.");
        boolean sem = true;

        System.out.println("Adeverintele alocate secretarului :" + getNumeSecretar());
        for(int i = 0; i<this.adeverinte.size(); i++) {
            System.out.println(adeverinte.get(i).getStud().getNumeStudent() + " " +
                    adeverinte.get(i).getStud().getGrupa() + " " +
                     adeverinte.get(i).getData().get(Calendar.DAY_OF_MONTH)+ " " +
                    adeverinte.get(i).getData().get(Calendar.MONTH) +
                    " " + adeverinte.get(i).getData().get(Calendar.YEAR) + "\n");
        }
        do{
            sem = true;
            for(int i = 0; i<this.adeverinte.size()-1; i++)
                if(this.adeverinte.get(i).getData().after(this.adeverinte.get(i+1).getData())){
                    Adeverinta temp = new Adeverinta();
                    temp = this.getAdeverinte(i);
                    this.adeverinte.set(i, this.adeverinte.get(i + 1));
                    this.adeverinte.set(i + 1, temp);
                    sem = false;
                }

        }while (sem!=true);
            System.out.println("Adeverintele alocate secretarului " + getNumeSecretar() + " in ordine dupa data :");
            for(int i = 0; i<this.adeverinte.size(); i++) {
                System.out.println(adeverinte.get(i).getStud().getNumeStudent() + " " +
                        adeverinte.get(i).getStud().getGrupa() + " " +
                        adeverinte.get(i).getData().get(Calendar.DAY_OF_MONTH) + " " +
                        adeverinte.get(i).getData().get(Calendar.MONTH) +
                        " " + adeverinte.get(i).getData().get(Calendar.YEAR) + "\n");
            }
    }
}
