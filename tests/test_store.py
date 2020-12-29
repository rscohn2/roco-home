# SPDX-FileCopyrightText: 2020 Robert Cohn
#
# SPDX-License-Identifier: MIT

import signalpy as sp


def exercise_store(store, events):
    for event in events:
        store.put(event)
    q = store.query()
    assert len(list(q)) == len(events)


def test_signalstore(empty_signal_events_store, project):
    store_signal_events = [
        {
            'device_guid': 'ec:fa:bc:c5:b8:90',
            'signal_guid': '8a050fe8-325e-11eb-a2da-00155d093636',
            'val': 0,
            'time': 1,
        },
        {
            'device_guid': 'ec:fa:bc:c5:b8:90',
            'signal_guid': '9013db30-325e-11eb-bead-00155d093636',
            'val': 0,
            'time': 2,
        },
    ]
    events = [sp.SignalEvent(from_store=e) for e in store_signal_events]
    exercise_store(empty_signal_events_store, events)
