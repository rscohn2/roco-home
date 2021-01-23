# SPDX-FileCopyrightText: 2020 Robert Cohn
#
# SPDX-License-Identifier: MIT

import logging
import secrets
import uuid

logger = logging.getLogger(__name__)


def add_parser(subparsers):
    parser = subparsers.add_parser('identity', help='Identity management')
    subparsers = parser.add_subparsers(dest='cmd')
    subparsers.required = True
    gen_token_parser = subparsers.add_parser(
        'gen-token', help='Generate a secret token'
    )
    gen_token_parser.set_defaults(func=gen_token)
    gen_guid_parser = subparsers.add_parser('gen-guid', help='Generate a guid')
    gen_guid_parser.set_defaults(func=gen_guid)


def make_token():
    return secrets.token_urlsafe()


def make_guid():
    return uuid.uuid1()


def gen_token():
    print('token:', make_token())


def gen_guid():
    print('guid:', make_guid())
