# SPDX-FileCopyrightText: 2020 Robert Cohn
#
# SPDX-License-Identifier: MIT

# import os.path
# import subprocess
# import sys

import signalpy as sp


def create_app(test_config=None):
    uri = (
        'mongodb://signalpy-db:orTeDdQGZmu1k3O0TJVpJjwMb8qll'
        'TylJlFwyx2QGQCCw6CWjlsjq17gn2e9FrrvYELHxFXpS1cFqK1V'
        'kw6OSQ==@signalpy-db.mongo.cosmos.azure.com:10255/'
        '?ssl=true'
        '&replicaSet=globaldb'
        '&maxIdleTimeMS=120000'
        '&appName=@signalpy-db@'
    )
    db = sp.MongoDB(uri)
    collector_app = sp.CollectorApp(db, test_config)
    return collector_app.app


app = create_app()
