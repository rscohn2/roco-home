# SPDX-FileCopyrightText: 2020 Robert Cohn
#
# SPDX-License-Identifier: MIT

import zignalz as zz


class Signal(zz.Object):

    _by_guid = {}

    def __init__(self, name, project, guid):
        """Representation of a signal.

        Parameters
        ----------
        signal_guid : str
        signal_name : str
        project : :class:`~zignalz.core.project.Project`

        """

        self.project = project
        self.name = name
        self.guid = guid
