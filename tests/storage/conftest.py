# SPDX-FileCopyrightText: 2020 Robert Cohn
#
# SPDX-License-Identifier: MIT

import pytest

import zignalz as zz


@pytest.fixture(scope='session')
def local_dynamodb():
    instance = zz.LocalDynamoDB('dynamodb')
    yield zz.DynamoDB()
    instance.down()


@pytest.fixture
def local_mongodb(tmp_path):
    instance = zz.LocalMongoDB(tmp_path)
    yield zz.MongoDB()
    instance.down()
