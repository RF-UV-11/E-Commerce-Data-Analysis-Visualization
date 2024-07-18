import pandas as pd

class totalSalesByDistributor:
    """
    A class used to query and process the total sales by distributor from a PostgreSQL database.

    Attributes
    ----------
    conn : psycopg2.connection
        A connection to the PostgreSQL database.

    Methods
    -------
    generateQuery():
        Generates the SQL query to retrieve the total sales amount by distributor.
    
    makeDataFrameFromQuery():
        Executes the generated SQL query and returns the results as a pandas DataFrame.
    """

    def __init__(self,conn) -> None:
        """
        Constructs all the necessary attributes for the totalSalesByDistributor object.

        Parameters
        ----------
        conn : psycopg2.connection
            A connection to the PostgreSQL database.
        """
        self.conn = conn

    def generateQuery(self):
        """
        Generates the SQL query to retrieve the total sales amount by distributor.

        The query selects the distributor name and calculates the sum of price multiplied by quantity for each order item,
        joined with products and distributors tables, groups the results by distributor name.

        Returns
        -------
        str
            The generated SQL query as a string.
        """
        self.query = """
        SELECT 
            d.distributor_name,
            SUM(oi.price * oi.quantity) AS Total_Sales
        FROM 
            order_items oi
        JOIN 
            products p ON oi.product_id = p.product_id
        JOIN 
            distributors d ON p.distributor_id = d.distributor_id
        GROUP BY 
            d.distributor_name
        """
        return self.query

    def makeDataFrameFromQuery(self):
        """
        Executes the generated SQL query and returns the results as a pandas DataFrame.

        This method calls `generateQuery()` to create the SQL query,
        then uses the connection attribute to execute the query and fetch the results into a pandas DataFrame.

        Returns
        -------
        pandas.DataFrame
            A DataFrame containing the total sales amount by distributor.
        """
        self.generateQuery()
        self.df = pd.read_sql(self.query, self.conn)
        return self.df