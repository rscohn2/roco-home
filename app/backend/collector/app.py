# SPDX-FileCopyrightText: 2020 Robert Cohn
#
# SPDX-License-Identifier: MIT

# import os.path
# import subprocess
# import sys

import signalpy as sp


def create_app(test_config=None):
    uri = ''
    db = sp.MongoDB(uri)
    collector_app = sp.CollectorApp(db, test_config)
    return collector_app.app


app = create_app()
