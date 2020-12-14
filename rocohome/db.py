# SPDX-FileCopyrightText: 2020 Robert Cohn
#
# SPDX-License-Identifier: MIT

import logging
import tempfile
from abc import ABC

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

    def reset(self):
        """Delete all tables."""
        pass

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

    class Table:
        def __init__(self, db, name):
            """Creates handle for a table.

            Parameters
            ----------
            db : :class:`~rocohome.db.DB`
              Handle to DB
            name : str
              Table name


            """
            pass

        def put(self, object):
            """Save an object in the table."""
            pass

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
        try:
            logger.info('Deleting table: %s' % name)
            self.client.delete_table(TableName=name)
        except self.client.exceptions.ResourceNotFoundException:
            pass
        self.client.create_table(
            TableName=name,
            KeySchema=info['KeySchema'],
            AttributeDefinitions=info['AttributeDefinitions'],
            ProvisionedThroughput=DynamoDB._provisioned,
        )
        return self.Table(self, name)

    class Table(DB.Table):
        def __init__(self, db, name):
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
            logger.info('table: %s put: %s' % (self.name, object))
            self.table.put_item(Item=object)


class CSVDB(DB):
    def __init__(self, name=None):
        if name:
            self.name = name
        else:
            self.temp_dir = tempfile.TemporaryDirectory
            self.name = self.temp_dir.name
