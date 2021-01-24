# SPDX-FileCopyrightText: 2020 Robert Cohn
#
# SPDX-License-Identifier: MIT

import signalpy as sp


class Signal(sp.Object):

    _by_guid = {}

    def __init__(self, name, project, guid=None):
        """Representation of a signal.

        Parameters
        ----------
        signal_guid : str
        signal_name : str
        project : :class:`~signalpy.core.project.Project`

        """

        self.project = project
        self.name = name
        self.guid = guid if guid else sp.make_guid()
        Signal._by_guid[guid] = self

    def by_guid(guid):
        """Returns signal associated with GUID."""
        return Signal._by_guid(guid)
