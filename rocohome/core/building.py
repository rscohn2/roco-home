# SPDX-FileCopyrightText: 2020 Robert Cohn
#
# SPDX-License-Identifier: MIT

import logging

import rocohome
import rocohome.core as rcore

logger = logging.getLogger(__name__)


class Building(rocohome.Object):
    """Representation of a building.

    A building contains devices that measure signals.

    """

    def __init__(self, building_name, building_dict, account):
        '''Construct a building from a dict'''

        self.account = account
        self.name = building_dict['name']
        self.guid = building_dict['guid']
        self.signal_by_name = {}
        for signal_name, signal_dict in building_dict['signals'].items():
            signal = rcore.Signal(signal_name, signal_dict, self)
            self.signal_by_name[signal_name] = signal
            signal.register_guid()
        self.device_by_name = {}
        for device_name, device_dict in building_dict['devices'].items():
            device = rcore.Device(device_name, device_dict, self)
            self.device_by_name[device_name] = device
            device.register()
