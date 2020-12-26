# SPDX-FileCopyrightText: 2020 Robert Cohn
#
# SPDX-License-Identifier: MIT

import logging

logger = logging.getLogger(__name__)


def add_parser(subparsers):
    parser = subparsers.add_parser('log-server', help='Log server')
    subparsers = parser.add_subparsers(dest='cmd')
    subparsers.required = True
    sync_parser = subparsers.add_parser(
        'sync', help='Sync logs to local machine'
    )
    sync_parser.set_defaults(func=sync)


def sync():
    pass
