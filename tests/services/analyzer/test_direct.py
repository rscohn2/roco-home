# SPDX-FileCopyrightText: 2020 Robert Cohn
#
# SPDX-License-Identifier: MIT

import pytest

import zignalz as zz


@pytest.mark.skip
def test_analyzer(stores_with_home_events, home_events):
    analyzer = zz.Analyzer(stores_with_home_events)
    o = analyzer.signals()
    assert len(list(o)) == len(home_events)
