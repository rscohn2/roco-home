import logging

from rocohome import db

logger = logging.getLogger(__name__)


def add_parser(subparsers):
    db_parser = subparsers.add_parser('db', help='Database maintenance')
    subparsers = db_parser.add_subparsers(dest='cmd')
    subparsers.required = True
    # create_parser = subparsers.add_parser('create', help='Create a database')
    # create_parser.set_defaults(func=create)
    up_parser = subparsers.add_parser('up', help='Start database')
    up_parser.set_defaults(func=up)
    up_parser.add_argument(
        '--jar-dir',
        default='.',
        help='Directory that contains DynamoDBLocal.jar',
    )
    down_parser = subparsers.add_parser('down', help='Shutdown database')
    down_parser.set_defaults(func=down)


def up():
    pid = db.local.up()
    with open('dynamo.pid', 'w') as fout:
        fout.write('%s\n' % pid)


def down():
    with open('dynamo.pid', 'r') as fin:
        pid = int(fin.read())
    db.local.down(pid)
