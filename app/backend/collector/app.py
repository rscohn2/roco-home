# SPDX-FileCopyrightText: 2020 Robert Cohn
#
# SPDX-License-Identifier: MIT

# import os.path
# import subprocess
# import sys

import zignalz as zz


def create_app(test_config=None):
    uri = ''
    db = zz.MongoDB(uri)
    collector_app = zz.CollectorApp(db, test_config)
    return collector_app.app


app = create_app()
