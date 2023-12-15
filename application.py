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
        print('Adding assets', name, value, quantity)
        self.asset.add_asset(name, value, quantity)

    def show_balance(self, name):
        print('Showing balance of', name)
        self.asset.show_balance(name)

    def remove_asset(self, name, quantity):
        print(f'Reducing the amount of {name} by {quantity}')
        self.asset.remove_asset(name, quantity)
