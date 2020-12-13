# SPDX-FileCopyrightText: 2020 Robert Cohn
#
# SPDX-License-Identifier: MIT

"""Persistent storage for objects.

"""

import logging

from rocohome import db

logger = logging.getLogger(__name__)


class Store:
    """Base class for persistent storage of objects."""

    _provisioned = {"ReadCapacityUnits": 1, "WriteCapacityUnits": 1}

    def __init__(self):
        self.table = None
        self.table_name = None

    def _delete_table(self):
        try:
            logger.info('Deleting table: %s' % self.table_name)
            db.client().delete_table(TableName=self.table_name)
        except db.client().exceptions.ResourceNotFoundException:
            return

    def create_table(self, table_name, key_schema, attribute_definitions):
        """Create a persistent store for this object.

        Delete if it already exists.

        """
        self.table_name = table_name
        self._delete_table()
        db.client().create_table(
            TableName=self.table_name,
            KeySchema=key_schema,
            AttributeDefinitions=attribute_definitions,
            ProvisionedThroughput=Store._provisioned,
        )
        self.table = db.resource().Table(self.table_name)
        assert self.table is not None

    def put(self, object):
        """Save an object."""
        encoded_object = object.to_store()
        logger.info(
            'saving object %s to %s' % (encoded_object, self.table_name)
        )
        self.table.put_item(Item=encoded_object)

    def scan(self, **kwargs):
        """Returns list of objects as dictionaries based on scan criteria."""
        start_key = None
        objects = []
        while True:
            if start_key:
                kwargs['ExclusiveStartKey'] = start_key
            response = self.table.scan(**kwargs)
            objects.append(response.get('Items', []))
            start_key = response.get('LastEvaluatedKey', None)
            if start_key is None:
                return objects
