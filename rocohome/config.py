import logging
import sys

import yaml

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
