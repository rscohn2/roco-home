import logging

import rocohome as rh

logger = logging.getLogger(__name__)

device_token_registry = {}


class Device:
    """Representation of a device."""

    def __init__(self, device_name, device_dict, building):
        self.building = building
        self.name = device_name
        self.guid = device_dict['guid']
        self.tokens = {}
        for token in device_dict['tokens']:
            self.tokens[token] = None
        self.sensors = {}
        for sensor_name, sensor_dict in device_dict['sensors'].items():
            self.sensors[sensor_name] = rh.Sensor(
                sensor_name, sensor_dict, self
            )

    def register_tokens(self):
        global device_token_registry
        for token in self.tokens:
            device_token_registry[token] = self

    def lookup_device(token):
        return device_token_registry[token]

    def lookup_sensor(self, sensor_name):
        return self.sensors[sensor_name]
