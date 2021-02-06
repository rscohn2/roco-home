# SPDX-FileCopyrightText: 2020 Robert Cohn
#
# SPDX-License-Identifier: MIT

import json
from os import path

import pytest
import yaml

import signalpy as sp


@pytest.fixture(scope='session')
def session_tmp_dir(tmp_path_factory):
    return tmp_path_factory.mktemp('data')


@pytest.fixture(scope='session')
def sqlite_db(session_tmp_dir):
    db = sp.SQLite3(path.join(session_tmp_dir, 'sqllite.db'))
    db.reset()
    return db


@pytest.fixture
def init_stores(sqlite_db):
    sqlite_db.reset()
    return sp.Stores(sqlite_db)


@pytest.fixture
def local_dynamodb(local_dynamodb_instance):
    db = sp.DynamoDB()
    db.reset()
    return db


@pytest.fixture(scope='session')
def data_dir():
    return path.join(path.dirname(path.realpath(__file__)), 'data')


@pytest.fixture(scope='session')
def device_events(data_dir):
    with open(path.join(data_dir, 'events', 'short.json'), 'r') as stream:
        return json.load(stream)


@pytest.fixture(scope='session')
def home_events(data_dir):
    with open(path.join(data_dir, 'events', 'home.json'), 'r') as stream:
        return json.load(stream)


home_overrides = {
    'furnace': {'guid': 'furnace_guid', 'token': 'furnace_token'},
    'attic': {'guid': 'attic_guid', 'token': 'attic_token'},
}


@pytest.fixture
def stores_with_home_project(init_stores, data_dir):
    with open(
        path.join(
            data_dir, 'configs', 'test2', 'projects', 'rscohn2', 'home.yml'
        )
    ) as fin:
        project_info = yaml.safe_load(fin)
    account = sp.Account('rscohn2')
    account.configure(init_stores)
    project = sp.Project(name='home', account=account)
    project.configure(project_info, home_overrides)
    return init_stores


@pytest.fixture
def home_project(init_stores, data_dir):
    with open(
        path.join(
            data_dir, 'configs', 'test2', 'projects', 'rscohn2', 'home.yml'
        )
    ) as fin:
        project_info = yaml.safe_load(fin)
    print('project_info:', project_info)
    account = sp.Account('rscohn2')
    account.configure(init_stores)
    project = sp.Project(name='home', account=account)
    project.configure(project_info, home_overrides)
    return project


@pytest.fixture
def stores_with_home_events(stores_with_home_project, home_events):
    collector = sp.Collector(stores_with_home_project)
    for event in home_events:
        collector.record_event(event)
    return stores_with_home_project
