import psycopg2
import os
import json

class postgresConnection:

    """
    A class to handle PostgreSQL database connections using configurations from a JSON file.

    Attributes
    ----------
    connections : dict
        The connections configurations from the JSON file.
    postgres : dict
        The PostgreSQL specific configurations.
    dbname : str
        The name of the database.
    user : str
        The username for the database.
    password : str
        The password for the database.
    host : str
        The host of the database.
    port : str
        The port of the database.
    conn : psycopg2.extensions.connection
        The connection object to the PostgreSQL database.

    Methods
    -------
    configConn(config_file=os.path.join("modules/configs.json"))
        Reads the configuration file and sets the connection attributes.
    makePostgresConnection()
        Establishes and returns a connection to the PostgreSQL database.
    closePostgresConnection()
        Closes the connection to the PostgreSQL database.
    """

    def __init__(self) -> None:

        """Initializes the postgresConnection class without any attributes."""

        pass

    def configConn(self,config_file=os.path.join("modules/configs.json")):

        """
        Reads the configuration file and sets the connection attributes.

        Parameters
        ----------
        config_file : str, optional
            The path to the configuration JSON file (default is "modules/configs.json").
        """

        with open(config_file, 'r') as file:
            config = json.load(file)

        self.connections = config.get("connections")
        self.postgres = self.connections.get("postgres")
        self.dbname = self.postgres.get("dbname")
        self.user = self.postgres.get("user")
        self.password = self.postgres.get("password")
        self.host = self.postgres.get("host")
        self.port = self.postgres.get("port")

    def makePostgresConnection(self):

        """
        Establishes and returns a connection to the PostgreSQL database.

        Returns
        -------
        psycopg2.extensions.connection
            The connection object to the PostgreSQL database.
        """

        self.configConn()
        self.conn = psycopg2.connect(
              dbname=self.dbname,
              user=self.user,
              password=self.password,
              host=self.host,
              port=self.port
        )
        
        return self.conn
    
    def closePostgresConnection(self):

        """
        Closes the connection to the PostgreSQL database.
        """

        self.conn.close()
        return
