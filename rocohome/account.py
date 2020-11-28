import logging

import yaml

import rocohome as rh

logger = logging.getLogger(__name__)


class Account:
    """Representation of an account.

    Account is modeled after github account where buildings are
    projects.

    """

    def __init__(self, name):
        self.id = name
        self.buildings = {}

    def load_building(self, file):
        try:
            logger.info('load building: %s' % file)
            with open(file, 'r') as stream:
                try:
                    building_dict = yaml.safe_load(stream)
                    logger.info('Loaded building: %s' % building_dict)
                    building = rh.Building(self, building_dict)
                    self.buildings[building.name] = building
                except yaml.YAMLError as exc:
                    logger.error('parsing building file %s: %s' % (file, exc))
                    raise exc
        except OSError as exc:
            logger.error('opening building file: %s: %s' % (file, exc))
            raise exc
        return building
