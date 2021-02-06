# SPDX-FileCopyrightText: 2020 Robert Cohn
#
# SPDX-License-Identifier: MIT

"""Entry points for analyzer service.

"""


class Analyzer:
    """Interface between log server front-end and persistent storage."""

    def __init__(self, stores):
        self.stores = stores

    def signals(self):
        return self.stores.signal_events.query()
