# SPDX-FileCopyrightText: 2020 Robert Cohn
#
# SPDX-License-Identifier: MIT

from signalpy.analytics import activations


def test_activations(signal_events_store):
    df = activations.extract_activations(signal_events_store)
    assert len(df.index) == 9
