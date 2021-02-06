# SPDX-FileCopyrightText: 2020 Robert Cohn
#
# SPDX-License-Identifier: MIT

import pytest

import zignalz as zz


@pytest.fixture
def test_account(init_stores):
    account = zz.Account('test-account')
    account.configure(init_stores)
    return account


@pytest.fixture
def test_project(test_account):
    return zz.Project('test-project', test_account)


@pytest.fixture
def test_device(test_project):
    return zz.Device('test-device', test_project)


@pytest.fixture
def test_signal(test_project):
    return zz.Signal('test-signal', test_project)
