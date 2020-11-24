import logging

from rocohome import cli, config

logger = logging.getLogger(__name__)


def add_parser(subparsers):
    parser = subparsers.add_parser('config', help='Manage configration')
    subparsers = parser.add_subparsers(dest='cmd')
    subparsers.required = True
    load_parser = subparsers.add_parser(
        'load', help='Load a configuration from a yaml file'
    )
    load_parser.set_defaults(func=load)
    load_parser.add_argument(
        'config_file',
        default='rocohome.yaml',
        help='Yaml file with configuration',
    )


def load():
    config.load(cli.args.config_file)
