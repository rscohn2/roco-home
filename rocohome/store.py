# SPDX-FileCopyrightText: 2020 Robert Cohn
#
# SPDX-License-Identifier: MIT

"""Persistent storage for objects.

"""

import logging
from abc import ABC

import rocohome as rh

logger = logging.getLogger(__name__)


class Store(ABC):
    """Base class for persistent storage of objects.

    Parameters
    ----------
    db : :class:`~rocohome.db.DB`
      Handle to DB
    name : str
      Name of store

    """

    def __init__(self, db, name):
        self.table = db.Table(db, name)

    def create(db, name, info):
        """Returns a :class:`~rocohome.store.Store`

        Creates a new Store. Deletes a Store with the same name.

        Parameters
        ----------
        db : :class:`~rocohome.db.DB`
          Handle to DB
        name : str
          Name of store
        info : dict
          database-specific info
        """
        db.create_table(name, info)

    def put(self, object):
        """Save an object.

        Parameters
        ----------
        object : object
          object with to_store method that returns a dict

        """
        self.table.put(object.to_store())

    def query(self):
        """Returns list of objects matching filter."""
        return self.table.query()


class SignalEventsStore(Store):
    """Stores events from devices."""

    table_name = 'SignalEvents'

    def __init__(self, db):
        super().__init__(db, SignalEventsStore.table_name)

    def create(db):
        table_info = {
            'KeySchema': [
                {'AttributeName': 'signal_guid', 'KeyType': 'HASH'},
                {'AttributeName': 'time', 'KeyType': 'RANGE'},
            ],
            'AttributeDefinitions': [
                {'AttributeName': 'signal_guid', 'AttributeType': 'S'},
                {'AttributeName': 'time', 'AttributeType': 'N'},
            ],
        }
        Store.create(db, SignalEventsStore.table_name, table_info)
        return SignalEventsStore(db)

    def query(self):
        for object in super().query():
            # convert dictionaries to Signals
            yield rh.SignalEvent(from_store=object)
