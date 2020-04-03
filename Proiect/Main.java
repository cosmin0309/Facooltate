import java.util.ArrayList;
import java.util.Calendar;

public class Main {
    public static void main(String[] args) {
        Student student1 = new Student("Epure Cosmin-Andrei", 231);
        Student student2 = new Student("Popescu Ion", 113);
        Student student3 = new Student("Ionescu Maria", 352);
        Student student4 = new Student("Petrescu Andrei", 451);
        Student student5 = new Student("Georgescu Mihai", 122);
        Student student6 = new Student("Marinescu Maria", 331);
        Secretar secretar1 = new Secretar("Secretar Info", "1,2,3", "Info");
        Secretar secretar2 = new Secretar("Secretar Mate", "1,2,3,4", "Mate");
        Secretar secretar3 = new Secretar("Secretar CTI", "1,2,3", "CTI");
        ArrayList<Secretar> secretari = new ArrayList<Secretar>();
        secretari.add(secretar1);
        secretari.add(secretar2);
        secretari.add(secretar3);
        ArrayList<Adeverinta> adeverinte = new ArrayList<Adeverinta>();
        adeverinte.add(student1.completeazaAdeverinta());
        adeverinte.add(student2.completeazaAdeverinta());
        adeverinte.add(student3.completeazaAdeverinta());
        adeverinte.add(student4.completeazaAdeverinta());
        adeverinte.add(student5.completeazaAdeverinta());
        adeverinte.add(student6.completeazaAdeverinta());
        SecretarSef secrSef = new SecretarSef("Secretar Sef","1,2,3,4", "Toate");
        System.out.println("Se distribuie adeverintele in functie de specializarea si anul secretarului");
        for(int i = 0; i < adeverinte.size(); i++) {
            if (adeverinte.get(i).getStud().getAn() == 1 || adeverinte.get(i).getStud().getAn() == 2
                    || adeverinte.get(i).getStud().getAn() == 3) {
                if (adeverinte.get(i).getStud().getSpecializare() == "Informatica")
                    for (int j = 0; j < secretari.size(); j++)//Caut secretarul de ani 1,2,3 cu specializarea Informatica
                        if (secretari.get(j).getSpecializareSecretar() == "Info") {
                            secretari.get(j).setAdeverinte(adeverinte.get(i));
                            break;
                        }
                if (adeverinte.get(i).getStud().getSpecializare() == "Matematica")
                    for (int j = 0; j < secretari.size(); j++)//Caut secretarul de ani 1,2,3 cu specializarea Matematica
                        if (secretari.get(j).getSpecializareSecretar() == "Mate") {
                            secretari.get(j).setAdeverinte(adeverinte.get(i));
                            break;
                        }
                if (adeverinte.get(i).getStud().getSpecializare() == "CTI")
                    for (int j = 0; j < secretari.size(); j++)//Caut secretarul de ani 1,2,3 cu specializarea CTI
                        if (secretari.get(j).getSpecializareSecretar() == "CTI") {
                            secretari.get(j).setAdeverinte(adeverinte.get(i));
                            break;
                        }

            }
            if(adeverinte.get(i).getStud().getAn() == 4){
                if (adeverinte.get(i).getStud().getSpecializare() == "Matematica")
                    for (int j = 0; j < secretari.size(); j++)//Caut Secretarul de an 4 cu specializarea Matematica
                        if (secretari.get(j).getSpecializareSecretar() == "Mate") {
                            secretari.get(j).setAdeverinte(adeverinte.get(i));
                            break;
                        }
                if (adeverinte.get(i).getStud().getSpecializare() == "CTI")
                    for (int j = 0; j < secretari.size(); j++)//Caut secretarul de an 4 cu specializarea CTI
                        if (secretari.get(j).getSpecializareSecretar() == "CTI") {
                            secretari.get(j).setAdeverinte(adeverinte.get(i));
                            break;
                        }

            }

        }

        for(int i = 0; i < secretari.size(); i++)
            secretari.get(i).sortAdeverinte();
        for(int i = 0; i < secretari.size(); i++)
            for(int j = 0; j < secretari.get(i).adeverinte.size(); j++) {
                secretari.get(i).validareAdeverinta(j);
                if(secretari.get(i).adeverinte.get(j).valida == false)
                    secrSef.setAdeverinteRespinse(secretari.get(i).getAdeverinte(j));
            }
        secrSef.sortAdeverinte();
        System.out.println("Adeverintele Respinse in ordine dupa data sunt:");
        for(int i = 0; i < secrSef.getAdeverinteRespinse().size(); i++)
            System.out.println(secrSef.getAdeverinteRespinse().get(i).getStud().getNumeStudent() + " de la grupa " +
                    secrSef.getAdeverinteRespinse().get(i).getStud().getGrupa() +" " + " adeverinta completata la data de " +
                    secrSef.getAdeverinteRespinse().get(i).getData().get(Calendar.DAY_OF_MONTH) +
                    secrSef.getAdeverinteRespinse().get(i).getData().get(Calendar.MONTH) + " " +
                    secrSef.getAdeverinteRespinse().get(i).getData().get(Calendar.YEAR) + " " + " pe motivul ca " +
                    secrSef.getAdeverinteRespinse().get(i).getFeedBack() + " \n");
    }
}