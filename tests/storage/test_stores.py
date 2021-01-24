# SPDX-FileCopyrightText: 2020 Robert Cohn
#
# SPDX-License-Identifier: MIT

from signalpy import Account, AccountStore
from signalpy import Project, DeviceStore
from signalpy import Project, ProjectStore
from signalpy import Signal, SignalStore

accounts = [
    Account('guid1', 'account1', 'token1'),
    Account('guid2', 'account2', 'token2'),
    Account('guid3', 'account3', 'token3'),
]


def account_match(ref, account):
    return (account.guid == ref.guid
            and account.name == ref.name
            and account.token == ref.token)


def account_found(ref, accounts):
    for account in accounts:
        if account_match(account, ref):
            return True
    return False


def test_account_store(sqlite_db):
    store = AccountStore.create(sqlite_db)
    for account in accounts:
        store.put(account)
    q = list(store.query())
    assert len(accounts) == len(q)
    for account in accounts:
        assert account_found(account, q)

projects = [
    Project('guid1', 'project1', accounts[0]),
    Project('guid2', 'project2', accounts[1]),
    Project('guid3', 'project3', accounts[2]),
]


def project_match(ref, project):
    return (project.guid == ref.guid
            and project.name == ref.name
            and account_match(project.account, ref.account))

def project_found(ref, projects):
    for project in projects:
        if project_match(ref, project):
            return True
    return False


def test_project_store(sqlite_db):
    store = ProjectStore.create(sqlite_db)
    for project in projects:
        store.put(project)
    q = list(store.query())
    assert len(projects) == len(q)
    for project in projects:
        assert project_found(project, q)

signals = [
    Signal('guid1', 'signal1', projects[0]),
    Signal('guid2', 'signal2', projects[0]),
    Signal('guid3', 'signal3', projects[2]),
]


def signal_match(ref, signal):
    return (signal.guid == ref.guid
            and signal.name == ref.name
            and project_match(signal.project, ref.project))

def signal_found(ref, signals):
    for signal in signals:
        if signal_match(ref, signal):
            return True
    return False


def test_signal_store(sqlite_db):
    store = SignalStore.create(sqlite_db)
    for signal in signals:
        store.put(signal)
    q = list(store.query())
    assert len(signals) == len(q)
    for signal in signals:
        assert signal_found(signal, q)
        
devices = [
    Signal('guid1', 'device1', projects[0]),
    Signal('guid2', 'device2', projects[0]),
    Signal('guid3', 'device3', projects[2]),
]


def device_match(ref, device):
    return (device.guid == ref.guid
            and device.name == ref.name
            and project_match(device.project, ref.project))

def device_found(ref, devices):
    for device in devices:
        if device_match(ref, device):
            return True
    return False


def test_device_store(sqlite_db):
    store = DeviceStore.create(sqlite_db)
    for device in devices:
        store.put(device)
    q = list(store.query())
    assert len(devices) == len(q)
    for device in devices:
        assert device_found(device, q)
        
