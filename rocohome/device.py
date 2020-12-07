# SPDX-FileCopyrightText: 2020 Robert Cohn
#
# SPDX-License-Identifier: MIT

import logging

import rocohome as rh

logger = logging.getLogger(__name__)


class Device:
    """Representation of a device."""

    by_token = {}
    by_guid = {}

    def __init__(self, device_name, device_dict, building):
        self.building = building
        self.name = device_name
        self.guid = device_dict['guid']
        self.tokens = {}
        for token in device_dict['tokens']:
            self.tokens[token] = None
        self.sensor_by_name = {}
        for sensor_name, sensor_dict in device_dict['sensors'].items():
            sensor = rh.Sensor(sensor_name, sensor_dict, self)
            self.sensor_by_name[sensor_name] = sensor

    def register_guid(self):
        Device.by_guid[self.guid] = self

    def register_tokens(self):
        global device_token_registry
        for token in self.tokens:
            Device.by_token[token] = self
