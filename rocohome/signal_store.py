# SPDX-FileCopyrightText: 2020 Robert Cohn
#
# SPDX-License-Identifier: MIT

"""Persistent storage for :class:`~rocohome.event.Event`.

"""

import logging

from boto3.dynamodb.conditions import Key

import rocohome as rh
from rocohome.store import Store

logger = logging.getLogger(__name__)


class SignalStore(Store):
    """Stores events from devices."""

    def signals(self):
        """Returns all events."""
        objects = super().scan()[0]
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
