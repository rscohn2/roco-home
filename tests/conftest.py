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
def configs_dir():
    return join(os.path.dirname(os.path.realpath(__file__)), 'configs')
