# SPDX-FileCopyrightText: 2020 Robert Cohn
#
# SPDX-License-Identifier: MIT

import pytest

from zignalz.analytics import activations


@pytest.mark.skip
def test_activations(signal_events_store):
    df = activations.extract_activations(signal_events_store)
    assert len(df.index) == 9
