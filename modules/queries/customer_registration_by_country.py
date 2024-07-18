import pandas as pd

class customerRegistrationByCountry:

    """
    A class used to represent and process customer registration data by country from a database.

    Attributes
    ----------
    conn : psycopg2.connection
        A connection to the PostgreSQL database.

    Methods
    -------
    generateQuery():
        Generates the SQL query to retrieve customer registration data by country and year.
    
    makeDataFrameFromQuery():
        Executes the generated SQL query and returns the result as a pandas DataFrame.
    """

    def __init__(self,conn):

        """
        Constructs all the necessary attributes for the customerRegistrationByCountry object.

        Parameters
        ----------
        conn : psycopg2.connection
            A connection to the PostgreSQL database.
        """

        self.conn = conn

    def generateQuery(self):

        """
        Generates the SQL query to retrieve customer registration data by country and year.

        The query selects the number of customers registered each year, grouped by country, 
        and orders the results by year and country.
        """

        self.query = """
        SELECT
            EXTRACT(YEAR FROM c.registration_date) AS registration_year,
            c.country,
            COUNT(c.customer_id) AS num_customers_registered
        FROM
            customers c
        GROUP BY
            registration_year, c.country
        ORDER BY
            registration_year, c.country;
        """
    
    def makeDataFrameFromQuery(self):

        """
        Executes the generated SQL query and returns the result as a pandas DataFrame.

        This method calls `generateQuery()` to create the SQL query,
        then uses the connection attribute to execute the query and fetch the results.

        Returns
        -------
        pd.DataFrame
            A DataFrame containing the number of customers registered each year, grouped by country.
        """

        self.generateQuery()
        self.df = pd.read_sql(self.query,self.conn)
        return self.df