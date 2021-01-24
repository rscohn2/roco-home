# SPDX-FileCopyrightText: 2020 Robert Cohn
#
# SPDX-License-Identifier: MIT

import logging

import signalpy as sp

logger = logging.getLogger(__name__)


class Project(sp.Object):

    _by_guid = {}

    def __init__(self, guid, name, account):
        """Container for project info."""

        self.guid = guid
        self.name = name
        self.account = account
        self.signal_by_name = {}
        sp.Project._by_guid[guid] = self
        
    def by_guid(guid):
        return Project._by_guid[guid]
    
    def configure(self, config):
        """Configure a project with devices and signals."""

        for signal_name, signal_dict in project_dict['signals'].items():
            signal = sp.Signal(signal_name, signal_dict, self)
            self.signal_by_name[signal_name] = signal
            signal.register_guid()
        self.device_by_name = {}
        for device_name, device_dict in project_dict['devices'].items():
            device = sp.Device(device_name, device_dict, self)
            self.device_by_name[device_name] = device
            device.register()
