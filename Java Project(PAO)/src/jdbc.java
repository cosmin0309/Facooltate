import config.DatabaseConfiguration;
import model.Secretar;
import model.Student;
import repository.RepositoryHelper;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;

public class jdbc{
    public void setStudent()
    {

        String createTableSql = "CREATE TABLE IF NOT EXISTS students" +
                "(id int PRIMARY KEY AUTO_INCREMENT, numeStudent varchar(30), an int ,specializare varchar(30))";

        Connection databaseConnection = DatabaseConfiguration.getDatabaseConnection();
        RepositoryHelper repositoryRepositoryHelper = RepositoryHelper.getRepositoryHelper();

        try {
            repositoryRepositoryHelper.executeSql(databaseConnection, createTableSql);
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }
    public void addStudent(Student student) {
        String insertStudent = "INSERT INTO students(numeStudent,an,specializare,grupa) VALUES('" + student.getNumeStudent() + "','" + student.getAn() + "','" + student.getSpecializare() +"'," + student.getGrupa() + ")";
        Connection databaseConnection = DatabaseConfiguration.getDatabaseConnection();
        RepositoryHelper databaseRepositoryHelper = RepositoryHelper.getRepositoryHelper();

        try {
            databaseRepositoryHelper.executeSql(databaseConnection, insertStudent);
        } catch (SQLException throwables) {
            throwables.printStackTrace();
        }
    }
    public ArrayList<Student> readStudent() {
        String selectStudent = "SELECT * FROM students";
        Connection databaseConnection = DatabaseConfiguration.getDatabaseConnection();
        RepositoryHelper databaseRepositoryHelper = RepositoryHelper.getRepositoryHelper();
        ArrayList<Student> students = new ArrayList<Student>();
        try {
            PreparedStatement preparedStatement = databaseConnection.prepareStatement(selectStudent);
            ResultSet resultSet = preparedStatement.executeQuery();
            while(resultSet.next()) {
                Student student = new Student(resultSet.getString(2),resultSet.getInt(3),resultSet.getString(4),resultSet.getInt(5));
                students.add(student);
            }
        } catch (SQLException throwables) {
            throwables.printStackTrace();
        }
        return students;
    }
    public void deleteStudent(Student student)
    {
        String deleteStudent = "DELETE FROM students WHERE numeStudent = '" + student.getNumeStudent()  + "' and grupa = '" + student.getGrupa() + "'";
        System.out.print(deleteStudent);
        Connection databaseConnection =  DatabaseConfiguration.getDatabaseConnection();
        RepositoryHelper databaseRepositoryHelper = RepositoryHelper.getRepositoryHelper();

        try {
            databaseRepositoryHelper.executeSql(databaseConnection, deleteStudent);
        } catch (SQLException throwables) {
            throwables.printStackTrace();
        }
    }
    public void setSecretar()
    {

        String createTableSql = "CREATE TABLE IF NOT EXISTS secretars" +
                "(id int PRIMARY KEY AUTO_INCREMENT, numeSecretar varchar(30),anSecretar varchar(2),specializareSecretar varchar(20)";

        Connection databaseConnection = DatabaseConfiguration.getDatabaseConnection();
        RepositoryHelper repositoryRepositoryHelper = RepositoryHelper.getRepositoryHelper();

        try {
            repositoryRepositoryHelper.executeSql(databaseConnection, createTableSql);
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }
    public void addSecretar(Secretar secretar)
    {

        String insertStudent = "INSERT INTO secreatars(numeSecretar,anSecretar,specializareSecretar) VALUES('" + secretar.getNumeSecretar() + "','" + secretar.getAnSecretar() + "'," + secretar.getSpecializareSecretar() + ")";
        Connection databaseConnection = DatabaseConfiguration.getDatabaseConnection();
        RepositoryHelper databaseRepositoryHelper = RepositoryHelper.getRepositoryHelper();

        try {
            databaseRepositoryHelper.executeSql(databaseConnection, insertStudent);
        } catch (SQLException throwables) {
            throwables.printStackTrace();
        }
    }
    public ArrayList<Secretar> readSecretar() {
        String selectSecretar = "SELECT * FROM secretars";
        Connection databaseConnection = DatabaseConfiguration.getDatabaseConnection();
        RepositoryHelper databaseRepositoryHelper = RepositoryHelper.getRepositoryHelper();
        ArrayList<Secretar> secretars = new ArrayList<Secretar>();
        try {
            PreparedStatement preparedStatement = databaseConnection.prepareStatement(selectSecretar);
            ResultSet resultSet = preparedStatement.executeQuery();
            while(resultSet.next()) {
                Secretar secretar = new Secretar(resultSet.getString(2), resultSet.getString(3), resultSet.getString(4));
                secretars.add(secretar);
          }
        } catch (SQLException throwables) {
            throwables.printStackTrace();
        }
        return secretars;
    }
    public void deleteSecretar(Secretar secretar)
    {
        String deletesql = "DELETE FROM secretars WHERE numeSecretar =" + secretar.getNumeSecretar()  + "and  specializareSecretar = " + secretar.getSpecializareSecretar();
        Connection databaseConnection =  DatabaseConfiguration.getDatabaseConnection();
        RepositoryHelper databaseRepositoryHelper = RepositoryHelper.getRepositoryHelper();

        try {
            databaseRepositoryHelper.executeSql(databaseConnection, deletesql);
        } catch (SQLException throwables) {
            throwables.printStackTrace();
        }
    }

    public static void main(String[] args)
    {
        jdbc jdbc =  new jdbc();


    }
}