# SPDX-FileCopyrightText: 2020 Robert Cohn
#
# SPDX-License-Identifier: MIT

import logging

from rocohome import db

logger = logging.getLogger(__name__)

provisioned = {"ReadCapacityUnits": 1, "WriteCapacityUnits": 1}


def create_event_table(db_client):
    table_name = 'Events'
    if table_name in db_client.list_tables()['TableNames']:
        db_client.delete_table(TableName=table_name)
    db_client.create_table(
        TableName=table_name,
        KeySchema=[
            {'AttributeName': 'signal_guid', 'KeyType': 'HASH'},
            {'AttributeName': 'time', 'KeyType': 'RANGE'},
        ],
        AttributeDefinitions=[
            {'AttributeName': 'signal_guid', 'AttributeType': 'S'},
            {'AttributeName': 'time', 'AttributeType': 'N'},
        ],
        ProvisionedThroughput=provisioned,
    )
    db.events = db.resource().Table(table_name)
    return db.events


def create_tables():
    create_event_table(db.client())


def reset():
    create_tables()
