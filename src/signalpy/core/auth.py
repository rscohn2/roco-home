# SPDX-FileCopyrightText: 2020 Robert Cohn
#
# SPDX-License-Identifier: MIT

import secrets
import uuid


def make_token():
    return secrets.token_urlsafe()


def make_guid():
    return str(uuid.uuid1())
