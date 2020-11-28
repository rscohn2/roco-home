import logging

from rocohome import db

logger = logging.getLogger(__name__)

provisioned = {"ReadCapacityUnits": 1, "WriteCapacityUnits": 1}


def create_observation_table(db_client):
    table_name = 'Observations'
    if table_name in db_client.list_tables()['TableNames']:
        db_client.delete_table(TableName=table_name)
    db_client.create_table(
        TableName=table_name,
        KeySchema=[
            {'AttributeName': 'observed_id', 'KeyType': 'HASH'},
            {'AttributeName': 'time', 'KeyType': 'RANGE'},
        ],
        AttributeDefinitions=[
            {'AttributeName': 'observed_id', 'AttributeType': 'S'},
            {'AttributeName': 'time', 'AttributeType': 'N'},
        ],
        ProvisionedThroughput=provisioned,
    )
    db.observations = db.resource().Table(table_name)
    return db.observations


def create_tables():
    create_observation_table(db.client())


def reset():
    for table in db.client().list_tables()['TableNames']:
        db.client().delete_table(TableName=table)
    create_tables()
