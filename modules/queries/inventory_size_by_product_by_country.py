import pandas as pd

class inventorySizeByProductByCountry:
    """
    A class used to query and process the inventory size by product and country from a PostgreSQL database.

    Attributes
    ----------
    conn : psycopg2.connection
        A connection to the PostgreSQL database.

    Methods
    -------
    generateQuery():
        Generates the SQL query to retrieve the total quantity available of each product by country.
    
    makeDataFrameFromQuery():
        Executes the generated SQL query and returns the results as a pandas DataFrame.
    """

    def __init__(self,conn):
        """
        Constructs all the necessary attributes for the inventorySizeByProductByCountry object.

        Parameters
        ----------
        conn : psycopg2.connection
            A connection to the PostgreSQL database.
        """
        self.conn = conn

    def generateQuery(self):
        """
        Generates the SQL query to retrieve the total quantity available of each product by country.

        The query selects the product name, country, and the sum of the quantity available for each product in each country,
        grouping the results by product name and country, and ordering them in descending order of total quantity available.
        """
        self.query = """
        SELECT
            p.product_name,
            d.country,
            SUM(i.quantity_available) AS total_quantity_available
        FROM
            inventory i
        JOIN
            products p ON i.product_id = p.product_id
        JOIN
            distributors d ON i.distributor_id = d.distributor_id
        GROUP BY
            p.product_name, d.country
        ORDER BY
            total_quantity_available DESC;

        """

    def makeDataFrameFromQuery(self):
        """
        Executes the generated SQL query and returns the results as a pandas DataFrame.

        This method calls `generateQuery()` to create the SQL query,
        then uses the connection attribute to execute the query and fetch the results into a pandas DataFrame.

        Returns
        -------
        pandas.DataFrame
            A DataFrame containing the total quantity available of each product by country.
        """
        self.generateQuery()
        self.df = pd.read_sql(self.query,self.conn)
        return self.df