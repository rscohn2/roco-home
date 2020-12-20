# SPDX-FileCopyrightText: 2020 Robert Cohn
#
# SPDX-License-Identifier: MIT

import rocohome


class Signal(rocohome.Object):
    """Representation of a signal.

    Attributes:
      name (str):
      building (:class:`~rocohome.core.building.Building`):
      guid (str):

    """

    by_guid = {}
    """Dictionary for mapping guid to signals."""

    def __init__(self, signal_name, signal_dict, building):
        self.building = building
        self.name = signal_name
        self.guid = signal_dict['guid']

    def register_guid(self):
        """Register signal for lookup by guid."""

        Signal.by_guid[self.guid] = self
