# SPDX-FileCopyrightText: 2020 Robert Cohn
#
# SPDX-License-Identifier: MIT

import json
from os import path

import pytest

import signalpy.core as rcore
import signalpy.services as rservices
import signalpy.services.cli as cli
import signalpy.storage as rstorage


class MockArgs:
    dry_run = False
    jar_dir = 'dynamodb'


@pytest.fixture(scope='session')
def mock_args():
    cli.args = MockArgs()


@pytest.fixture(scope='session')
def local_dynamodb_instance(mock_args):
    print('Starting instance')
    db_pid = rstorage.dynamodb.local.up()
    yield db_pid
    print('Stopping instance')
    rstorage.dynamodb.local.down(db_pid)


@pytest.fixture(scope='session')
def sqlite_db():
    db = rstorage.SQLite3()
    yield db
    db.delete()


@pytest.fixture
def local_dynamodb(local_dynamodb_instance):
    db = rstorage.DynamoDB()
    db.reset()
    return db


@pytest.fixture(scope='session')
def data_dir():
    return path.join(path.dirname(path.realpath(__file__)), 'data')


@pytest.fixture(scope='session')
def device_events(data_dir):
    with open(path.join(data_dir, 'events', 'short.json'), 'r') as stream:
        return json.load(stream)


@pytest.fixture
def project(data_dir):
    account = rcore.Account(
        'rscohn2', {'guid': 'acea2d90-325e-11eb-aef5-00155d093636'}
    )
    return account.load_project(
        path.join(
            data_dir,
            'configs',
            'test1',
            'accounts',
            account.name,
            'projects',
            'home',
            'signalpy-project.yml',
        )
    )


@pytest.fixture
def empty_signal_events_store(sqlite_db):
    return rstorage.SignalEventsStore.create(sqlite_db)


@pytest.fixture
def signal_events_store(project, empty_signal_events_store, device_events):
    store = empty_signal_events_store
    collector = rservices.EventCollector(store)
    for device_event in device_events:
        collector.record_event(device_event)
    return store
