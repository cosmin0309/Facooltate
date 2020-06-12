import model.Adeverinta;
import model.Secretar;
import model.SecretarSef;
import model.Student;
import repository.StudentRepository;

import java.io.FileWriter;
import java.io.IOException;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.util.ArrayList;
import java.util.Calendar;
import java.util.Scanner;

public class Service {
    ArrayList<Student> studenti = new ArrayList<Student>(); //Creez o lista pentru a salva toti studentii
    ArrayList<Secretar> secretari = new ArrayList<Secretar>();
    ArrayList<Adeverinta> adeverinte = new ArrayList<Adeverinta>();
    SecretarSef secrSef;

    public void add_student(){
        int numar_studenti_de_adaugat;
        System.out.println("Dati numarul de studenti pe care doriti sa ii adaugati:");
        Scanner sc = new Scanner(System.in);
        numar_studenti_de_adaugat = sc.nextInt();
        for(int i = 0; i <numar_studenti_de_adaugat; i++){
            System.out.println("Nume Prenume : \n");
            String numestudent;
            sc.nextLine();
            numestudent = sc.nextLine();
            //System.out.print(numestudent);
            sc.nextLine();
            System.out.println("Grupa : \n");
            int grupa;
            grupa = sc.nextInt();
            Student stud_de_adaugat = new Student(numestudent, grupa);
            this.studenti.add(stud_de_adaugat);
        }

    }

    public void add_secretar(){
        int numar_secretari_de_adaugat;
        System.out.println("Dati numarul de secretari pe care doriti sa ii adaugati:");
        Scanner sc = new Scanner(System.in);
        numar_secretari_de_adaugat = sc.nextInt();
        for(int i = 0; i <numar_secretari_de_adaugat; i++){
            sc.nextLine();
            System.out.println("Nume Prenume:\n");
            String numesecretar = sc.nextLine();
            System.out.println("Specializare: \n");
            String specializare = sc.nextLine();
            System.out.println("Ani :\n");
            String ani = sc.nextLine();
            Secretar secr_de_adaugat = new Secretar(numesecretar, ani, specializare);
            this.secretari.add(secr_de_adaugat);
        }
    }


    public void completati(){
        for(int i = 0; i<this.studenti.size(); i++){
            this.adeverinte.add(this.studenti.get(i).completeazaAdeverinta());
            System.out.println("Am completat pentru studentul" + this.adeverinte.get(i).getStud().getNumeStudent() + " " + this.adeverinte.get(i).getStud().getSpecializare());
        }
        System.out.println("Se distribuie adeverintele in functie de specializarea si anul secretarului");
        for(int i = 0; i < this.adeverinte.size(); i++) {
            if (this.adeverinte.get(i).getStud().getAn() == 1 || this.adeverinte.get(i).getStud().getAn() == 2
                    || this.adeverinte.get(i).getStud().getAn() == 3) {
                if (this.adeverinte.get(i).getStud().getSpecializare().strip() == "Informatica")
                    for (int j = 0; j < this.secretari.size(); j++) {//Caut secretarul de ani 1,2,3 cu specializarea Informatica
                        if (this.secretari.get(j).getSpecializareSecretar().equals("Info")) {
                            this.secretari.get(j).setAdeverinte(this.adeverinte.get(i));
                            break;
                        }
                    }
                if (this.adeverinte.get(i).getStud().getSpecializare().strip() == "Matematica")
                    for (int j = 0; j < this.secretari.size(); j++)//Caut secretarul de ani 1,2,3 cu specializarea Matematica
                        if (this.secretari.get(j).getSpecializareSecretar().equals("Mate")) {
                            this.secretari.get(j).setAdeverinte(this.adeverinte.get(i));
                            break;
                        }
                if (this.adeverinte.get(i).getStud().getSpecializare().equals("CTI"))
                    for (int j = 0; j < this.secretari.size(); j++)//Caut secretarul de ani 1,2,3 cu specializarea CTI
                        if (this.secretari.get(j).getSpecializareSecretar().equals("CTI")) {
                            this.secretari.get(j).setAdeverinte(this.adeverinte.get(i));
                            break;
                        }

            }
            if(this.adeverinte.get(i).getStud().getAn() == 4){
                if (adeverinte.get(i).getStud().getSpecializare().equals("Matematica"))
                    for (int j = 0; j < this.secretari.size(); j++)//Caut Secretarul de an 4 cu specializarea Matematica
                        if (this.secretari.get(j).getSpecializareSecretar().equals("Mate")) {
                            this.secretari.get(j).setAdeverinte(this.adeverinte.get(i));
                            break;
                        }
                if (this.adeverinte.get(i).getStud().getSpecializare().equals("CTI"))
                    for (int j = 0; j < this.secretari.size(); j++)//Caut secretarul de an 4 cu specializarea CTI
                        if (this.secretari.get(j).getSpecializareSecretar().equals("CTI")) {
                            this.secretari.get(j).setAdeverinte(this.adeverinte.get(i));
                            break;
                        }

            }

        }
        for(int i = 0; i < this.secretari.size(); i++)
            this.secretari.get(i).sortAdeverinte();

    }

