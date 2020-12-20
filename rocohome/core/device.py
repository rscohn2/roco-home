# SPDX-FileCopyrightText: 2020 Robert Cohn
#
# SPDX-License-Identifier: MIT

import logging

import rocohome.core as rcore

logger = logging.getLogger(__name__)


class Device:
    """Representation of a device.

    Attributes:
      name (str):
      guid (str):
      building (:class:`~rocohome.core.building.Building`):
      tokens (list):
        Token strings that authorize recording events for this device

    """

    by_token = {}
    """Lookup device by token."""

    by_guid = {}
    """Lookup device by GUID."""

    def __init__(self, device_name, device_dict, building):
        self.building = building
        self.name = device_name
        self.guid = device_dict['guid']
        self.tokens = device_dict['tokens']
        self.sensor_by_name = {}
        for sensor_name, sensor_dict in device_dict['sensors'].items():
            sensor = rcore.Sensor(sensor_name, sensor_dict, self)
            self.sensor_by_name[sensor_name] = sensor

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)

    def register(self):
        """Register device for lookup by token and guid."""

        logger.info('Register device: %s' % self)
        Device.by_guid[self.guid] = self
        for token in self.tokens:
            Device.by_token[token] = self
