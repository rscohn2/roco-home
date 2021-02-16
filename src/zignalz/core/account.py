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

    def __init__(self, name, guid, token=None):
        """Construct an account."""
        self.guid = guid
        self.name = name
        self.token = token if token else zz.make_token()

    def configure(self, stores):
        self.stores = stores
