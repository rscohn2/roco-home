# SPDX-FileCopyrightText: 2020 Robert Cohn
#
# SPDX-License-Identifier: MIT

import pytest

import signalpy as sp


@pytest.fixture(scope='session')
def local_dynamodb():
    instance = sp.LocalDynamoDB('dynamodb')
    yield sp.DynamoDB()
    instance.down()


@pytest.fixture
def local_mongodb(tmp_path):
    instance = sp.LocalMongoDB(tmp_path)
    yield sp.MongoDB()
    instance.down()
