# SPDX-FileCopyrightText: 2020 Robert Cohn
#
# SPDX-License-Identifier: MIT

import logging

import zignalz as zz

logger = logging.getLogger(__name__)


class Project(zz.Object):

    def __init__(self, name, account, guid=None):
        """Container for project info."""

        self.guid = guid if guid else zz.make_guid()
        self.name = name
        self.account = account
        self._signal_by_name = {}
        self._device_by_name = {}
        self.conf = {}

    def _get_overrides(self, name, overrides):
        """Allow overrides for debugging."""

        guid = None
        token = None
        try:
            logger.info(f'override check {name}')
            guid = overrides[name]['guid']
            logger.info(f'override {name} guid: {guid}')
        except KeyError:
            pass
        try:
            token = overrides[name]['token']
            logger.info(f'override {name} token: {token}')
        except KeyError:
            pass
        return (guid, token)

    def device_by_name(self, name, overrides):
        if name not in self._device_by_name:
            (guid, token) = self._get_overrides(name, overrides)
            device = zz.Device(name=name, project=self, guid=guid, token=token)
            self._device_by_name[name] = device
            self.account.stores.device.put(device)
        return self._device_by_name[name]

    def signal_by_name(self, name):
        if name not in self._signal_by_name:
            signal = zz.Signal(name=name, project=self)
            self._signal_by_name[name] = signal
            self.account.stores.signal.put(signal)
        return self._signal_by_name[name]

    def configure(self, info, overrides=None):
        """Configure a project with devices and signals."""

        self.name = info['name']
        for device_name, device_info in info['devices'].items():
            device = self.device_by_name(device_name, overrides)
            device.configure(device_info)
