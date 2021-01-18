# SPDX-FileCopyrightText: 2020 Robert Cohn
#
# SPDX-License-Identifier: MIT

"""Events occur on a device and are recorded in the database.

"""

import logging

import signalpy as sp

logger = logging.getLogger(__name__)


class Event(sp.Object):
    """Representation of an event.

    Attributes:
       time
         UTC timestamp
       raw
         Incoming representation
    """

    pass


class SignalEvent(Event):
    """Representation of an signal event.

    Attributes:
       time
         UTC timestamp
       signal (:class:`~signalpy.core.signal.Signal`)
       val
         recorded value
       raw
         Incoming representation
    """

    def __init__(self, time, device, signal, val):
        self.time = time
        self.device = device
        self.signal = signal
        self.val = val
