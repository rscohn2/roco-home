import argparse
import sys

from rocohome.cli import db


def parse_args(cmd_args):
    parser = argparse.ArgumentParser(description='CLI for rocohome')
    parser.add_argument(
        '--verbose', action='store_true', help='display log information'
    )
    subparsers = parser.add_subparsers()
    db.add_parser(subparsers)
    return parser.parse_args()


def main(cmd_args=sys.argv[1:]):
    parse_args(cmd_args)
