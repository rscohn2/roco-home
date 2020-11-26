import json
import os.path
from os.path import join

import pytest

import rocohome as rh
import rocohome.cli as cli
import rocohome.db as db


class MockArgs:
    dry_run = False
    jar_dir = 'dynamodb'


@pytest.fixture(scope='session')
def mock_args():
    cli.args = MockArgs()


@pytest.fixture(scope='session')
def db_instance(mock_args):
    print('Starting instance')
    db_pid = rh.db.local.up()
    yield db_pid
    print('Stoping instance')
    db.local.down(db_pid)


@pytest.fixture
def reset_db(db_instance):
    db.admin.reset()


@pytest.fixture(scope='session')
def data_dir():
    return join(os.path.dirname(os.path.realpath(__file__)), 'data')


@pytest.fixture(scope='session')
def short_observations(data_dir):
    with open(join(data_dir, 'observations', 'short.json'), 'r') as stream:
        return json.load(stream)


@pytest.fixture(scope='session')
def home_config(data_dir):
    rh.config.config.set(join(data_dir, 'configs', 'test1.yaml'))
