# SPDX-FileCopyrightText: 2020 Robert Cohn
#
# SPDX-License-Identifier: MIT

from signalpy import Account, AccountStore

accounts = [
    Account('guid1', 'name1', 'token1'),
    Account('guid2', 'name2', 'token2'),
    Account('guid3', 'name3', 'token3'),
]


def account_found(ref, accounts):
    for account in accounts:
        if (
            account.guid == ref.guid
            and account.name == ref.name
            and account.token == ref.token
        ):
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
