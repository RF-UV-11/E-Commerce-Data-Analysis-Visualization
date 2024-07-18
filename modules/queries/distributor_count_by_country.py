import pandas as pd

class distributorCountByCountry:
    """
    A class used to query and process the count of distributors by country from a PostgreSQL database.

    Attributes
    ----------
    conn : psycopg2.connection
        A connection to the PostgreSQL database.

    Methods
    -------
    generateQuery():
        Generates the SQL query to retrieve the count of distributors by country.
    
    makeDataFrameFromQuery():
        Executes the generated SQL query and returns the results as a pandas DataFrame.
    """

    def __init__(self,conn):
        """
        Constructs all the necessary attributes for the distributorCountByCountry object.

        Parameters
        ----------
        conn : psycopg2.connection
            A connection to the PostgreSQL database.
        """
        self.conn = conn

    def generateQuery(self):
        """
        Generates the SQL query to retrieve the count of distributors by country.

        The query selects the country and the count of distributors in each country,
        grouping the results by country and ordering them in descending order of distributor count.
        """
        self.query = """
        SELECT country, COUNT(*) AS distributor_count
        FROM distributors
        GROUP BY country
        ORDER BY distributor_count DESC;
        """
    
    def makeDataFrameFromQuery(self):
        """
        Executes the generated SQL query and returns the results as a pandas DataFrame.

        This method calls `generateQuery()` to create the SQL query,
        then uses the connection attribute to execute the query and fetch the results into a pandas DataFrame.

        Returns
        -------
        pandas.DataFrame
            A DataFrame containing the count of distributors by country.
        """
        self.generateQuery()
        self.df = pd.read_sql(self.query,self.conn)
        return self.df
