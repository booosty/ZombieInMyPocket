import pickle
from abc import ABC
from sqlite3 import connect, Error, Binary
from colorama import Fore, Style


class DatabaseConnectionFactory(ABC):
    """
    Database Abstract Factory
    """

    def create_connection(self, path):
        pass

    def create_cursor(self, db_connection):
        pass


class IDatabaseHandler(ABC):
    """
    DatabaseHandler Interface
    """

    def save(self, game):
        pass

    def load(self):
        pass


class SQLiteConnectionFactory(DatabaseConnectionFactory):
    """
    Concrete Factory for SQLite
    """

    def create_connection(self, path):
        connection = None
        try:
            connection = connect(path)
        except Error as err:
            print(
                Fore.RED
                + f"SQLite Error: {err}"
                + Style.RESET_ALL
            )
        except Exception as e:
            print(e)
        finally:
            return connection

    def create_cursor(self, db_connection):
        return db_connection.cursor()


class SQLiteHandler(IDatabaseHandler):
    """
    Concrete Product - SQLite
    """

    def __init__(self, connection_factory):
        self.connection_factory = connection_factory

    def save(self, game):
        con = self.connection_factory.create_connection("saves/game_save.db")
        cursor = self.connection_factory.create_cursor(con)
        data = pickle.dumps(game, pickle.HIGHEST_PROTOCOL)

        try:
            cursor.execute("""DROP TABLE IF EXISTS game""")
            cursor.execute("""CREATE TABLE game(id, data)""")
            cursor.execute("""INSERT INTO game VALUES (?, ?)""", (1, Binary(data)))
        except Error as err:
            print(f'Sql error: {" ".join(err.args)}')
            print(f'Exception class is: {err.__class__}')
        finally:
            con.commit()
            con.close()

    def load(self):
        data = None
        con = self.connection_factory.create_connection("saves/game_save.db")
        cursor = self.connection_factory.create_cursor(con)

        try:
            cursor.execute("SELECT data FROM game")
            rows = cursor.fetchall()

            for r in rows[0]:
                data = pickle.loads(r)

        except Error as err:
            print(f'Sql error: {" ".join(err.args)}')
            print(f'Exception class is: {err.__class__}')
        finally:
            con.close()
            return data

