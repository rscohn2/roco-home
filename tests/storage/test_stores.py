# SPDX-FileCopyrightText: 2020 Robert Cohn
#
# SPDX-License-Identifier: MIT

from signalpy import Account, Device, Project, Signal


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


def test_account_store(init_stores):
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


def test_project_store(init_stores):
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


def test_signal_store(init_stores):
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


def test_device_store(init_stores):
    store = init_stores.device
    for device in devices:
        store.put(device)
    q = list(store.query())
    assert len(devices) == len(q)
    for device in devices:
        assert device_found(device, q)
