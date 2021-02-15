# SPDX-FileCopyrightText: 2020 Robert Cohn
#
# SPDX-License-Identifier: MIT

import json
import logging
import sqlite3
from abc import ABC, abstractmethod

import pymongo

"""Persistent storage.

The DB is used to abstract the database implementation.  A DB contains
1 or more Tables. A Table stores objects as dictionaries. The
:class:`~zignalz.storage.store.Store` is a higher-level abstraction
for a Table that stores objects as python objects.



Attributes
----------

DB : class
  Abstract base class for a database
MongoDB : class
  Concrete DB class
SqliteDB : class
  Concrete DB class

"""

logger = logging.getLogger(__name__)


class DB(ABC):
    """Abstract base class for DB."""

    @abstractmethod
    def reset(self):
        """Delete all tables."""
        pass

    @abstractmethod
    def create_table(self, name, info):
        """Create table.

        Create table, delete first if it exists.

        Parameters
        ----------
        db : object
          Handle to DB
        name : str
          Table name
        info : dict
          DB-specific info

        """
        pass

    class Table:
        @abstractmethod
        def __init__(self, db, name):
            """Creates handle for a table.

            Parameters
            ----------
            db : :class:`~zignalz.db.DB`
              Handle to DB
            name : str
              Table name


            """
            pass

        @abstractmethod
        def put(self, object):
            """Save an object in the table.

            Parameters
            ----------

            object : dict

            """
            pass

        @abstractmethod
        def delete(self, object):
            """Delete an object in the table.

            Parameters
            ----------

            object : dict

            """
            pass

        @abstractmethod
        def update(self, object):
            """Update an object in the table.

            Parameters
            ----------

            object : dict

            """
            pass

        @abstractmethod
        def query(self):
            """Returns iterator for objects matching filter conditions.

            Returns
            -------
            dict

            """
            pass


class SQLite3(DB):
    def __init__(self, path=':memory:'):
        self.path = path
        self.connector = sqlite3.connect(path)
        self.connector.row_factory = sqlite3.Row
        self.cursor = self.connector.cursor()

    def reset(self):
        self._execute(
            """SELECT name FROM sqlite_master
               WHERE type = 'table' AND name NOT LIKE 'sqlite_%';"""
        )
        for row in self.cursor.fetchall():
            self._execute(f'DROP TABLE {row[0]}')

    def create_table(self, name, info):
        self._execute(f'DROP TABLE IF EXISTS {name}')
        i = info['sqlite']
        sstring = ','.join(
            key + ' ' + value for key, value in i['schema'].items()
        )
        self._execute(f'CREATE TABLE {name} ({sstring});')
        return SQLite3.Table(self, name, info)

    def _execute(self, command, parameters=()):
        logger.info(f'sqlite execute. "{command}" with {parameters}')
        self.cursor.execute(command, parameters)

    class Table(DB.Table):
        def __init__(self, db, name, info):
            logger.info(f'table info {info}')
            self.info = info['sqlite']
            self.db = db
            self.name = name

        def put(self, object):
            fields = object.keys()
            fstring = ','.join(fields)
            qstring = ','.join(['?'] * len(fields))
            values = []
            for k in fields:
                if self.info['schema'][k] == 'json':
                    v = json.dumps(object[k])
                else:
                    v = object[k]
                values.append(v)
            self.db._execute(
                f'INSERT INTO {self.name} ({fstring}) VALUES ({qstring});',
                values,
            )

        def delete(self, object):
            self.db._execute(
                f'DELETE from {self.name} WHERE guid = "{object["guid"]}";'
            )

        def update(self, object):
            self.delete(object)
            self.put(object)

        def query(self):
            self.db._execute(f'SELECT * from {self.name}')
            for c in self.db.cursor:
                o = {}
                for k in self.info['schema']:
                    if self.info['schema'][k] == 'json':
                        v = json.loads(c[k])
                    else:
                        v = c[k]
                    o[k] = v
                yield o


class MongoDB(DB):
    def __init__(self, uri=None):
        self.client = pymongo.MongoClient(uri)
        self.db = self.client['zignalz']

    def reset(self):
        for col in self.db.list_collections():
            col.drop()

    def create_table(self, name, info):
        self.signal_events = self.db['signal_events']
        return self.Table(self, 'signal_events')

    class Table(DB.Table):
        def __init__(self, db, name):
            self.db = db
            self.collection = db.db[name]

        def put(self, object):
            self.collection.insert_one(object)

        def delete(self, object):
            self.collection.delete_one({'guid': object['guid']})

        def update(self, object):
            self.delete(object)
            self.put(object)

        def query(self):
            return self.collection.find()
