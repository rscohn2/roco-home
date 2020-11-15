from rocohome import db

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


def create_tables():
    create_device_table()


def reset():
    ''' Delete the tables '''

    for table in db.client().list_tables()['TableNames']:
        db.client().delete_table(TableName=table)
    create_tables()
