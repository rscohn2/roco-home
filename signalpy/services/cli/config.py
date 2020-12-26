# SPDX-FileCopyrightText: 2020 Robert Cohn
#
# SPDX-License-Identifier: MIT

import logging
import sys

import yaml

from signalpy.services import cli

logger = logging.getLogger(__name__)


class Config:
    def __init__(self):
        self.data = None

    def sensor_name(self, device_id, sensor_id):
        return self.data['devices'][device_id]['sensors'][sensor_id]

    def set(self, file):
        try:
            logger.info('set config: %s' % file)
            with open(file, 'r') as stream:
                try:
                    self.data = yaml.safe_load(stream)
                    logger.info('Loaded config: %s' % self.data)
                except yaml.YAMLError as exc:
                    logger.error(exc)
        except OSError:
            logger.error('Cannot open config file: %s' % file)
            sys.exit(1)


config = Config()


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
        default='signalpy.yaml',
        help='Yaml file with configuration',
    )


def load():
    config.load(cli.args.config_file)
