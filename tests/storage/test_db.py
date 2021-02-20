# SPDX-FileCopyrightText: 2020 Robert Cohn
#
# SPDX-License-Identifier: MIT

from collections import OrderedDict

events = [
    {'guid': 'a', 'signal_guid': 'abc', 'time': 1, 'val': 0},
    {'guid': 'b', 'signal_guid': 'abc', 'time': 2, 'val': 1},
    {'guid': 'c', 'signal_guid': 'abd', 'time': 2, 'val': 1},
    {'guid': 'd', 'signal_guid': 'abd', 'time': 3, 'val': 0},
]


def get(table, guid):
    for i in list(table.query({'guid': guid})):
        assert i['guid'] == guid
        return i


def exercise_db(db):
    db.reset()
    table_info = {
        'sqlite': {
            'schema': OrderedDict(
                [
                    ('guid', 'text'),
                    ('signal_guid', 'text'),
                    ('time', 'integer'),
                    ('val', 'real'),
                ]
            )
        },
    }
    table = db.create_table('test', table_info)
    for event in events:
        table.put(event)
    assert len(list(table.query())) == len(events)
    table.delete(events[0])
    assert len(list(table.query())) == len(events) - 1
    b_obj = get(table, 'b')
    assert b_obj['signal_guid'] == 'abc'
    b_obj['signal_guid'] = 'efg'
    table.update(b_obj)
    assert get(table, 'b')['signal_guid'] == 'efg'


def test_sqlite(sqlite_db):
    exercise_db(sqlite_db)


def test_mongodb(local_mongodb):
    exercise_db(local_mongodb)
