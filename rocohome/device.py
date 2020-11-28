import logging

import rocohome as rh

logger = logging.getLogger(__name__)

registry = {}


class Device:
    """Representation of a device.

    A device is a network connected object that contains sensors.

    Attributes:
      name -- Name to use in UI
      sensors -- Dict where keys are sensor_id, value is a sensor
      id -- Unique ID that does not change. Usually a MAC.
      tokens -- Dict where keys are tokens used for authentication

    """

    def __init__(self, name, building, dict):
        self.name = name
        self.id = dict['id']
        self.building = building
        self.tokens = {}
        for token in dict['tokens']:
            self.tokens[token] = None
        self.sensors = {}
        for name, sensor in dict['sensors'].items():
            self.sensors[name] = rh.Sensor(name, self, sensor)

    def register(self):
        global registry
        for token in self.tokens:
            registry[token] = self
            logger.info('registered %s with token: %s' % (self.id, token))

    def lookup(token):
        return registry[token]

    def lookup_sensor(self, sensor_id):
        return self.sensors[sensor_id]
