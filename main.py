import sqlite3
from application import Application
from assets import Asset


def init_db(db_cursor):
    db_cursor.execute('''CREATE TABLE IF NOT EXISTS assets(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    value REAL,
                    quantity REAL,
                    money_invested REAL)''')


if __name__ == '__main__':
    with sqlite3.connect('balance.db') as database:
        cursor = database.cursor()
        init_db(cursor)
        asset = Asset(database)
        main = Application(asset)
        main.main()
