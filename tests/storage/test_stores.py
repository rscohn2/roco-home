# SPDX-FileCopyrightText: 2020 Robert Cohn
#
# SPDX-License-Identifier: MIT

import logging

from zignalz import Account, Device, Project, Signal, SignalEvent

logger = logging.getLogger(__name__)


def test_init_store(init_stores):
    pass


def found(ref, objects, match):
    logger.info(f'looking for {ref}')
    for o in objects:
        logger.info(f'  checking {o}')
        if match(o, ref):
            return True
    return False


def exercise_store(objects, store, match):
    for o in objects:
        store.put(o)
    q = list(store.query())
    assert len(objects) == len(q)
    for o in objects:
        assert found(o, q, match)
    store.delete(objects[0])
    q = list(store.query())
    assert not found(objects[0], q, match)
    objects[1].name = 'foo'
    store.update(objects[1])
    q = list(store.query())
    assert found(objects[1], q, match)


accounts = [
    Account('account1'),
    Account('account2'),
    Account('account3'),
]


def account_match(ref, account):
    return (
        account.guid == ref.guid
        and account.name == ref.name
        and account.token == ref.token
    )

projects = [
    Project('project1', accounts[0]),
    Project('project2', accounts[1]),
    Project('project3', accounts[2]),
]


def project_match(ref, project):
    return (
        project.guid == ref.guid
        and project.name == ref.name
        and account_match(project.account, ref.account)
    )

signals = [
    Signal('signal1', projects[0]),
    Signal('signal2', projects[0]),
    Signal('signal3', projects[2]),
]


def signal_match(ref, signal):
    return (
        signal.guid == ref.guid
        and signal.name == ref.name
        and project_match(signal.project, ref.project)
    )


devices = [
    Device('device1', projects[0]),
    Device('device2', projects[0]),
    Device('device3', projects[2]),
]


def device_match(ref, device):
    return (
        device.guid == ref.guid
        and device.name == ref.name
        and project_match(device.project, ref.project)
    )


signal_events = [
    SignalEvent(0, devices[0], signals[0], 0),
    SignalEvent(1, devices[0], signals[0], 1),
    SignalEvent(2, devices[0], signals[0], 0),
    SignalEvent(3, devices[1], signals[1], 1),
]


def signal_event_match(ref, test):
    return (
        test.time == ref.time
        and device_match(test.device, ref.device)
        and signal_match(test.signal, ref.signal)
        and test.val == ref.val
    )


def test_stores(init_stores):
    exercise_store(accounts, init_stores.account, account_match)
    exercise_store(projects, init_stores.project, project_match)
    exercise_store(signals, init_stores.signal, signal_match)
    exercise_store(devices, init_stores.device, device_match)
    exercise_store(
        signal_events, init_stores.signal_events, signal_event_match
    )
