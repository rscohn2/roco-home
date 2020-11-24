import logging

from rocohome import config, db

logger = logging.getLogger(__name__)

provisioned = {"ReadCapacityUnits": 1, "WriteCapacityUnits": 1}


def create_device_table():
    db.client().create_table(
        TableName='Devices',
        KeySchema=[
            {'AttributeName': 'mac', 'KeyType': 'HASH'},
            {'AttributeName': 'name', 'KeyType': 'RANGE'},
        ],
        AttributeDefinitions=[
            {'AttributeName': 'mac', 'AttributeType': 'S'},
            {'AttributeName': 'name', 'AttributeType': 'S'},
        ],
        ProvisionedThroughput=provisioned,
    )
    db.devices = db.resource().Table('Devices')
    with db.devices.batch_writer() as batch:
        for name in config.config['devices']:
            device_info = config.config['devices'][name]
            logger.info('Adding device: %s: %s' % (name, device_info))
            batch.put_item(Item={'name': name, 'mac': device_info['mac']})


def create_tables():
    create_device_table()


def reset(config_file):
    ''' Delete the tables '''

    config.load(config_file)
    for table in db.client().list_tables()['TableNames']:
        db.client().delete_table(TableName=table)
    create_tables()
