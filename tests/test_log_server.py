# SPDX-FileCopyrightText: 2020 Robert Cohn
#
# SPDX-License-Identifier: MIT

import rocohome as rh


def test_log_server(populated_event_table, building):
    log_server = rh.LogServer(populated_event_table, building)
    o = log_server.query('1st-floor-circulator')
    assert len(o) == 7
