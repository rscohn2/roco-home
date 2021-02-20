# SPDX-FileCopyrightText: 2020 Robert Cohn
#
# SPDX-License-Identifier: MIT

import logging

import zignalz as zz

logger = logging.getLogger(__name__)


class Account(zz.Object):
    """Representation of an account.

    Account is modeled after GitHub account where projects are
    repositories.

    """

    _by_name = {}

    def __init__(self, name, guid=None, token=None):
        """Construct an account."""
        self.guid = guid if guid else zz.make_guid()
        self.name = name
        self.token = token if token else zz.make_token()
        Account._by_name[self.name] = self

    def by_name(name):
        return Account._by_name[name]

    def configure(self, stores):
        self.stores = stores
