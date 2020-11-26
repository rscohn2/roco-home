import logging

from rocohome import db

logger = logging.getLogger(__name__)

provisioned = {"ReadCapacityUnits": 1, "WriteCapacityUnits": 1}


def create_observation_table():
    db.client().create_table(
        TableName='Observations',
        KeySchema=[
            {'AttributeName': 'sensor_name', 'KeyType': 'HASH'},
            {'AttributeName': 'time', 'KeyType': 'RANGE'},
        ],
        AttributeDefinitions=[
            {'AttributeName': 'sensor_name', 'AttributeType': 'S'},
            {'AttributeName': 'time', 'AttributeType': 'N'},
        ],
        ProvisionedThroughput=provisioned,
    )
    db.observations = db.resource().Table('Observations')


def create_tables():
    create_observation_table()


def reset():
    for table in db.client().list_tables()['TableNames']:
        db.client().delete_table(TableName=table)
    create_tables()
