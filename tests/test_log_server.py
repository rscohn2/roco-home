# SPDX-FileCopyrightText: 2020 Robert Cohn
#
# SPDX-License-Identifier: MIT

import rocohome.services as rservices


def test_log_server(signal_events_store, building):
    log_server = rservices.EventLogServer(signal_events_store, building)
    o = log_server.signals()
    assert len(list(o)) == 21
