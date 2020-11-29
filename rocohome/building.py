import logging

import rocohome as rh

logger = logging.getLogger(__name__)


class Building:
    """Representation of a building.

    A building contains devices that measure signals.

    """

    def __init__(self, building_name, building_dict, account):
        '''Construct a building from a dict'''

        self.account = account
        self.name = building_dict['name']
        self.guid = building_dict['guid']
        self.signals = {}
        for signal_name, signal_dict in building_dict['signals'].items():
            self.signals[signal_name] = rh.Signal(
                signal_name, signal_dict, self
            )
        self.devices = {}
        for device_name, device_dict in building_dict['devices'].items():
            self.devices[device_name] = rh.Device(
                device_name, device_dict, self
            )
            self.devices[device_name].register_tokens()

    def lookup_signal(self, signal_name):
        return self.signals[signal_name]
