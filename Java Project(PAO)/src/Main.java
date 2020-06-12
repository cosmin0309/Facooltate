public class Main {
    public static void main(String[] args) {

/*
      jdbc jdbc = new jdbc();
      jdbc.setStudent();
      Student stud = new Student("John Doe", 1, "CTI", 112);
      jdbc.addStudent(stud);
*/
    /*  *SetUpData setUpData = new SetUpData();

      setUpData.setUp();
      setUpData.addStudent();
      setUpData.displayStudent();

      StudentRepository studentRepository = new StudentRepository();
      Student student = studentRepository.getStudentById(1);

      System.out.println("an = " + student.getAn());

      studentRepository.updateStudentAn(3, 1);
      Student updatedStudent = studentRepository.getStudentById(1);

      System.out.println("an = " + updatedStudent.getAn());

      studentRepository.insertStudent(new Student("Cosmin", 2, "Informatica", 231));

*/
      
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