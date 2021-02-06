# SPDX-FileCopyrightText: 2020 Robert Cohn
#
# SPDX-License-Identifier: MIT

import logging
import os

import zignalz as zz
from zignalz import cli

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


def add_project_parser(parent_subparser):
    parser = parent_subparser.add_parser('project', help='Project maintenance')
    subparsers = parser.add_subparsers(dest='cmd')
    subparsers.required = True
    create_parser = subparsers.add_parser('create', help='Create a project.')
    create_parser.set_defaults(func=create_project)
    create_parser.add_argument(
        'account_name', help='Name of account that owns project.'
    )
    create_parser.add_argument(
        'project_config', help='Project configuration file.'
    )

    update_parser = subparsers.add_parser('update', help='Update a project.')
    update_parser.set_defaults(func=update_project)
    update_parser.add_argument(
        'account_name', help='Name of account that owns project.'
    )
    update_parser.add_argument(
        'project_config', help='Project configuration file.'
    )

    list_parser = subparsers.add_parser('list', help='List all projects.')
    list_parser.set_defaults(func=list_projects)


def add_parser(subparsers):
    parser = subparsers.add_parser('admin', help='Maintenance interface')
    subparsers = parser.add_subparsers(dest='cmd')
    subparsers.required = True
    reset_parser = subparsers.add_parser(
        'reset', help='Create empty database with old tables'
    )
    reset_parser.set_defaults(func=reset)
    add_account_parser(subparsers)


uri_env = 'ZIGNALZ_DB_URI'


def get_db():
    if uri_env not in os.environ:
        logger.error(f'Set {uri_env}')
        exit(1)
    return zz.MongoDB(os.environ[uri_env])


def reset():
    response = input('Deleting everything! Type reset to confirm: ')
    if response != 'reset':
        print('aborting reset')
        exit(0)

    db = get_db()
    zz.AccountStore.create(db)
    zz.SignalEventsStore.create(db)
    logger.info('Reset database')


def create_account():
    db = get_db()
    account = zz.Account(name=cli.args.account_name)
    zz.AccountStore(db).put(account)
    print(f'Created account: {account}')


def list_accounts():
    db = get_db()
    for account in zz.AccountStore(db).query():
        print(f' {account}')


def create_project():
    assert False


def update_project():
    assert False


def list_projects():
    db = get_db()
    for project in zz.ProjectStore(db).query():
        print(f' {project}')


def create_device():
    db = get_db()
    device = zz.Device(name=cli.args.device_name)
    zz.DeviceStore(db).put(device)
    print(f'Created device: {device}')


def update_device():
    assert False


def list_devices():
    db = get_db()
    for device in zz.DeviceStore(db).query():
        print(f' {device}')
