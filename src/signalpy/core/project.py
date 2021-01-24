# SPDX-FileCopyrightText: 2020 Robert Cohn
#
# SPDX-License-Identifier: MIT

import logging

import signalpy as sp

logger = logging.getLogger(__name__)


class Project(sp.Object):

    _by_guid = {}

    def __init__(self, name, account, guid=None):
        """Container for project info."""

        self.guid = guid if guid else sp.make_guid()
        self.name = name
        self.account = account
        self._signal_by_name = {}
        self._device_by_name = {}
        sp.Project._by_guid[guid] = self

    def by_guid(guid):
        return Project._by_guid[guid]

    def device_by_name(self, name):
        if name not in self._device_by_name:
            device = sp.Device(name=name, project=self)
            self._device_by_name[name] = device
            self.stores.device.put(device)
        return self._device_by_name[name]

    def signal_by_name(self, name):
        if name not in self._signal_by_name:
            signal = sp.Signal(name=name, project=self)
            self._signal_by_name[name] = signal
            self.stores.signal.put(signal)
        return self._signal_by_name[name]

    def configure(self, stores, info):
        """Configure a project with devices and signals."""

        self.name = info['name']
        self.stores = stores
        for device_name, device_info in info['devices'].items():
            device = self.device_by_name(device_name)
            device.configure(device_info)
