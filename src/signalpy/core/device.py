# SPDX-FileCopyrightText: 2020 Robert Cohn
#
# SPDX-License-Identifier: MIT

import logging

import signalpy as sp

logger = logging.getLogger(__name__)


class Device(sp.Object):

    _by_guid = {}
    """Lookup device by GUID."""

    _by_token = {}
    """Lookup device by GUID."""

    def __init__(self, name, project, guid=None, token=None):
        self.guid = guid if guid else sp.make_guid()
        self.token = token if token else sp.make_token()
        self.name = name
        self.project = project
        self._sensor_by_name = {}
        Device._by_guid[self.guid] = self
        Device._by_token[self.token] = self

    def by_guid(guid):
        return Device._by_guid[guid]

    def by_token(token):
        return Device._by_token[token]

    def sensor_by_name(self, name, type=None):
        if name not in self._sensor_by_name:
            self._sensor_by_name[name] = sp.sensor_factory(type, name, self)
        return self._sensor_by_name[name]

    def configure(self, info):
        for sensor_name, sensor_info in info['sensors'].items():
            sensor = self.sensor_by_name(sensor_name, sensor_info['type'])
            sensor.configure(sensor_info)
