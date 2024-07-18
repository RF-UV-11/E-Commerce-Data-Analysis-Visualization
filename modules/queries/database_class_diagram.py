import pandas as pd

class databaseClassDiagram:
    """
    A class used to represent and process the database class diagram from a PostgreSQL database.

    Attributes
    ----------
    conn : psycopg2.connection
        A connection to the PostgreSQL database.

    Methods
    -------
    generateQuery():
        Generates the SQL query to retrieve the database schema information.
    
    makeRelationInfo():
        Executes the generated SQL query and returns the relationship information.
    """

    def __init__(self,conn):
        """
        Constructs all the necessary attributes for the databaseClassDiagram object.

        Parameters
        ----------
        conn : psycopg2.connection
            A connection to the PostgreSQL database.
        """
        self.conn = conn

    def generateQuery(self):
        """
        Generates the SQL query to retrieve the database schema information.

        The query selects the table names, column names, foreign table names, foreign column names,
        and constraint types for primary key and foreign key constraints.
        """
        self.query = """
        SELECT 
            tc.table_name AS table_name,
            kcu.column_name AS column_name,
            ccu.table_name AS foreign_table_name,
            ccu.column_name AS foreign_column_name,
            tc.constraint_type
        FROM 
            information_schema.table_constraints AS tc 
        JOIN 
            information_schema.key_column_usage AS kcu 
        ON 
            tc.constraint_name = kcu.constraint_name
        JOIN 
            information_schema.constraint_column_usage AS ccu 
        ON 
            ccu.constraint_name = tc.constraint_name
        WHERE 
            tc.constraint_type IN ('PRIMARY KEY', 'FOREIGN KEY');
        """

    def makeRelationInfo(self):
        """
        Executes the generated SQL query and returns the relationship information.

        This method calls `generateQuery()` to create the SQL query,
        then uses the connection attribute to execute the query and fetch the results.

        Returns
        -------
        list of tuple
            A list of tuples containing the relationship information between tables.
        """
        self.generateQuery()
        # Execute the query
        cursor = self.conn.cursor()
        cursor.execute(self.query)
        self.relationship_info = cursor.fetchall()
        return self.relationship_info