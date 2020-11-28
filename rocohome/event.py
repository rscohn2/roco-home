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

    def decode(e):
        """Returns a decoded event."""

        if e['version'] not in supported_versions:
            raise UnsupportedEventVersion(e['version'])
        if e['event'] == 'observation':
            return Observation(e)
        else:
            raise UnsupportedEvent(e['event'])


class Observation(Event):
    """Representation of an sensor observation."""

    def __init__(self, e):
        """Decodes an observation."""
        self.sensor = rh.Device.lookup(e['token']).lookup_sensor(
            e['sensor_id']
        )
        self.val = int(e['val'])
        super().__init__(e)

    def encode(self):
        """Encode an observation for insertion into the db."""

        return {
            'time': self.time,
            'account_id': self.sensor.device.building.account.id,
            'building_id': self.sensor.device.building.id,
            'observed_id': self.sensor.observed_id,
            'val': self.val,
        }
