class Asset:
    def __init__(self, name: int):
        self.name = name
        self.balance = {}

    def add_balance(self, money: float, value: float, fee=0.001):
        money -= money * fee
        quantity = money / value
        self.balance[self.name] = quantity
        return self.balance


asset = Asset('XXX')
asset.add_balance(100, 0.2)
print(asset.balance)
