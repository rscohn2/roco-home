# SPDX-FileCopyrightText: 2020 Robert Cohn
#
# SPDX-License-Identifier: MIT

import logging
import os

import signalpy as sp
from signalpy import cli
from signalpy.cli.identity import make_guid, make_token

logger = logging.getLogger(__name__)


def add_account_parser(parent_subparser):
    parser = parent_subparser.add_parser('account', help='Account maintenance')
    subparsers = parser.add_subparsers(dest='cmd')
    subparsers.required = True
    create_parser = subparsers.add_parser('create', help='Create an account.')
    create_parser.set_defaults(func=create_account)
    create_parser.add_argument('account_name', help='Name of account')

    list_parser = subparsers.add_parser('list', help='List all accounts.')
    list_parser.set_defaults(func=list_accounts)


def add_parser(subparsers):
    parser = subparsers.add_parser('admin', help='Maintenance interface')
    subparsers = parser.add_subparsers(dest='cmd')
    subparsers.required = True
    reset_parser = subparsers.add_parser(
        'reset', help='Create empty database with old tables'
    )
    reset_parser.set_defaults(func=reset)
    add_account_parser(subparsers)


uri_env = 'SIGNALPY_DB_URI'


def get_db():
    if uri_env not in os.environ:
        logger.error(f'Set {uri_env}')
        exit(1)
    return sp.MongoDB(os.environ[uri_env])


def reset():
    response = input('Deleting everything! Type reset to confirm: ')
    if response != 'reset':
        print('aborting reset')
        exit(0)

    db = get_db()
    sp.AccountStore.create(db)
    sp.SignalEventsStore.create(db)
    logger.info('Reset database')


def create_account():
    db = get_db()
    account = sp.Account(make_guid(), cli.args.account_name, make_token())
    sp.AccountStore(db).put(account)
    print(f'Created account: {account}')


def list_accounts():
    db = get_db()
    for account in sp.AccountStore(db).query():
        print(f' {account}')
