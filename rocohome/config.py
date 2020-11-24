import logging
import sys

import yaml

logger = logging.getLogger(__name__)

config = None


def load(file='rocohome.yaml'):
    global config
    try:
        logger.info('Loading config: %s' % file)
        with open(file, 'r') as stream:
            try:
                config = yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                logger.error(exc)
    except OSError:
        logger.error('Cannot open config file: %s' % file)
        sys.exit(1)
