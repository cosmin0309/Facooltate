package repository;

import config.DatabaseConfiguration;
import model.Student;

import java.sql.*;

public class StudentRepository {
    
    public void insertStudent(Student student){
        
        String preparedSql = "{all insertStudent(?,?,?,?,?)}";

        Connection databaseConnection = DatabaseConfiguration.getDatabaseConnection();

        try {
            CallableStatement cstmt = databaseConnection.prepareCall(preparedSql);
            cstmt.setString(2, student.getNumeStudent());
            cstmt.setInt(3, student.getAn());
            cstmt.setString(4, student.getSpecializare());
            cstmt.setInt(5, student.getGrupa());


            cstmt.registerOutParameter(1, Types.INTEGER);

            cstmt.execute();
            System.out.println("Added user with id:" + cstmt.getInt(1));
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    // PreparedStatement
    public Student getStudentById(int id) {
        String selectSql = "SELECT * FROM students WHERE id=?";

        Connection databaseConnection = DatabaseConfiguration.getDatabaseConnection();
        try {
            PreparedStatement preparedStatement = databaseConnection.prepareStatement(selectSql);
            preparedStatement.setInt(1, id);

            ResultSet resultSet = preparedStatement.executeQuery();
            return maptoStudent(resultSet);
        } catch (SQLException e) {
            e.printStackTrace();
        }
        return null;
    }

    // PreparedStatement
    public void updateStudentAn(int an, int id) {
        String updateAnSql = "UPDATE students SET an=? WHERE id=?";

        Connection databaseConnection = DatabaseConfiguration.getDatabaseConnection();
        try {
            PreparedStatement preparedStatement = databaseConnection.prepareStatement(updateAnSql);
            preparedStatement.setInt(1, an);
            preparedStatement.setInt(2, id);

            preparedStatement.executeUpdate();
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    private Student maptoStudent(ResultSet resultSet) throws SQLException {
        if (resultSet.next()){
            return new Student(resultSet.getInt(1), resultSet.getString(2), resultSet.getInt(3), resultSet.getString(4), resultSet.getInt(5));
        }
        return null;
    }


}

