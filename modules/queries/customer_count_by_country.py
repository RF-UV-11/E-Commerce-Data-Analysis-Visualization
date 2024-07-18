import pandas as pd

class customerCountByCountry:

    """
    A class used to represent and process the customer count by country from a database.

    Attributes
    ----------
    conn : psycopg2.connection
        A connection to the PostgreSQL database.

    Methods
    -------
    generateQuery():
        Generates the SQL query to retrieve customer count data by country.
    
    makeDataFrameFromQuery():
        Executes the generated SQL query and returns the result as a pandas DataFrame.
    """

    def __init__(self,conn):

        """
        Constructs all the necessary attributes for the customerCountByCountry object.

        Parameters
        ----------
        conn : psycopg2.connection
            A connection to the PostgreSQL database.
        """

        self.conn = conn

    def generateQuery(self):

        """
        Generates the SQL query to retrieve customer count data by country.

        The query selects the number of customers grouped by country and orders
        the results in descending order of customer count.
        """

        self.query = """
        SELECT country, COUNT(*) AS customer_count
        FROM customers
        GROUP BY country
        ORDER BY customer_count DESC;
        """
    
    def makeDataFrameFromQuery(self):

        """
        Executes the generated SQL query and returns the result as a pandas DataFrame.

        This method calls `generateQuery()` to create the SQL query,
        then uses the connection attribute to execute the query and fetch the results.

        Returns
        -------
        pd.DataFrame
            A DataFrame containing the customer count grouped by country.
        """
        
        self.generateQuery()
        self.df = pd.read_sql(self.query, self.conn)
        return self.df