# SPDX-FileCopyrightText: 2020 Robert Cohn
#
# SPDX-License-Identifier: MIT

import logging
import sqlite3
from abc import ABC, abstractmethod

import boto3

"""Persistent storage.

The DB is used to abstract the database implementation.  A DB contains
1 or more Tables. A Table stores objects as dictionaries. The
:class:`~signalpy.storage.store.Store` is a higher-level abstraction
for a Table that stores objects as python objects.



Attributes
----------

DB : class
  Abstract base class for a database
DynamoDB : class
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
            db : :class:`~signalpy.db.DB`
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
        def query(self):
            """Returns iterator for objects matching filter conditions.

            Returns
            -------
            dict

            """
            pass


class DynamoDB(DB):
    _provisioned = {"ReadCapacityUnits": 1, "WriteCapacityUnits": 1}

    def __init__(self, port=8000):
        # cache handles
        self.client = boto3.client(
            'dynamodb', endpoint_url='http://localhost:%d' % port
        )
        self.resource = boto3.resource(
            'dynamodb', endpoint_url='http://localhost:%d' % port
        )

    def reset(self):
        for name in self.client.list_tables()['TableNames']:
            self.client.delete_table(TableName=name)

    def create_table(self, name, info):
        dynamo_info = info['dynamodb']
        try:
            logger.info(f'Deleting table: {name}')
            self.client.delete_table(TableName=name)
        except self.client.exceptions.ResourceNotFoundException:
            pass
        self.client.create_table(
            TableName=name,
            KeySchema=dynamo_info['KeySchema'],
            AttributeDefinitions=dynamo_info['AttributeDefinitions'],
            ProvisionedThroughput=DynamoDB._provisioned,
        )
        return self.Table(self, name, info)

    class Table(DB.Table):
        def __init__(self, db, name, info):
            self.db = db
            self.name = name
            self.table = db.resource.Table(name)

        def query(self, **kwargs):
            start_key = None
            while True:
                if start_key:
                    kwargs['ExclusiveStartKey'] = start_key
                response = self.table.scan(**kwargs)
                for object in response['Items']:
                    yield object
                start_key = response.get('LastEvaluatedKey', None)
                if start_key is None:
                    return

        def put(self, object):
            logger.info(f'table: {self.name} put: {object}')
            self.table.put_item(Item=object)


class SQLite3(DB):
    def __init__(self, path=':memory:'):
        self.path = path
        self.connector = sqlite3.connect(path)
        self.connector.row_factory = sqlite3.Row
        self.cursor = self.connector.cursor()

    def delete(self):
        self._execute(
            """SELECT name FROM sqlite_master
               WHERE type = 'table' AND name NOT LIKE 'sqlite_%';"""
        )
        for row in self.cursor.fetchall():
            self._execute(f'DROP TABLE {row[0]}')

    def reset(self):
        self.delete()
        self.__init__(self.path)

    def create_table(self, name, info):
        self._execute(f'DROP TABLE IF EXISTS {name}')
        schema = info['sqlite']['schema']
        sstring = ','.join(s[0] + ' ' + s[1] for s in schema)
        self._execute(f'CREATE TABLE {name} ({sstring});')
        return SQLite3.Table(self, name, info)

    def _execute(self, command, parameters=()):
        logger.info(f'sqlite execute. "{command}" with {parameters}')
        self.cursor.execute(command, parameters)

    class Table(DB.Table):
        def __init__(self, db, name, info):
            self.db = db
            self.name = name

        def put(self, object):
            fields = object.keys()
            fstring = ','.join(fields)
            qstring = ','.join(['?'] * len(fields))
            values = [object[k] for k in fields]
            self.db._execute(
                f'INSERT INTO {self.name} ({fstring}) VALUES ({qstring});',
                values,
            )

        def query(self):
            self.db._execute(f'SELECT * from {self.name}')
            return self.db.cursor


class MongoDB(DB):
    def __init__(self):
        pass

    def delete(self):
        pass

    def reset(self):
        pass

    def create_table(self, name, info):
        pass

    def _execute(self, command, parameters=()):
        pass

    class Table(DB.Table):
        def __init__(self, db, name, info):
            pass

        def put(self, object):
            pass

        def query(self):
            pass
