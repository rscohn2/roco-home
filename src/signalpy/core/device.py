# SPDX-FileCopyrightText: 2020 Robert Cohn
#
# SPDX-License-Identifier: MIT

import logging

import signalpy as sp

logger = logging.getLogger(__name__)


class Device(sp.Object):

    _by_guid = {}
    """Lookup device by GUID."""

    def __init__(self, guid, name, project):
        self.guid = guid
        self.name = name
        self.project = project
        Device._by_guid[guid] = self

    def by_guid(guid):
        return Device._by_guid[guid]
