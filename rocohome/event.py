# SPDX-FileCopyrightText: 2020 Robert Cohn
#
# SPDX-License-Identifier: MIT

import logging

import rocohome as rh

logger = logging.getLogger(__name__)

supported_versions = set([1])


class UnsupportedEventVersion(Exception):
    def __init__(self, version):
        self.version = version


class UnsupportedEvent(Exception):
    def __init__(self, event):
        self.event = event


def device_decode_event(e):
    """Returns an Event from a device-generated dict"""

    if e['version'] not in supported_versions:
        raise UnsupportedEventVersion(e['version'])
    if e['event'] == 'sensor':
        return SensorEvent(e)
    else:
        raise UnsupportedEvent(e['event'])


def db_decode_event(e):
    """Returns an Event from a db generated dict"""

    if e['version'] not in supported_versions:
        raise UnsupportedEventVersion(e['version'])
    if e['event'] == 'sensor':
        return SensorEvent(e)
    else:
        raise UnsupportedEvent(e['event'])


class Event:
    """Representation of an event.

    Attributes:
       time -- UTC timestamp
       raw -- Incoming representation
    """

    def __init__(self, e):
        """Decodes attributes common to all events."""

        self.time = int(e['time'])
        self.raw = e


class SensorEvent(Event):
    """Representation of an sensor event."""

    def __init__(self, e):
        """Decodes a sensor event."""
        self.sensor = rh.Device.lookup_device(e['token']).lookup_sensor(
            e['sensor_id']
        )
        self.val = int(e['val'])
        super().__init__(e)

    def encode(self):
        """Encode an sensor event for insertion into the db."""

        return {
            'time': self.time,
            'device_guid': self.sensor.device.guid,
            'signal_guid': self.sensor.signal.guid,
            'val': self.val,
        }
