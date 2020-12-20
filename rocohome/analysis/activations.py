# SPDX-FileCopyrightText: 2020 Robert Cohn
#
# SPDX-License-Identifier: MIT

import logging

import pandas as pd

logger = logging.getLogger(__name__)


def extract_activations(signal_events):
    times = []
    signals = []
    durations = []
    begin = {}
    for se in signal_events.query():
        name = se.signal.name
        if se.val == 0:
            if name in begin:
                times.append(se.time)
                signals.append(name)
                durations.append(se.time - begin[name])
                del begin[name]
        else:
            begin[name] = se.time
    df = pd.DataFrame(
        data={'time': times, 'signal': signals, 'duration': durations}
    )
    logger.info('activations:\n%s' % df)
    return df
