# SPDX-FileCopyrightText: 2020 Robert Cohn
#
# SPDX-License-Identifier: MIT

"""Interface between log server front-end and persistent storage.

"""


class EventLogServer:
    """Interface between log server front-end and persistent storage."""

    def __init__(self, event_store, building):
        self.event_store = event_store
        self.building = building

    def events(self):
        return self.event_store.events()

    def signals(self, signal_names=None):
        """Returns a list of signal events associated with the list of
        signalnames.

        """

        assert False
        # convert signal names to signals
        signals = [
            self.building.signal_by_name[signal_name]
            for signal_name in signal_names
        ]
        return self.event_store.signal_events(signals)
