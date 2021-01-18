# SPDX-FileCopyrightText: 2020 Robert Cohn
#
# SPDX-License-Identifier: MIT

import argparse
import logging
import sys

from signalpy.cli import config, db, identity

args = None


def parse_args(cmd_args):
    parser = argparse.ArgumentParser(description='CLI for signalpy')
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
    config.add_parser(subparsers)
    identity.add_parser(subparsers)
    return parser.parse_args()


def setup():
    if args.verbose:
        logging.basicConfig(level=logging.INFO)
    else:
        logging.basicConfig(level=logging.ERROR)


def main(cmd_args=sys.argv[1:]):
    global args

    args = parse_args(cmd_args)
    setup()
    args.func()
