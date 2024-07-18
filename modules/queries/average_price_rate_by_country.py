import pandas as pd

class averagePriceRateByCountry:

    """
    A class used to represent and process the average price rate by country from a database.

    Attributes
    ----------
    conn : psycopg2.connection
        A connection to the PostgreSQL database.

    Methods
    -------
    generateQuery():
        Generates the SQL query to retrieve average price rate data by country.
    
    makeDataFrameFromQuery():
        Executes the generated SQL query and returns the result as a pandas DataFrame.
    """

    def __init__(self,conn) -> None:
        """
        Constructs all the necessary attributes for the averagePriceRateByCountry object.

        Parameters
        ----------
        conn : psycopg2.connection
            A connection to the PostgreSQL database.
        """
        self.conn = conn
        
    def generateQuery(self):

        """
        Generates the SQL query to retrieve average price rate data by country.

        The query selects the minimum, maximum, and average prices of products,
        grouped by the distributor's country.

        Returns
        -------
        str
            The SQL query string.
        """

        self.query = """
        SELECT 
            d.country,
            MIN(p.price) AS min_price,
            MAX(p.price) AS max_price,
            AVG(p.price) AS avg_price
        FROM 
            products p
        JOIN 
            distributors d ON p.distributor_id = d.distributor_id
        GROUP BY 
            d.country;
        """

        return self.query

    def makeDataFrameFromQuery(self):
        """
        Executes the generated SQL query and returns the result as a pandas DataFrame.

        This method calls `generateQuery()` to create the SQL query,
        then uses the connection attribute to execute the query and fetch the results.

        Returns
        -------
        pd.DataFrame
            A DataFrame containing the minimum, maximum, and average prices of products
            grouped by the distributor's country.
        """
        self.generateQuery()
        self.df = pd.read_sql(self.query,self.conn)
        return self.df