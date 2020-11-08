import logging
import os
import signal

from rocohome.util import background, shell

logger = logging.getLogger(__name__)


def add_parser(subparsers):
    db_parser = subparsers.add_parser('db', help='Database maintenance')
    subparsers = db_parser.add_subparsers(dest='cmd')
    subparsers.required = True
    create_parser = subparsers.add_parser('create', help='Create a database')
    create_parser.set_defaults(func=create)
    up_parser = subparsers.add_parser('up', help='Start database')
    up_parser.set_defaults(func=up)
    down_parser = subparsers.add_parser('down', help='Shutdown database')
    down_parser.set_defaults(func=down)


def create():
    logger.info('Creating a database')
    shell('ls')


def up():
    instance = background(
        (
            'java -Djava.library.path=./DynamoDBLocal_lib'
            ' -jar DynamoDBLocal.jar -sharedDb'
        )
    )
    logger.info('Started %s' % instance.pid)
    with open('dynamo.pid', 'w') as fout:
        fout.write('%s\n' % instance.pid)


def down():
    with open('dynamo.pid', 'r') as fin:
        pid = int(fin.read())
    logger.info('Killing %d' % pid)
    os.kill(pid, signal.SIGKILL)
