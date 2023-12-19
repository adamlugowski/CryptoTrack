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
                self.arguments.name)
            case 'asset_average':
                self.asset_average(self.arguments.name)

    def add_asset(self, name, value, quantity):
        print(f'Adding asset: {name}, {value}, {quantity}.')
        self.asset.add_asset(name, value, quantity)

    def show_balance(self, name):
        print(f'Showing quantity of {name}.')
        self.asset.show_balance(name)

    def remove_asset(self, name):
        print(f'Removing asset {name} from your balance sheet.')
        self.asset.remove_asset(name)

    def asset_average(self, name):
        print(f'Purchasing average of: {name}.')
        self.asset.asset_average(name)
