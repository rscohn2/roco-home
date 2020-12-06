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

    def signals(self, signal_names=None):
        """Returns a list of signal events associated with the list of
        signalnames.

        """

        # convert signal names to signals
        signals = [
            self.building.signals[signal_name] for signal_name in signal_names
        ]
        return self.event_store.signal_events(signals)