    public void match_adeverinte(){
        System.out.println("\nSe distribuie adeverintele in functie de specializarea si anul secretarului");
        for(int i = 0; i < this.adeverinte.size(); i++) {
            if (this.adeverinte.get(i).getStud().getAn() == 1 || this.adeverinte.get(i).getStud().getAn() == 2
                    || this.adeverinte.get(i).getStud().getAn() == 3) {
                if (this.adeverinte.get(i).getStud().getSpecializare().strip() == "Informatica")
                    for (int j = 0; j < this.secretari.size(); j++) {//Caut secretarul de ani 1,2,3 cu specializarea Informatica
                        if (this.secretari.get(j).getSpecializareSecretar().equals("Info")) {
                            this.secretari.get(j).setAdeverinte(this.adeverinte.get(i));
                            break;
                        }
                    }
                if (this.adeverinte.get(i).getStud().getSpecializare().strip() == "Matematica")
                    for (int j = 0; j < this.secretari.size(); j++)//Caut secretarul de ani 1,2,3 cu specializarea Matematica
                        if (this.secretari.get(j).getSpecializareSecretar().equals("Mate")) {
                            this.secretari.get(j).setAdeverinte(this.adeverinte.get(i));
                            break;
                        }
                if (this.adeverinte.get(i).getStud().getSpecializare().equals("CTI"))
                    for (int j = 0; j < this.secretari.size(); j++)//Caut secretarul de ani 1,2,3 cu specializarea CTI
                        if (this.secretari.get(j).getSpecializareSecretar().equals("CTI")) {
                            this.secretari.get(j).setAdeverinte(this.adeverinte.get(i));
                            break;
                        }

            }
            if(this.adeverinte.get(i).getStud().getAn() == 4){
                if (adeverinte.get(i).getStud().getSpecializare().equals("Matematica"))
                    for (int j = 0; j < this.secretari.size(); j++)//Caut Secretarul de an 4 cu specializarea Matematica
                        if (this.secretari.get(j).getSpecializareSecretar().equals("Mate")) {
                            this.secretari.get(j).setAdeverinte(this.adeverinte.get(i));
                            break;
                        }
                if (this.adeverinte.get(i).getStud().getSpecializare().equals("CTI"))
                    for (int j = 0; j < this.secretari.size(); j++)//Caut secretarul de an 4 cu specializarea CTI
                        if (this.secretari.get(j).getSpecializareSecretar().equals("CTI")) {
                            this.secretari.get(j).setAdeverinte(this.adeverinte.get(i));
                            break;
                        }

            }

        }
        for(int i = 0; i < this.secretari.size(); i++)
            this.secretari.get(i).sortAdeverinte();

    }

    public void add_secretarSef(){
        System.out.println("Dati numele secretarului sef:\n");
        String nume;
        Scanner sc = new Scanner(System.in);
        nume = sc.nextLine();
        String ani = "1, 2, 3, 4";
        String specializare = "Toate";
        this.secrSef = new SecretarSef(nume, ani, specializare);
    }


    public void send_adev(){
        for(int i = 0; i < this.secretari.size(); i++)
            for(int j = 0; j < this.secretari.get(i).adeverinte.size(); j++) {
                this.secretari.get(i).validareAdeverinta(j);
                if(this.secretari.get(i).adeverinte.get(j).valida == false)
                    this.secrSef.setAdeverinteRespinse(secretari.get(i).getAdeverinte(j));
            }
    }


    public void print_studenti(){
        for(int i = 0; i < this.studenti.size(); i++){
            System.out.print(this.studenti.get(i).getNumeStudent() +" " +  this.studenti.get(i).getGrupa() + "\n");
        }
    }

    public void print_secretari(){
        for(int i = 0; i < this.secretari.size(); i++){
            System.out.print(this.secretari.get(i).getNumeSecretar() +" " +  this.secretari.get(i).getAnSecretar() + this.secretari.get(i).getSpecializareSecretar() +  "\n");
        }
    }

