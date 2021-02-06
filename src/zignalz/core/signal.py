# SPDX-FileCopyrightText: 2020 Robert Cohn
#
# SPDX-License-Identifier: MIT

import zignalz as zz


class Signal(zz.Object):

    _by_guid = {}

    def __init__(self, name, project, guid=None):
        """Representation of a signal.

        Parameters
        ----------
        signal_guid : str
        signal_name : str
        project : :class:`~zignalz.core.project.Project`

        """

        self.project = project
        self.name = name
        self.guid = guid if guid else zz.make_guid()
        Signal._by_guid[self.guid] = self

    def by_guid(guid):
        """Returns signal associated with GUID."""
        return Signal._by_guid[guid]
