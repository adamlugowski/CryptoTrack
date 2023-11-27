class Asset:
    def __init__(self, name: int):
        self.name = name
        self.balance = {}

    def add_balance(self, money: float, price: float, fee=0.001):
        money -= money * fee
        quantity = money / price
        self.balance[self.name] = quantity
        return self.balance


asset = Asset('XXX')
asset.add_balance(100, 0.2)
print(asset.balance)



# mam $
# za $ kupuje x
# x ma cenę
# mam x w ilości y
#
# balance pokazuje x w ilości y
#


