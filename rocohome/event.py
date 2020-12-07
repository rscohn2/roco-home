# SPDX-FileCopyrightText: 2020 Robert Cohn
#
# SPDX-License-Identifier: MIT

"""Events occur on a device and are recorded in the database.

"""

import logging

import rocohome as rh

logger = logging.getLogger(__name__)

supported_versions = set([1])


class UnsupportedEventVersionError(Exception):
    """Event uses unsupported version number."""

    def __init__(self, version):
        self.version = version


class UnsupportedEventError(Exception):
    """Event uses unsupported type."""

    def __init__(self, event):
        self.event = event


def _device_decode_event(e):
    """Returns an Event from a device-generated dict."""

    if e['version'] not in supported_versions:
        raise UnsupportedEventVersionError(e['version'])
    if e['event'] == 'sensor':
        return SignalEvent(from_device=e)
    else:
        raise UnsupportedEventError(e['event'])


def _store_decode_event(e):
    """Returns an Event from a db generated dict"""

    if e['version'] not in supported_versions:
        raise UnsupportedEventVersionError(e['version'])
    if e['event'] == 'sensor':
        return SignalEvent(from_store=e)
    else:
        raise UnsupportedEventError(e['event'])


class Event:
    """Representation of an event.

    Attributes:
       time
         UTC timestamp
       raw
         Incoming representation
    """

    def __init__(self, dict):
        self.time = int(dict['time'])
        self.raw = dict


class SignalEvent(Event):
    """Representation of an signal event.

    Attributes:
       time
         UTC timestamp
       signal
         :class:`~rocohome.signal.Signal`
       val
         recorded value
       raw
         Incoming representation
    """

    def __init__(self, from_device=None, from_store=None):
        if from_device:
            self.device = rh.Device.by_token[from_device['token']]
            self.signal = self.device.sensor_by_name[
                from_device['sensor_id']
            ].signal
            self.val = int(from_device['val'])
            # Extract common arguments
            super().__init__(from_device)
        elif from_store:
            self.device = rh.Device.by_guid[from_store['device_guid']]
            self.signal = rh.Signal.by_guid[from_store['signal_guid']]
            self.val = from_store['val']
            # Extract common arguments
            super().__init__(from_store)
        else:
            assert False, 'Supply from_store or to_store'

    def to_store(self):
        """Encode an sensor event for insertion into the event store."""
        return {
            'time': self.time,
            'device_guid': self.device.guid,
            'signal_guid': self.signal.guid,
            'val': self.val,
        }
