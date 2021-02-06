# SPDX-FileCopyrightText: 2020 Robert Cohn
#
# SPDX-License-Identifier: MIT

import pytest

import signalpy as sp


@pytest.fixture
def test_account(init_stores):
    account = sp.Account('test-account')
    account.configure(init_stores)
    return account


@pytest.fixture
def test_project(test_account):
    return sp.Project('test-project', test_account)


@pytest.fixture
def test_device(test_project):
    return sp.Device('test-device', test_project)


@pytest.fixture
def test_signal(test_project):
    return sp.Signal('test-signal', test_project)
