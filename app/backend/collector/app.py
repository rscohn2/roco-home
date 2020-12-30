# SPDX-FileCopyrightText: 2020 Robert Cohn
#
# SPDX-License-Identifier: MIT

import signalpy as sp

def create_app(test_config=None):
    db = sp.SQLite3()
    collector_app = sp.CollectorApp(db, test_config)
    return collector_app.app
