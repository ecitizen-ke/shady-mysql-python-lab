from app.db import DbConnection


class State:
    states = []

    def __init__(self):
        self.conn = DbConnection()

    def get_states(self):
        """select all records from table states"""
        query = "SELECT * FROM states"
        self.conn.cursor.execute(query)

        # Retrieve the user record in the database: returns a tuple
        results = self.conn.cursor.fetchall()
        if results:
            for row in results:
                state = {
                    'id': row[0],
                    'name': row[1],
                    'abbreviation': row[2],
                    'capital': row[3],
                    'population': row[4],
                    'year_admitted': row[5]
                }
                self.states.append(state)
            return self.states
        # Close cursor
        self.conn.cursor.close()
        # Close connection
        self.conn.conn.close()

        return self.states

    def save(self, name, abbreviation, capital, population, year_admitted):
        """Create new state entry"""

        try:
            state = (name, abbreviation, capital, population, year_admitted)

            # Check if state already exists
            query = "SELECT * FROM states WHERE name=%s"
            self.conn.cursor.execute(query, (name,))
            result = self.conn.cursor.fetchone()

            if result:
                return {
                    "message": "State already exists",
                    "status": 409,
                    "result": result
                }

            query = "INSERT INTO states (name, abbreviation,capital,population,year_admitted) VALUES(%s, %s,%s, %s,%s)"
            result = self.conn.cursor.execute(query, state)

            if self.conn.cursor.rowcount:
                # execution was successful
                self.conn.conn.commit()

            self.conn.cursor.close()

            # close connection

            self.conn.conn.close()
            return {
                "message": "State saved successfully",
                "status": 201,
                "result": {
                    'id': self.conn.cursor.lastrowid,
                    'name': name,
                    'abbreviation': abbreviation,
                    'capital': capital,
                    'population': population,
                    'year_admitted': year_admitted
                }
            }
        except Exception as e:
            print(f"Error occurred: {e}")
            return {
                "message": "Error occurred while saving state",
                "status": 500,
                "result": None
            }

    def filter_states_by_starting_letter(self, start_letter):
        """Search for states beginning with a given starting letter"""
        query = "SELECT * FROM states WHERE name LIKE %s"
        self.conn.cursor.execute(query, (start_letter + '%',))
        results = self.conn.cursor.fetchall()
        self.conn.cursor.close()
        # Close connection
        self.conn.conn.close()
        if results:
            for row in results:
                state = {
                    'id': row[0],
                    'name': row[1],
                    'abbreviation': row[2],
                    'capital': row[3],
                    'population': row[4],
                    'year_admitted': row[5]
                }
                self.states.append(state)
            return {
                "message": "States found",
                "status": 200,
                "result": self.states
            }
        else:
            return {
                "message": "No states found",
                "status": 404,
                "result": None
            }

    def update_state_population(self, state_id, new_population):
        """Update the population of a state identified by state_id"""

        query = "UPDATE states SET population = %s WHERE id = %s"

        try:
            self.conn.cursor.execute(query, (new_population, state_id))
            self.conn.conn.commit()  # Commit the transaction
            update_success = True
        except Exception as e:
            print(f"An error occurred: {e}")
            self.conn.conn.rollback()  # Rollback in case of an error
            update_success = False
        finally:
            # Close cursor
            self.conn.cursor.close()
            # Close connection
            self.conn.conn.close()

        if update_success:
            return {
                "message": "Population updated successfully",
                "status": 200,
                "result": None
            }
        else:
            return {
                "message": "Error occurred while updating population",
                "status": 500,
                "result": None
            }

    def delete_state(self, state_id):
        """Delete a state identified by state_id"""

        query = "DELETE FROM states WHERE id = %s"

        try:
            self.conn.cursor.execute(query, (state_id,))
            self.conn.conn.commit()  # Commit the transaction
            delete_success = True
        except Exception as e:
            print(f"An error occurred: {e}")
            self.conn.conn.rollback()  # Rollback in case of an error
            delete_success = False
        finally:
            # Close cursor
            self.conn.cursor.close()
            # Close connection
            self.conn.conn.close()

        if delete_success:
            return {
                "message": "State deleted successfully",
                "status": 200,
                "result": None
            }
        else:
            return {
                "message": "Error occurred while deleting state",
                "status": 500,
                "result": None
            }

    def search_state_by_name(self, state_name):
        """Search for a state by its name"""

        query = "SELECT * FROM states WHERE LOWER(name) = LOWER(%s) ORDER BY id ASC"

        try:
            self.conn.cursor.execute(query, (state_name,))
            result = self.conn.cursor.fetchone()
            state = None

            if result:
                # Assuming the columns are id, name, and population
                state = {
                    'id': result[0],
                    'name': result[1],
                    'population': result[2] if len(result) > 2 else None,
                    'year_admitted': result[3],
                    'abbreviation': result[4],
                    'capital': result[5],
                }
        except Exception as e:
            print(f"An error occurred: {e}")
            state = None
        finally:
            # Close cursor
            self.conn.cursor.close()
            # Close connection
            self.conn.conn.close()

        if state is not None:
            return {
                "message": "State found",
                "status": 200,
                "result": state
            }
        else:
            return {
                "message": "No state found",
                "status": 404,
                "result": None
            }

    def list_all_state_capitals(self):
        """List all state capitals"""

        query = "SELECT id, capital FROM states ORDER BY capital ASC"

        try:
            self.conn.cursor.execute(query)
            results = self.conn.cursor.fetchall()
            capitals_list = []

            if results:
                # Assuming the columns are id and capital
                for row in results:
                    capital = {
                        'id': row[0],
                        'capital': row[1]
                    }
                    capitals_list.append(capital)
        except Exception as e:
            print(f"An error occurred: {e}")
            capitals_list = []
        finally:
            # Close cursor
            self.conn.cursor.close()
            # Close connection
            self.conn.conn.close()
        if len(capitals_list) > 0:
            return {
                "message": "Capitals listed",
                "status": 200,
                "result": capitals_list
            }
        else:
            return {
                "message": "No capitals found",
                "status": 404,
                "result": None
            }

    def find_most_populous_state(self):
        """Find the state with the highest population"""

        query = "SELECT id, name, population FROM states ORDER BY population DESC LIMIT 1"

        try:
            self.conn.cursor.execute(query)
            result = self.conn.cursor.fetchone()
            state = None

            if result:
                # Assuming the columns are id, name, and population
                state = {
                    'id': result[0],
                    'name': result[1],
                    'population': result[2]
                }
        except Exception as e:
            print(f"An error occurred: {e}")
            state = None
        finally:
            # Close cursor
            self.conn.cursor.close()
            # Close connection
            self.conn.conn.close()

        if state is not None:
            return {
                "message": "State found",
                "status": 200,
                "result": state
            }
        else:
            return {
                "message": "No state found",
                "status": 404,
                "result": None
            }

    def calculate_average_population(self):
        """Calculate the average population of all states"""

        query = "SELECT AVG(population) FROM states"

        try:
            self.conn.cursor.execute(query)
            result = self.conn.cursor.fetchone()
            average_population = result[0] if result else None
        except Exception as e:
            print(f"An error occurred: {e}")
            average_population = None
        finally:
            # Close cursor
            self.conn.cursor.close()
            # Close connection
            self.conn.conn.close()

        if average_population is not None:
            return {
                "message": "Average population calculated",
                "status": 200,
                "result": average_population
            }
        else:
            return {
                "message": "Error occurred while calculating average population",
                "status": 500,
                "result": None
            }

    def list_states_admitted_after_year(self, year):
        """List states admitted after a certain year, ordered by admission year ascending"""

        query = "SELECT * FROM states WHERE admission_year > %s ORDER BY admission_year ASC"

        try:
            self.conn.cursor.execute(query, (year,))
            results = self.conn.cursor.fetchall()
            states_list = []

            if results:
                # Assuming the columns are id, name, and admission_year
                for row in results:
                    state = {
                        'id': row[0],
                        'name': row[1],
                        'admission_year': row[2]
                    }
                    states_list.append(state)
        except Exception as e:
            print(f"An error occurred: {e}")
            states_list = []
        finally:
            # Close cursor
            self.conn.cursor.close()
            # Close connection
            self.conn.conn.close()

        if len(states_list) > 0:
            return {
                "message": "States listed",
                "status": 200,
                "result": states_list
            }
        else:
            return {
                "message": "No states found",
                "status": 404,
                "result": None
            }

    def count_states_by_population_range(self, lower_bound, upper_bound):
        """Count states based on population ranges"""

        query = "SELECT COUNT(*) FROM states WHERE population >= %s AND population <= %s"

        try:
            self.conn.cursor.execute(query, (lower_bound, upper_bound))
            result = self.conn.cursor.fetchone()
            count = result[0] if result else 0
        except Exception as e:
            print(f"An error occurred: {e}")
            count = 0
        finally:
            # Close cursor
            self.conn.cursor.close()
            # Close connection
            self.conn.conn.close()

        return {
            "message": "Count calculated",
            "status": 200,
            "result": count
        }

    def join_states_with_capitals(self):
        """Join states and capitals tables to display state names along with their capitals"""

        query = ("SELECT s.name AS state_name, c.capital AS capital_name FROM states s JOIN capitals c ON s.id = "
                 "c.state_id ORDER BY s.name ASC")

        try:
            self.conn.cursor.execute(query)
            results = self.conn.cursor.fetchall()
            state_capital_list = []

            if results:
                # Assuming the columns are state_name and capital_name
                for row in results:
                    state_capital = {
                        'state_name': row[0],
                        'capital_name': row[1]
                    }
                    state_capital_list.append(state_capital)
        except Exception as e:
            print(f"An error occurred: {e}")
            state_capital_list = []
        finally:
            # Close cursor
            self.conn.cursor.close()
            # Close connection
            self.conn.conn.close()

        if len(state_capital_list) > 0:
            return {
                "message": "States and capitals found",
                "status": 200,
                "result": state_capital_list
            }
        else:
            return {
                "message": "No states or capitals found",
                "status": 404,
                "result": None
            }
