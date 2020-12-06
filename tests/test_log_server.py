# SPDX-FileCopyrightText: 2020 Robert Cohn
#
# SPDX-License-Identifier: MIT

import rocohome as rh


def test_log_server(populated_event_store, building):
    log_server = rh.EventLogServer(populated_event_store, building)
    o = log_server.signals(['1st-floor-circulator'])
    assert len(o) == 7
