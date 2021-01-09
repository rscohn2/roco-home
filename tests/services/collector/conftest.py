# SPDX-FileCopyrightText: 2020 Robert Cohn
#
# SPDX-License-Identifier: MIT

import pytest

import signalpy as sp


def end_point(path):
    return f'/api/v1/{path}'


class FlaskClient:
    def __init__(self, client):
        self.client = client

    def post(self, path, data):
        return self.client.post(end_point(path), data=data)

    def get(self, path):
        return self.client.get(end_point(path))


@pytest.fixture()
def flask_client():
    db = sp.SQLite3()
    collector = sp.CollectorApp(db, test_config=None)
    collector.app.config['TESTING'] = True

    with collector.app.test_client() as client:
        yield FlaskClient(client)
