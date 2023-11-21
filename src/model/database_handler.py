import pickle
from abc import ABC
from pathlib import Path
from sqlite3 import connect, Error, Binary
from colorama import Fore, Style


class DatabaseConnectionFactory(ABC):
    """
    Database Abstract Factory
    """

    def create_connection(self):
        pass

    def create_cursor(self):
        pass


class IDatabaseHandler(ABC):
    def save(self, game):
        pass

    def load(self):
        pass


# William
class DatabaseHandler:
    """
    Main object to handle database connections e.g. SQLite, MySQL
    """

    def __init__(self):
        self.root_dir = Path(__file__).parent.parent

    # William
    def connect_sqlite(self):
        """
        Make a new connection to SQLite database
        :return:
        """
        connection = None
        try:
            connection = connect(str(self.root_dir / "saves") + "\\" + "game_save.db")
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

    # William
    def save_to_sqlite(self, game):
        """
        Save current game state to database file
        :param game:
        :return:
        """
        con = self.connect_sqlite()
        cursor = con.cursor()
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

    # William
    def load_from_sqlite(self):
        """
        Load current game state from database file
        :return:
        """
        data = None
        con = self.connect_sqlite()
        cursor = con.cursor()

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
