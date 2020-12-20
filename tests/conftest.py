# SPDX-FileCopyrightText: 2020 Robert Cohn
#
# SPDX-License-Identifier: MIT

import json
import os.path
from os.path import join

import pytest

import rocohome.core as rcore
import rocohome.services as rservices
import rocohome.services.cli as cli
import rocohome.storage as rstorage


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


@pytest.fixture
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
    return join(os.path.dirname(os.path.realpath(__file__)), 'data')


@pytest.fixture(scope='session')
def device_events(data_dir):
    with open(join(data_dir, 'events', 'short.json'), 'r') as stream:
        return json.load(stream)


@pytest.fixture(scope='session')
def account():
    return rcore.Account(
        'rscohn2', {'guid': 'acea2d90-325e-11eb-aef5-00155d093636'}
    )


@pytest.fixture(scope='session')
def building(account, data_dir):
    return account.load_building(join(data_dir, 'buildings', 'home.yaml'))


@pytest.fixture
def empty_signal_events_store(local_dynamodb):
    store = rstorage.SignalEventsStore.create(local_dynamodb)
    return store


@pytest.fixture
def signal_events_store(building, empty_signal_events_store, device_events):
    store = empty_signal_events_store
    collector = rservices.EventCollector(store)
    for device_event in device_events:
        collector.record_event(device_event)
    return store
