# SPDX-FileCopyrightText: 2020 Robert Cohn
#
# SPDX-License-Identifier: MIT

import signalpy as sp


class Signal(sp.Object):

    by_guid = {}
    """Dictionary for mapping GUID to signals."""

    def __init__(self, signal_name, signal_dict, project):
        """Representation of a signal.

        Parameters
        ----------
        signal_name : str
        signal_dict : dict
        project : :class:`~signalpy.core.project.Project`

        """

        self.project = project
        self.name = signal_name
        self.guid = signal_dict['guid']

    def register_guid(self):
        """Register signal for lookup by GUID."""

        Signal.by_guid[self.guid] = self
