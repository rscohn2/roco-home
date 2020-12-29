# SPDX-FileCopyrightText: 2020 Robert Cohn
#
# SPDX-License-Identifier: MIT

import marshmallow as mm

import signalpy as sp


class Signal(sp.Object):
    """Representation of a signal.

    Attributes:
      name (str):
      project (:class:`~signalpy.core.project.Project`):
      guid (str):

    """

    by_guid = {}
    """Dictionary for mapping guid to signals."""

    def __init__(self, signal_name, signal_dict, project):
        self.project = project
        self.name = signal_name
        self.guid = signal_dict['guid']

    def register_guid(self):
        """Register signal for lookup by guid."""

        Signal.by_guid[self.guid] = self

    class DeviceField(mm.fields.Field):
        """Serialization/deserialization of a Signal.

        """

        def _serialize(self, signal, attr, obj, **kwargs):
            assert False
    
        def _deserialize(self, sensor_id, attr, data, **kwargs):
            device = sp.Device.by_guid[data['device_guid']]
            return device.sensor_by_name[sensor_id].signal

    class StoreField(mm.fields.Field):
        """Serialization/deserialization of a Signal.

        """

        def _serialize(self, signal, attr, obj, **kwargs):
            return signal.guid
    
        def _deserialize(self, guid, attr, data, **kwargs):
            try:
                return sp.Signal.by_guid[guid]
            except KeyError as error:
                raise ValidationError('Unknown signal guid.') from error

