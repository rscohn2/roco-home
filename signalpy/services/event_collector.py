# SPDX-FileCopyrightText: 2020 Robert Cohn
#
# SPDX-License-Identifier: MIT

"""Interface between collector front-end and persistent storage.

"""

import logging

import marshmallow as mm

import signalpy as sp

logger = logging.getLogger(__name__)


class EventCollector:
    """Interface between collector front-end and persistent storage."""

    def __init__(self, event_store):
        self.accounts = {}
        self.store = event_store
        self.schemas = {'sensor': sp.SignalEvent.DeviceSchema(unknown=mm.EXCLUDE)}

    def record_event(self, device_event):
        """Insert an event into the Event Store.

        Convert from device-generate dict into
        :class:`~signalpy.core.event.Event`.

        """
        logger.info(f'recording event: {device_event}')
        try:
            schema =self.schemas[device_event['event']] 
            event = schema.load(device_event)
            self.store.put(event)
        except KeyError:
            logger.error(f'unknown event: {device_event["event"]}')
