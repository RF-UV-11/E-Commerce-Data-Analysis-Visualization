import pandas as pd

class totalSalesByCountry:
    """
    A class used to query and process the total sales by country from a PostgreSQL database.

    Attributes
    ----------
    conn : psycopg2.connection
        A connection to the PostgreSQL database.

    Methods
    -------
    generateQuery():
        Generates the SQL query to retrieve the total sales amount by country.
    
    makeDataFrameFromQuery():
        Executes the generated SQL query and returns the results as a pandas DataFrame.
    """

    def __init__(self,conn):
        """
        Constructs all the necessary attributes for the totalSalesByCountry object.

        Parameters
        ----------
        conn : psycopg2.connection
            A connection to the PostgreSQL database.
        """
        self.conn = conn
    
    def generateQuery(self):
        """
        Generates the SQL query to retrieve the total sales amount by country.

        The query selects the country and calculates the sum of price multiplied by quantity for each order item,
        joined with orders and customers tables, groups the results by country, and orders the results by total sales amount descending.

        Returns
        -------
        str
            The generated SQL query as a string.
        """
        self.query = """
        SELECT c.country, SUM(oi.price * oi.quantity) AS total_sales_amount
        FROM orders o
        JOIN order_items oi ON o.order_id = oi.order_id
        JOIN customers c ON o.customer_id = c.customer_id
        GROUP BY c.country
        ORDER BY total_sales_amount DESC;
        """
    
    def makeDataFrameFromQuery(self):
        """
        Executes the generated SQL query and returns the results as a pandas DataFrame.

        This method calls `generateQuery()` to create the SQL query,
        then uses the connection attribute to execute the query and fetch the results into a pandas DataFrame.

        Returns
        -------
        pandas.DataFrame
            A DataFrame containing the total sales amount by country.
        """
        self.generateQuery()
        self.df = pd.read_sql(self.query,self.conn)
        return self.df
