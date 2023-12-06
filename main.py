import sqlite3
from application import Application


def init_db(db_cursor):
    db_cursor.execute('''CREATE TABLE IF NOT EXISTS assets(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TXT,
                    value REAL,
                    quantity REAL)''')


if __name__ == '__main__':
    with sqlite3.connect('balance.db') as database:
        cursor = database.cursor()
        init_db(cursor)
        main = Application()
        main.main()
