import pickle
from pathlib import Path
from sqlite3 import connect, Error, Binary
from colorama import Fore, Style


# William
class DatabaseHandler:
    def __init__(self):
        self.root_dir = Path(__file__).parent.parent

    # William
    def connect_sqlite(self):
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
        con = self.connect_sqlite()
        cursor = con.cursor()
        data = pickle.dumps(game, pickle.HIGHEST_PROTOCOL)
        cursor.execute("insert into table (game) values (:game)", Binary(data))
        con.commit()
        con.close()

    # William
    def load_from_sqlite(self):
        con = self.connect_sqlite()
        cursor = con.cursor()
        cursor.execute("select data from table limit 1")
        data = None

        for row in cursor:
            data = pickle.loads(str(row['data']))

        con.close()
        return data
