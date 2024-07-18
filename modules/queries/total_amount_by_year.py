import pandas as pd

class totalAmountByYear:
    """
    A class used to query and process the total amount by year from a PostgreSQL database.

    Attributes
    ----------
    conn : psycopg2.connection
        A connection to the PostgreSQL database.

    Methods
    -------
    generateQuery():
        Generates the SQL query to retrieve the total amount by year.
    
    makeDataFrameFromQuery():
        Executes the generated SQL query and returns the results as a pandas DataFrame.
    """

    def __init__(self,conn):
        """
        Constructs all the necessary attributes for the totalAmountByYear object.

        Parameters
        ----------
        conn : psycopg2.connection
            A connection to the PostgreSQL database.
        """
        self.conn = conn

    def generateQuery(self):
        """
        Generates the SQL query to retrieve the total amount by year.

        The query extracts the year from the order date, sums the price multiplied by quantity for each order item,
        groups the results by year, and orders the results by year.

        Returns
        -------
        str
            The generated SQL query as a string.
        """
        self.query = """
        SELECT 
            EXTRACT(year FROM o.order_date) AS order_year,
            SUM(oi.price * oi.quantity) AS total_amount
        FROM 
            orders o
        JOIN 
            order_items oi ON o.order_id = oi.order_id
        GROUP BY 
            order_year
        ORDER BY 
            order_year
        """

    def makeDataFrameFromQuery(self):
        """
        Executes the generated SQL query and returns the results as a pandas DataFrame.

        This method calls `generateQuery()` to create the SQL query,
        then uses the connection attribute to execute the query and fetch the results into a pandas DataFrame.

        Returns
        -------
        pandas.DataFrame
            A DataFrame containing the total amount by year.
        """
        self.generateQuery()
        self.df = pd.read_sql(self.query, self.conn)
        return self.df