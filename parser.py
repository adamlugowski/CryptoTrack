import sys
import argparse


class Parser:
    def __init__(self):
        self.parser = argparse.ArgumentParser(
            prog="CryptoTrack",
            description="A simple and powerful program for tracking purchased tokens.",
            epilog="Author: Adam Ługowski")

        self.action_group = self.parser.add_mutually_exclusive_group(required=True)

        self.action_group.add_argument(
            '--add-asset',
            dest='action',
            action='store_const',
            const='add_asset',
            help='Adding token to balance sheet'
        )

        self.action_group.add_argument(
            '--show-balance',
            dest='action',
            action='store_const',
            const='show_balance',
            help='Showing balance of requested token'
        )

        self.action_group.add_argument(
            '--remove-asset',
            dest='action',
            action='store_const',
            const='remove_asset',
            help='Remove token from your balance sheet'
        )

        self.add_group = self.parser.add_argument_group('Adding, removing, listing assets')
        self.add_group.add_argument(
            '--name',
            type=str,
            help="Name of the token. Note that you should omit '$' sign",
            required='--add-asset' in sys.argv or '--show-balance' in sys.argv or '--remove-asset' in sys.argv
        )

        self.add_group.add_argument(
            '--value',
            type=float,
            help='Price for one token',
            required='--add-asset' in sys.argv
        )

        self.add_group.add_argument(
            '--quantity',
            type=float,
            help='Quantity of purchased tokens',
            required='--add-asset' in sys.argv or '--remove-asset' in sys.argv
        )

    def parse_args(self):
        return self.parser.parse_args()
