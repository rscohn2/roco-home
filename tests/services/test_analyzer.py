# SPDX-FileCopyrightText: 2020 Robert Cohn
#
# SPDX-License-Identifier: MIT

import signalpy as sp


def test_analyzer(signal_events_store, project):
    analyzer = sp.Analyzer(signal_events_store, project)
    o = analyzer.signals()
    assert len(list(o)) == 21
