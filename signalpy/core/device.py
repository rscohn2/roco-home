# SPDX-FileCopyrightText: 2020 Robert Cohn
#
# SPDX-License-Identifier: MIT

import logging

import marshmallow as mm

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

    by_token = {}
    """Lookup device by token."""

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
        """Register device for lookup by token and guid."""

        logger.info('Register device: %s' % self)
        Device.by_guid[self.guid] = self
        for token in self.tokens:
            Device.by_token[token] = self

    class Field(mm.fields.Field):
        """Serialization/deserialization of a Device.

        """

        def _serialize(self, device, attr, obj, **kwargs):
            return device.guid
    
        def _deserialize(self, id, attr, data, **kwargs):
            logger.info(f'deserialize devicefield {data}')
            try:
                return Device.by_guid[id]
            except KeyError as error:
                raise ValidationError('Unknown device guid.') from error

        @mm.post_load
        def make_device(self, data, **kwargs):
            logger.info(f'data: {data}')
            return sp.Device(**data)
