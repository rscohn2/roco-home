# SPDX-FileCopyrightText: 2020 Robert Cohn
#
# SPDX-License-Identifier: MIT

import zignalz as zz


class Signal(zz.Object):
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