    public void menu(){
        Scanner sc= new Scanner(System.in);
        int optiune = 0;
        while(optiune != 8) {
            System.out.println("Selectati optiunea dorita:\n");
            System.out.println("Adaugati Studenti: 1\n");
            System.out.println("Adaugati Secretar: 2\n");
            System.out.println("Studentii sunt rugati sa isi completeze pe rand adeverintele: 3\n");
            /*Dupa completare se vor distribui adeverintele in functie de specialzarea si anul secretarului*/
            System.out.println("Adaugati un unic Secretar-Sef: 4\n");
            System.out.println("Trimiteti adeverintele respinse catre secretarul sef: 5\n");
            System.out.println("Afisati lista cu toti studentii adaugati: 6\n");
            System.out.println("Afisati lista cu toti secretarii adaugati: 7\n");
            System.out.println("Exit : 8\n");
            optiune = sc.nextInt();
            switch (optiune){
                case 1:
                    this.add_student();
                    break;
                case 2:
                    this.add_secretar();
                    break;
                case 3:
                    this.completati();
                    break;
                case 4:
                    this.add_secretarSef();
                    break;
                case 5:
                    this.send_adev();
                    break;
                case 6:
                    this.print_studenti();
                    break;
                case 7:
                    this.print_secretari();
                    break;
                case 8:
                    break;
            }
        }
    }
    public void writeInCsv(String action, LocalDateTime timp) throws IOException {
        FileWriter csvWriter = new FileWriter("src\\actiune_csv.txt", true);
        csvWriter.append("\n");
        csvWriter.append(action + " ");
        DateTimeFormatter dtf = DateTimeFormatter.ofPattern("yyyy/MM/dd HH:mm:ss");
        csvWriter.append(dtf.format(timp));
        csvWriter.flush();
        csvWriter.close();

    }
    public void menu2() throws IOException {
        SingletonServiceStudent stud = SingletonServiceStudent.getInstance();
        stud.readingCSVFile();
        this.studenti = stud.studenti;
        System.out.println("Am Citit datele despre studenti");
        SingletonServiceSecretar secr = SingletonServiceSecretar.getInstance();
        secr.readingCSVFile();
        this.secretari = secr.secretari;
        System.out.println("Am citit datele despre secretari");

        SingletonServiceAdeverinte adv = SingletonServiceAdeverinte.getInstance();
        adv.readingCSVFile();
        //this.adeverinte = adv;

        SingletonServiceSecretarSef secrS = SingletonServiceSecretarSef.getInstance();
        this.secrSef = secrS.secrSef;
        System.out.println("Am citit datele despre secretarul sef");
        for(int i = 0; i < adv.date.size(); i++) {
            this.studenti.get(i).determinaSpecializareSiAnDinGrupa();
            Adeverinta adv_de_adaugat = new Adeverinta();
            adv_de_adaugat.setStud(this.studenti.get(i));
            adv_de_adaugat.setData(adv.date.get(i));
            this.adeverinte.add(adv_de_adaugat);
        }
        this.match_adeverinte();

        Scanner sc= new Scanner(System.in);
        int optiune = 0;
        while(optiune != 7) {
            System.out.println("Selectati optiunea dorita:\n");
            System.out.println("Adaugati Student: 1\n");//Se va adauga si o data noua pentru adeverinta
            System.out.println("Trimiteti adeverintele respinse catre secretarul sef: 2\n");
            System.out.println("Afisati lista cu toti studentii: 3\n");
            System.out.println("Cititi data unei adeverinte: 4\n");
            System.out.println("Afisati lista cu toti secretarii adaugati: 5\n");
            System.out.println("Afisati lista cu toate adeverintele respinse: 6\n");
            System.out.print("Updatati anul unui student: 7\n");

            System.out.println("Exit :8 \n");
            System.out.println("Optiunea: ");
            optiune = sc.nextInt();
            switch (optiune){
                case 1:
                    this.studenti.add(stud.writingCSVFile());
                    LocalDateTime now = LocalDateTime.now();
                    writeInCsv("adaugare student", now);
                    break;
                case 2:
                    now = LocalDateTime.now();
                    writeInCsv("trimitere adeverinte", now);
                    this.send_adev();
                    break;
                case 3:
                    now = LocalDateTime.now();
                    writeInCsv("print studenti", now);
                    this.print_studenti();
                    break;
                case 4:
                    Adeverinta advv = new Adeverinta();
                    advv.setData(adv.writingCSVFile());
                    advv.setStud(studenti.get(studenti.size() - 1));
                    this.adeverinte.add(advv);
                    now = LocalDateTime.now();
                    writeInCsv("adaugare data pt adeverinta", now);
                    break;
                case 5:
                    now = LocalDateTime.now();
                    writeInCsv("print secretari", now);
                    this.print_secretari();
                    break;
                case 6:
                    for (int i = 0; i < this.secrSef.getAdeverinteRespinse().size(); i++)
                        System.out.println(" Adeverinta lui " + this.secrSef.getAdeverinteRespinse().get(i).getStud().getNumeStudent() + " de la data de "
                                + this.secrSef.getAdeverinteRespinse().get(i).getData().get(Calendar.DAY_OF_MONTH) + " "
                                + this.secrSef.getAdeverinteRespinse().get(i).getData().get(Calendar.MONTH) + " "
                                + this.secrSef.getAdeverinteRespinse().get(i).getData().get(Calendar.YEAR)
                                + " deoarece "+ this.secrSef.getAdeverinteRespinse().get(i).getFeedBack());
                    now = LocalDateTime.now();
                    writeInCsv("print adeverinte gresite", now);
                    break;

                case 7:

                case 8:
                    now = LocalDateTime.now();
                    writeInCsv("Exit", now);
                    break;
            }
        }
    }
}

