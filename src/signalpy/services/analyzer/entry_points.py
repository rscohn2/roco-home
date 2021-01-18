# SPDX-FileCopyrightText: 2020 Robert Cohn
#
# SPDX-License-Identifier: MIT

"""Entry points for analyzer service.

"""


class Analyzer:
    """Interface between log server front-end and persistent storage."""

    def __init__(self, signal_store, building):
        self.signal_store = signal_store
        self.building = building

    def signals(self):
        return self.signal_store.query()