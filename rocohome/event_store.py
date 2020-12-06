# SPDX-FileCopyrightText: 2020 Robert Cohn
#
# SPDX-License-Identifier: MIT

"""Persistent storage for :class:`~rocohome.event.Event`.

"""

import logging

from boto3.dynamodb.conditions import Key

import rocohome as rh
from rocohome.object_store import ObjectStore

logger = logging.getLogger(__name__)


class EventStore(ObjectStore):
    """Stores events from devices.

    Inherits from :class:`~rocohome.object_store.ObjectStore`

    """

    def signal_events(self, signals=None):
        """Returns signal events associated with a list of signals."""
        signal_guids = [signal.guid for signal in signals]
        # retrieve the events associated with the guids from the event store
        # FIXME: get all the guids, not just the first one
        objects = super().scan(
            FilterExpression=Key('signal_guid').eq(signal_guids[0])
        )
        # convert dictionaries to Signals
        return [rh.SignalEvent(from_store=object) for object in objects]

    def reset(self):
        """Resets store to empty.

        Creates if doesn't exist, delete/create if it does exist.
        """
        super().create_table(
            'Events',
            key_schema=[
                {'AttributeName': 'signal_guid', 'KeyType': 'HASH'},
                {'AttributeName': 'time', 'KeyType': 'RANGE'},
            ],
            attribute_definitions=[
                {'AttributeName': 'signal_guid', 'AttributeType': 'S'},
                {'AttributeName': 'time', 'AttributeType': 'N'},
            ],
        )
