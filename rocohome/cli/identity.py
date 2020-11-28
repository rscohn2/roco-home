import logging
import secrets

logger = logging.getLogger(__name__)


def add_parser(subparsers):
    parser = subparsers.add_parser('identity', help='Identity management')
    subparsers = parser.add_subparsers(dest='cmd')
    subparsers.required = True
    gen_parser = subparsers.add_parser(
        'gen-token', help='Generate an identity token'
    )
    gen_parser.set_defaults(func=gen_token)


def gen_token():
    print('token:', secrets.token_urlsafe())
