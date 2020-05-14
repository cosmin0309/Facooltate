import java.util.Calendar;
import java.util.Date;
import java.util.Scanner;

public class Student {
    String numeStudent;
    int an;
    String specializare;
    int grupa;

    public int getGrupa() {
        return grupa;
    }

    public void setGrupa(int grupa) {
        this.grupa = grupa;
    }

    public Student(String numeStudent, int grupa) {
        this.numeStudent = numeStudent;
        this.grupa = grupa;
    }

    public Student() {
    }

    public String getNumeStudent() {
        return numeStudent;
    }

    public void setNumeStudent(String numeStudent) {
        this.numeStudent = numeStudent;
    }

    public int getAn() {
        return an;
    }

    public void setAn(int an) {
        this.an = an;
    }

    public String getSpecializare() {
        return specializare;
    }

    public void setSpecializare(String specializare) {
        this.specializare = specializare;
    }
    public void determinaSpecializareSiAnDinGrupa(){
        this.setAn(this.getGrupa()/100);
        if((1 == this.getGrupa() / 10 % 10) || 2 == this.getGrupa()/ 10 % 10)
            this.setSpecializare("Matematica");
        if((3 == this.getGrupa() / 10 % 10) || 4 == this.getGrupa()/ 10 % 10)
            this.setSpecializare("Informatica");
        if((5 == this.getGrupa() / 10 % 10))
            this.setSpecializare("CTI");

    }
    public Adeverinta completeazaAdeverinta(){
        System.out.println("Studentul " + this.getNumeStudent() +" completeaza adeverinta.");
        Adeverinta adev = new Adeverinta();
        determinaSpecializareSiAnDinGrupa();
        adev.setStud(this);
        System.out.println("Dati data : ");
        Scanner sc = new Scanner(System.in);
        int zi, luna, an;
        zi = sc.nextInt();
        luna = sc.nextInt();
        an = sc.nextInt();
        Date data = new Date(an-1900, luna, zi);
        Calendar calendar = Calendar.getInstance();
        calendar.setTime(data);
        adev.setData(calendar);
        return adev;
    }
}
