package repository;

import java.sql.Connection;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;

public class RepositoryHelper {
    private static RepositoryHelper repositoryHelper = new RepositoryHelper();

    private RepositoryHelper() {
    }

    public static RepositoryHelper getRepositoryHelper() {
        return repositoryHelper;
    }

    public void executeSql(Connection connection, String sql) throws SQLException {
        Statement stmt = connection.createStatement();
        // execute() for updating and select instructions
        stmt.execute(sql);
    }

    public void executeUpdateSql(Connection connection, String sql) throws SQLException {
        Statement stmt = connection.createStatement();
        // executeUpdate() for updating the data or the database structure
        stmt.executeUpdate(sql);
    }

    public ResultSet executeQuerySql(Connection connection, String sql) throws SQLException {
        Statement stmt = connection.createStatement();
        // executeQuery() for SELECT instructions
        return stmt.executeQuery(sql);
    }

}