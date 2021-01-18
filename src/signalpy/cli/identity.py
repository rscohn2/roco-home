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
    gen_uuid_parser = subparsers.add_parser('gen-uuid', help='Generate a uuid')
    gen_uuid_parser.set_defaults(func=gen_uuid)


def gen_token():
    print('token:', secrets.token_urlsafe())


def gen_uuid():
    print('uuid:', uuid.uuid1())
