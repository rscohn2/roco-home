# SPDX-FileCopyrightText: 2020 Robert Cohn
#
# SPDX-License-Identifier: MIT

import logging

import yaml

import rocohome.core as rcore

logger = logging.getLogger(__name__)


class Account:
    """Representation of an account.

    Account is modeled after github account where buildings are
    projects.

    """

    def __init__(self, account_name, account_dict):
        """Construct an account."""
        self.name = account_name
        self.guid = account_dict['guid']
        self.buildings = {}

    def load_building(self, file):
        """Load configuration data for a building."""
        try:
            logger.info('load building: %s' % file)
            with open(file, 'r') as stream:
                try:
                    building_dict = yaml.safe_load(stream)
                    building_name = building_dict['name']
                    logger.info(
                        'Loaded building %s: %s'
                        % (building_name, building_dict)
                    )
                    self.buildings[building_name] = rcore.Building(
                        building_name, building_dict, self
                    )
                    return self.buildings[building_name]
                except yaml.YAMLError as exc:
                    logger.error('parsing building file %s: %s' % (file, exc))
                    raise exc
        except OSError as exc:
            logger.error('opening building file: %s: %s' % (file, exc))
            raise exc
