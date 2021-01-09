# SPDX-FileCopyrightText: 2020 Robert Cohn
#
# SPDX-License-Identifier: MIT


def test_hello(flask_client):
    rv = flask_client.get('hello')
    assert 'Hello from the collector' == rv.json['message']
    assert rv.status == '200 OK'


def test_bad_event(flask_client):
    rv = flask_client.post('signal_events', {'version': 3})
    assert rv.status == '400 BAD REQUEST'
    assert 'Validation' in rv.json['message']


def test_record_events(project, flask_client, device_events):
    for event in device_events:
        rv = flask_client.post('signal_events', event)
        assert 'Recorded event' == rv.json['message']
        assert rv.status == '200 OK'
