package config;

import repository.RepositoryHelper;

import java.sql.Connection;
import java.sql.ResultSet;
import java.sql.SQLException;


public class SetUpData {
    public void setUp() {
        String createTableSql = "CREATE TABLE IF NOT EXISTS students" +
                "(id int PRIMARY KEY AUTO_INCREMENT, numeStudent varchar(30)," +
                "an int)" + "specializare varchar(30)" + "grupa int";

        Connection databaseConnection = DatabaseConfiguration.getDatabaseConnection();
        RepositoryHelper repositoryHelper = RepositoryHelper.getRepositoryHelper();

        try {
            repositoryHelper.executeSql(databaseConnection, createTableSql);
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    public void addStudent() {
        String insertStudentSql = "INSERT INTO students(numeStudent, an, specializare, grupa) VALUES('Epure Cosmin', 2,'Informatica', 231)";

        Connection databaseConnection = DatabaseConfiguration.getDatabaseConnection();
        RepositoryHelper repositoryHelper = RepositoryHelper.getRepositoryHelper();

        try {
            repositoryHelper.executeUpdateSql(databaseConnection, insertStudentSql);
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    public void displayStudent() {
        String selectSql = "SELECT * FROM students";

        Connection databaseConnection = DatabaseConfiguration.getDatabaseConnection();
        RepositoryHelper repositoryHelper = RepositoryHelper.getRepositoryHelper();

        try {
            ResultSet resultSet = repositoryHelper.executeQuerySql(databaseConnection, selectSql);
            while (resultSet.next()) {
                System.out.println("Id:" + resultSet.getString(1));
                System.out.println("numeStudent:" + resultSet.getString(2));
                System.out.println("an:" + resultSet.getInt(3));
                System.out.println("specializare:" + resultSet.getString(4));
                System.out.println("an:" + resultSet.getInt(5));

            }

        } catch (SQLException e) {
            e.printStackTrace();
        }
    }
}