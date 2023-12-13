from parser import Parser
from assets import Asset


class Application:
    def __init__(self, asset: Asset):
        parser = Parser()
        self.arguments = parser.parse_args()
        self.asset = asset

    def main(self):
        match self.arguments.action:
            case 'add_asset': self.add_asset(
                self.arguments.name,
                self.arguments.value,
                self.arguments.quantity)
            case 'show_balance': self.show_balance(
                self.arguments.name)
            case 'remove_asset': self.remove_asset(
                self.arguments.name,
                self.arguments.quantity)

    def add_asset(self, name, value, quantity):
        print('Adding assets')
        self.asset.add_asset(name, value, quantity)

    def show_balance(self, name):
        for asset in self.asset.show_balance(name):
            print(asset)

    def remove_asset(self, name, quantity):
        print('Reducing the amount of assets')
        self.asset.remove_asset(name, quantity)
