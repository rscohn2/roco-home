# SPDX-FileCopyrightText: 2020 Robert Cohn
#
# SPDX-License-Identifier: MIT

import pytest

from zignalz import cli


@pytest.mark.skip
def test_db_start():
    cli.db.up()
    cli.db.down()
