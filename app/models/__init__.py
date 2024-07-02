from app.db import DbConnection
class State:
    def __init__(self):
        self.conn = DbConnection()

    def store(self,name,abbreviation,capital,population,year_admitted):
        """Create new state entry"""
        self.name = name
        self.abbreviation=abbreviation
        self.capital=capital
        self.population=population
        self.year_admitted=year_admitted
        state = (self.name,self.abbreviation,self.capital,self.population,self.year_admitted)
       
        query = "INSERT INTO states (name, abbreviation,capital,population,year_admitted) VALUES(%s, %s,%s, %s,%s)"
        self.conn.cursor.execute(query,state)

        if self.conn.cursor.rowcount:
            # execution was successful
            self.conn.conn.commit()

        self.conn.cursor.close()

        #close connection

        self.conn.conn.close()
    
    def update(self,id,name,abbreviation,capital,population,year_admitted):
        """Update State"""
        # select state where the id = id
        query = "SELECT * FROM states where id=%s"
        self.conn.cursor.execute(query,[id])
        record = self.conn.cursor.fetchone()
        if not record :
            return {
                'message':False,
                'record':None
            }


        update_query = """
            UPDATE states 
            SET name = %s, abbreviation = %s, capital = %s, population = %s, year_admitted = %s 
            WHERE id = %s
        """

        try:
            self.conn.cursor.execute(update_query,[name,abbreviation,capital,population,year_admitted,id])
            self.conn.conn.commit()

        except Exception as e:
            self.conn.rollback()
            return {
                'message': False,
                'error': str(e)
            }
        
