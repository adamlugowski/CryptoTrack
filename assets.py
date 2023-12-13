class Asset:
    def __init__(self, connection):
        self.connection = connection

    # I will try to make this function work on condition:
    # if asset in database: increase quantity and count value using weighted average
    def add_asset(self, name: str, value: float, quantity: float):
        sql = 'INSERT INTO assets VALUES (null, ?, ?, ?)'
        cursor = self.connection.cursor()
        cursor.execute(sql, (name, value, quantity))

    def show_balance(self, name: str):
        cursor = self.connection.cursor()
        return cursor.execute('SELECT * FROM assets')

    def remove_asset(self, name, quantity):
        cursor = self.connection.cursor()
        cursor.execute('DELETE FROM assets WHERE name=?', (name, ))
        self.connection.commit()


