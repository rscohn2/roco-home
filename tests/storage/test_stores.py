# SPDX-FileCopyrightText: 2020 Robert Cohn
#
# SPDX-License-Identifier: MIT

from zignalz import Account, Device, Project, Signal, SignalEvent


def test_init_store(init_stores):
    pass


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


def account_found(ref, accounts):
    for account in accounts:
        print('  checking:', account)
        if account_match(account, ref):
            return True
    return False


def account_store(init_stores):
    store = init_stores.account
    for account in accounts:
        store.put(account)
    q = list(store.query())
    assert len(accounts) == len(q)
    for account in accounts:
        assert account_found(account, q)


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


def project_found(ref, projects):
    for project in projects:
        if project_match(ref, project):
            return True
    return False


def project_store(init_stores):
    store = init_stores.project
    for project in projects:
        store.put(project)
    q = list(store.query())
    assert len(projects) == len(q)
    for project in projects:
        assert project_found(project, q)


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


def signal_found(ref, signals):
    for signal in signals:
        if signal_match(ref, signal):
            return True
    return False


def signal_store(init_stores):
    store = init_stores.signal
    for signal in signals:
        store.put(signal)
    q = list(store.query())
    assert len(signals) == len(q)
    for signal in signals:
        assert signal_found(signal, q)


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


def device_found(ref, devices):
    for device in devices:
        if device_match(ref, device):
            return True
    return False


def device_store(init_stores):
    store = init_stores.device
    for device in devices:
        store.put(device)
    q = list(store.query())
    assert len(devices) == len(q)
    for device in devices:
        assert device_found(device, q)


signal_events = [
    SignalEvent(0, devices[0], signals[0], 0),
    SignalEvent(1, devices[0], signals[0], 1),
    SignalEvent(2, devices[0], signals[0], 0),
    SignalEvent(3, devices[1], signals[1], 1),
]


def signal_event_match(ref, test):
    print('  checking', test)
    print('    with', test.signal)
    return (
        test.time == ref.time
        and device_match(test.device, ref.device)
        and signal_match(test.signal, ref.signal)
        and test.val == ref.val
    )


def signal_event_found(ref, signal_events):
    for signal_event in signal_events:
        if signal_event_match(ref, signal_event):
            return True
    return False


def signal_event_store(init_stores):
    store = init_stores.signal_events
    for signal_event in signal_events:
        store.put(signal_event)
    q = list(store.query())
    assert len(signal_events) == len(q)
    for signal_event in signal_events:
        print('look for', signal_event)
        print(' with', signal_event.signal)
        assert signal_event_found(signal_event, q)


def test_stores(init_stores):
    account_store(init_stores)
    project_store(init_stores)
    signal_store(init_stores)
    device_store(init_stores)
    signal_event_store(init_stores)
