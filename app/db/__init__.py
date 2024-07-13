import mysql.connector
import os


class DbConnection:
    def __init__(self):
        self.host = os.getenv('DB_HOST')
        self.db = os.getenv('DB_NAME')
        self.user = os.getenv('DB_USER')
        self.password = os.getenv('DB_PASSWORD')

        # create connection
        self.conn = mysql.connector.connect(
            host=self.host, database=self.db, user=self.user, password=self.password
        )

        self.cursor = self.conn.cursor()
