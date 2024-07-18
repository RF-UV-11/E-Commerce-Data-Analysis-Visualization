import pandas as pd

class totalAmountByProductCategory:
    """
    A class used to query and process the total amount by product category from a PostgreSQL database.

    Attributes
    ----------
    conn : psycopg2.connection
        A connection to the PostgreSQL database.

    Methods
    -------
    generateQuery():
        Generates the SQL query to retrieve the total amount by product category.
    
    makeDataFrameFromQuery():
        Executes the generated SQL query and returns the results as a pandas DataFrame.
    """

    def __init__(self,conn):
        """
        Constructs all the necessary attributes for the totalAmountByProductCategory object.

        Parameters
        ----------
        conn : psycopg2.connection
            A connection to the PostgreSQL database.
        """
        self.conn = conn

    def generateQuery(self):
        """
        Generates the SQL query to retrieve the total amount by product category.

        The query selects the product category and the sum of the price multiplied by quantity for each order item,
        grouping the results by product category.

        Returns
        -------
        str
            The generated SQL query as a string.
        """
        self.query = """
        SELECT 
            p.category,
            SUM(oi.price * oi.quantity) AS total_amount
        FROM 
            order_items oi
        JOIN 
            products p ON oi.product_id = p.product_id
        GROUP BY 
            p.category

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
            A DataFrame containing the total amount by product category.
        """
        self.generateQuery()
        self.df = pd.read_sql(self.query,self.conn)
        return self.df