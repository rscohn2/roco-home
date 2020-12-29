# SPDX-FileCopyrightText: 2020 Robert Cohn
#
# SPDX-License-Identifier: MIT

"""Manage data for home automation.

"""

import logging

import signalpy.storage.dynamodb as dynamodb  # noqa: F401
from signalpy.base import Object  # noqa: F401
from signalpy.core.account import Account  # noqa: F401
from signalpy.core.device import Device  # noqa: F401
from signalpy.core.event import SignalEvent  # noqa: F401
from signalpy.core.project import Project  # noqa: F401
from signalpy.core.sensor import Sensor  # noqa: F401
from signalpy.core.signal import Signal  # noqa: F401
from signalpy.services.event_collector import EventCollector  # noqa: F401
from signalpy.services.event_log_server import EventLogServer  # noqa: F401
from signalpy.storage.db import DynamoDB  # noqa: F401
from signalpy.storage.db import SQLite3  # noqa: F401
from signalpy.storage.store import SignalEventsStore  # noqa: F401

logger = logging.getLogger(__name__)

fh = logging.FileHandler('signalpy.log')
fh.setLevel(logging.INFO)
logger.addHandler(fh)
