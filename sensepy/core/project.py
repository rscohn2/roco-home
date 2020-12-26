# SPDX-FileCopyrightText: 2020 Robert Cohn
#
# SPDX-License-Identifier: MIT

import logging

import sensepy
import sensepy.core as rcore

logger = logging.getLogger(__name__)


class Project(sensepy.Object):
    """Representation of a project.

    A project contains devices that measure signals.

    """

    def __init__(self, project_name, project_dict, account):
        '''Construct a project from a dict'''

        self.account = account
        self.name = project_dict['name']
        self.guid = project_dict['guid']
        self.signal_by_name = {}
        for signal_name, signal_dict in project_dict['signals'].items():
            signal = rcore.Signal(signal_name, signal_dict, self)
            self.signal_by_name[signal_name] = signal
            signal.register_guid()
        self.device_by_name = {}
        for device_name, device_dict in project_dict['devices'].items():
            device = rcore.Device(device_name, device_dict, self)
            self.device_by_name[device_name] = device
            device.register()
