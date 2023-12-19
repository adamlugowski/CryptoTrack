class Asset:
    def __init__(self, connection):
        self.connection = connection

    # I will try to make this function work on condition:
    # if asset in database: increase quantity and count value using weighted average
    def add_asset(self, name: str, value: float, quantity: float):
        money_invested = quantity * value
        cursor = self.connection.cursor()
        cursor.execute('INSERT INTO assets VALUES (null, ?, ?, ?, ?)', (name, value, quantity, money_invested))

    def show_balance(self, name: str):
        cursor = self.connection.cursor()
        cursor.execute('SELECT SUM(quantity) FROM assets WHERE name=?', (name, ))
        result = cursor.fetchone()
        print(result[0])

    def remove_asset(self, name):
        cursor = self.connection.cursor()
        cursor.execute('DELETE FROM assets WHERE name=?', (name, ))
        self.connection.commit()

    # funkcja do zliczania średniej zakupowej
    def asset_average(self, name):
        cursor = self.connection.cursor()
        cursor.execute('SELECT SUM(money_invested) / SUM(quantity) FROM assets WHERE name=?', (name, ))
        result = cursor.fetchone()
        print(result[0])

