# SPDX-FileCopyrightText: 2020 Robert Cohn
#
# SPDX-License-Identifier: MIT

import os

from flask import Flask, request

import signalpy as sp

collector = None


class CollectorApp:
    def __init__(self, db, test_config):
        global collector
        store = sp.SignalEventsStore.create(db)
        collector = sp.Collector(store)

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
        @self.app.route('/api/v1/hello')
        def hello():
            return {'message': 'Hello from the collector'}

        @self.app.route('/api/v1/signal_events', methods=['POST'])
        def post_signal_event():
            try:
                collector.record_event(request.form.to_dict())
                return {'message': 'Recorded event'}
            except sp.Collector.EventError as err:
                return {'message': err.message}, 400
