# SPDX-FileCopyrightText: 2020 Robert Cohn
#
# SPDX-License-Identifier: MIT

import rocohome as rh


def test_log_server(populated_signal_events_store, building):
    log_server = rh.EventLogServer(populated_signal_events_store, building)
    o = log_server.signals()
    assert len(list(o)) == 21
