# SPDX-FileCopyrightText: 2020 Robert Cohn
#
# SPDX-License-Identifier: MIT

from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello, collector2!"
