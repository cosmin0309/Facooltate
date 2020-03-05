import java.util.Scanner;

class Problema1{
    void rezolvare(){
        int[] catalog = new int[20];
        Scanner scanner = new Scanner(System.in);
        int i;
        float suma = 0;
        for ( i =  1; i <=20; i++) {

            catalog[i] = scanner.nextInt();
            if(catalog[i] == -1) {
                i--;
                System.out.println("Media : " + suma/i);
                break;
            }
            suma += catalog[i];
        }

    }
}
//Problema 2
class Person{
    String name;
    String surname;
    String age;
    long id_number;
    String type;

    public Person(String name, String surname, String age, long id_number, String type) {
        this.surname = surname;
        this.name = name;
        this.age = age;
        this.id_number = id_number;
        this.type = type;
    }

    public String getSurname() {
        return surname;
    }

    public void setSurname(String surname) {
        this.surname = surname;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getAge() {
        return age;
    }

    public void setAge(String age) {
        this.age = age;
    }

    public long getId_number() {
        return id_number;
    }

    public void setId_number(long id_number) {
        this.id_number = id_number;
    }

    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
}

class Room{
    String room_number;
    String room_type;
    String room_floor;

    public Room(String room_number, String room_type, String room_floor) {
        this.room_number = room_number;
        this.room_type = room_type;
        this.room_floor = room_floor;
    }

    public String getRoom_number() {
        return room_number;
    }

    public void setRoom_number(String room_number) {
        this.room_number = room_number;
    }

    public String getRoom_type() {
        return room_type;
    }

    public void setRoom_type(String room_type) {
        this.room_type = room_type;
    }

    public String getRoom_floor() {
        return room_floor;
    }

    public void setRoom_floor(String room_floor) {
        this.room_floor = room_floor;
    }

}

class Subject{
    Room room;
    int noOfStudents;
    Person teacher;

    public Subject(Room room, int noOfStudents, Person teacher) {
        this.room = room;
        this.noOfStudents = noOfStudents;
        this.teacher = teacher;
    }


    public int getNoOfStudents() {
        return noOfStudents;
    }

    public void setNoOfStudents(int noOfStudents) {
        this.noOfStudents = noOfStudents;
    }

}
class Scratch {
    public static void main(String[] args) {
        Problema1 p1 = new Problema1();
        //p1.rezolvare();
        Person person1 = new Person("John", "Doe", "24", 1123444, "student");
        Person person2 = new Person("Jane", "Roe", "56", 2233444, "teacher");
        /*System.out.println("Person 1 : ");
        System.out.println(person1.getName());
        System.out.println(person1.getSurname());
        System.out.println(person1.getAge());
        System.out.println(person1.getId_number());
        System.out.println(person1.getType());
        System.out.println("\nPerson 2 : ");
        System.out.println(person2.getName());
        System.out.println(person2.getSurname());
        System.out.println(person2.getAge());
        System.out.println(person2.getId_number());
        System.out.println(person2.getType());
       */
      Room room1 = new Room("12A", "normal", "3");
      Room room2 = new Room("12B", "tech", "7");
      System.out.println("Room 1 :" + room1.getRoom_number() + " " + room1.getRoom_type() + " " + room1.getRoom_floor());

      System.out.println("Room 2 :" + room2.getRoom_number() + " " + room2.getRoom_type() + " " + room2.getRoom_floor());
      Subject subject1 = new Subject(room1, 25,person1);
      Subject subject2 = new Subject(room2, 23, person2);

      System.out.println(subject1.room.getRoom_number() +" " + subject1.room.getRoom_type() + " " + " " + subject1.room.getRoom_floor() + " " + subject1.teacher.getName()+ " " + subject1.teacher.getId_number() + " " + subject1.teacher.getAge() + " " + subject1.teacher.getType() + " " + subject1.getNoOfStudents());
      System.out.println(subject2.room.getRoom_number() +" " + subject2.room.getRoom_type() + " " + " " + subject2.room.getRoom_floor() + " " + subject2.teacher.getName()+ " " + subject2.teacher.getId_number() + " " + subject2.teacher.getAge() + " " + subject2.teacher.getType() + " " + subject2.getNoOfStudents());

    }
}
