# SPDX-FileCopyrightText: 2020 Robert Cohn
#
# SPDX-License-Identifier: MIT


class Signal:
    """Representation of a signal."""

    by_guid = {}

    def __init__(self, signal_name, signal_dict, building):
        self.building = building
        self.name = signal_name
        self.guid = signal_dict['guid']

    def register_guid(self):
        Signal.by_guid[self.guid] = self
