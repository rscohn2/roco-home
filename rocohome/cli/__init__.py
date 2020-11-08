import argparse
import logging
import sys

from rocohome.cli import db

args = None


def parse_args(cmd_args):
    parser = argparse.ArgumentParser(description='CLI for rocohome')
    parser.add_argument(
        '--verbose', action='store_true', help='display log information'
    )
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='do not perform actions that modify system state',
    )
    subparsers = parser.add_subparsers(dest='cmd')
    subparsers.required = True
    db.add_parser(subparsers)
    return parser.parse_args()


def setup():
    if args.verbose:
        logging.basicConfig(level=logging.INFO)


def main(cmd_args=sys.argv[1:]):
    global args

    args = parse_args(cmd_args)
    setup()
    args.func()
