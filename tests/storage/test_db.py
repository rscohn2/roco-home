# SPDX-FileCopyrightText: 2020 Robert Cohn
#
# SPDX-License-Identifier: MIT

from collections import OrderedDict

events = [
    {'signal_guid': 'abc', 'time': 1, 'val': 0},
    {'signal_guid': 'abc', 'time': 2, 'val': 1},
    {'signal_guid': 'abd', 'time': 2, 'val': 1},
    {'signal_guid': 'abd', 'time': 3, 'val': 0},
]


def exercise_db(db):
    db.reset()
    table_info = {
        'sqlite': {
            'schema': OrderedDict(
                [
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
    q = table.query()
    assert len(list(q)) == len(events)


def test_sqlite(sqlite_db):
    exercise_db(sqlite_db)


def test_mongodb(local_mongodb):
    exercise_db(local_mongodb)
