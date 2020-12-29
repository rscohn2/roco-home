# SPDX-FileCopyrightText: 2020 Robert Cohn
#
# SPDX-License-Identifier: MIT

import signalpy as sp


def test_log_server(signal_events_store, project):
    log_server = sp.EventLogServer(signal_events_store, project)
    o = log_server.signals()
    assert len(list(o)) == 21
