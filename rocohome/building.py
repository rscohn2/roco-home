import logging

import rocohome as rh

logger = logging.getLogger(__name__)


class Building:
    """Representation of a building.

    A building contains devices.
    """

    def __init__(self, account, dict):
        '''Construct a building from a dict'''

        self.id = dict['id']
        self.account = account
        self.name = dict['name']
        self.devices = {}
        for name, device_dict in dict['devices'].items():
            device = rh.Device(name, self, device_dict)
            self.devices[name] = device
            device.register()

    def lookup_sensor(
        self,
    ):
        return
