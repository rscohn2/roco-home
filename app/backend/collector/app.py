# SPDX-FileCopyrightText: 2020 Robert Cohn
#
# SPDX-License-Identifier: MIT

# import os.path
# import subprocess
# import sys

import signalpy as sp


def create_app(test_config=None):
    # print('A message')
    # print('executable: %s' % sys.executable)
    # subprocess.call('ls -l %s' % os.path.dirname(sys.executable), shell=True)
    # subprocess.call('ls -Rl', shell=True)
    # subprocess.call('pip list', shell=True)
    # subprocess.call('pip install -r requirements.txt', shell=True)
    # subprocess.call('pip list', shell=True)

    db = sp.SQLite3()
    collector_app = sp.CollectorApp(db, test_config)
    return collector_app.app


app = create_app()
