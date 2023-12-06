from parser import Parser


class Application:
    def __init__(self):
        parser = Parser()
        self.arguments = parser.parse_args()

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

    def show_balance(self, name):
        print('Showing quantity and average asset value')

    def remove_asset(self, name, quantity):
        print('Reducing the amount of assets')
