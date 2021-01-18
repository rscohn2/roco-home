# SPDX-FileCopyrightText: 2020 Robert Cohn
#
# SPDX-License-Identifier: MIT

import logging

import signalpy as sp

logger = logging.getLogger(__name__)


class Device(sp.Object):
    """Representation of a device.

    Attributes:
      name (str):
      guid (str):
      project (:class:`~signalpy.core.project.Project`):
      tokens (list):
        Token strings that authorize recording events for this device

    """

    by_guid = {}
    """Lookup device by GUID."""

    def __init__(self, device_name, device_dict, project):
        self.project = project
        self.name = device_name
        self.guid = device_dict['guid']
        self.tokens = device_dict['tokens']
        self.sensor_by_name = {}
        for sensor_name, sensor_dict in device_dict['sensors'].items():
            sensor = sp.Sensor(sensor_name, sensor_dict, self)
            self.sensor_by_name[sensor_name] = sensor

    def register(self):
        """Register device for lookup by GUID."""

        logger.info(f'Register device: {self}')
        Device.by_guid[self.guid] = self
