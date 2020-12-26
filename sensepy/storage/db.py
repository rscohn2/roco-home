# SPDX-FileCopyrightText: 2020 Robert Cohn
#
# SPDX-License-Identifier: MIT

import logging
import sqlite3
from abc import ABC, abstractmethod

import boto3

"""Persistent storage for *store.

DB contains 1 or more Table. Store maps objects to dictionaries, and
DB manages the dictionaries as rows in a table.

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
            db : :class:`~sensepy.db.DB`
              Handle to DB
            name : str
              Table name


            """
            pass

        @abstractmethod
        def put(self, object):
            """Save an object in the table."""
            pass

        @abstractmethod
        def query(self):
            """Returns list of objects matching filter conditions."""
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
            self._schema = info['sqlite']['schema']

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
            keys = [field[0] for field in self._schema]
            for row in self.db.cursor.fetchall():
                o = dict(zip(keys, row))
                logger.info(f'query: {o}')
                yield o
