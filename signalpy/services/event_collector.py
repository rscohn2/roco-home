# SPDX-FileCopyrightText: 2020 Robert Cohn
#
# SPDX-License-Identifier: MIT

"""Interface between collector front-end and persistent storage.

"""

import logging

import signalpy.core.event as spevent

logger = logging.getLogger(__name__)


class EventCollector:
    """Interface between collector front-end and persistent storage."""

    def __init__(self, event_store):
        self.accounts = {}
        self.store = event_store

    def record_event(self, device_event):
        """Insert an event into the Event Store.

        Convert from device-generate dict into
        :class:`~signalpy.core.event.Event`.

        """
        logger.info('recording event: %s' % device_event)
        event = spevent._device_decode_event(device_event)
        self.store.put(event)
