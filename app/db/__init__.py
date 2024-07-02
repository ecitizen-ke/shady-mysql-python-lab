import mysql.connector
import os
class DbConnection:
    def __init__(self):
        self.host = os.getenv('DB_HOST')
        self.db=os.getenv('DB_NAME')
        self.username = os.getenv('root')
        self.password = os.getenv('DB_PASSWORD')

        # create connection
        self.conn = mysql.connector.connect(host=self.host,user=self.user,password=self.password,database=self.db)

        self.cursor = self.conn.cursor()

