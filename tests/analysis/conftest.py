# SPDX-FileCopyrightText: 2020 Robert Cohn
#
# SPDX-License-Identifier: MIT

from os.path import join

import pandas as pd
import pytest


@pytest.fixture
def signal_events_df(data_dir):
    return pd.read_csv(join(data_dir, 'signal-events.csv'))
