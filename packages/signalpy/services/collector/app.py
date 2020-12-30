# SPDX-FileCopyrightText: 2020 Robert Cohn
#
# SPDX-License-Identifier: MIT

import os

from flask import Flask

import signalpy as sp


class CollectorApp:
    def __init__(self, db, test_config):
        store = sp.SignalEventsStore.create(db)
        self.collector = sp.Collector(store)

        # create and configure the app
        self.app = Flask(__name__, instance_relative_config=True)
        self.app.config.from_mapping(
            SECRET_KEY='dev',
            DATABASE=os.path.join(self.app.instance_path, 'flaskr.sqlite'),
        )

        if test_config is None:
            # load the instance config, if it exists, when not testing
            self.app.config.from_pyfile('config.py', silent=True)
        else:
            # load the test config if passed in
            self.app.config.from_mapping(test_config)

        # ensure the instance folder exists
        try:
            os.makedirs(self.app.instance_path)
        except OSError:
            pass

        # a simple page that says hello
        @self.app.route('/hello')
        def hello():
            return 'Hello, World!'
