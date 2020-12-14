# SPDX-FileCopyrightText: 2020 Robert Cohn
#
# SPDX-License-Identifier: MIT

events = [
    {'signal_guid': 'abc', 'time': 1, 'val': 0},
    {'signal_guid': 'abc', 'time': 2, 'val': 1},
    {'signal_guid': 'abd', 'time': 2, 'val': 1},
    {'signal_guid': 'abd', 'time': 3, 'val': 0},
]


def exercise_db(db):
    db.reset()
    table_info = {
        'KeySchema': [
            {'AttributeName': 'signal_guid', 'KeyType': 'HASH'},
            {'AttributeName': 'time', 'KeyType': 'RANGE'},
        ],
        'AttributeDefinitions': [
            {'AttributeName': 'signal_guid', 'AttributeType': 'S'},
            {'AttributeName': 'time', 'AttributeType': 'N'},
        ],
    }
    table = db.create_table('test', table_info)
    for event in events:
        table.put(event)
    q = table.query()
    assert len(q) == len(events)


def test_dynamodb(local_dynamodb):
    exercise_db(local_dynamodb)
