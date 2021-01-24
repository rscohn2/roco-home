# SPDX-FileCopyrightText: 2020 Robert Cohn
#
# SPDX-License-Identifier: MIT

"""Manage data for home automation.

"""

import logging

from signalpy.base import Object  # noqa: F401
from signalpy.core.account import Account  # noqa: F401
from signalpy.core.device import Device  # noqa: F401
from signalpy.core.event import SignalEvent  # noqa: F401
from signalpy.core.project import Project  # noqa: F401
from signalpy.core.sensor import Sensor  # noqa: F401
from signalpy.core.signal import Signal  # noqa: F401
from signalpy.core.util import background  # noqa: F401
from signalpy.core.util import shell  # noqa: F401
from signalpy.services.analyzer.entry_points import Analyzer  # noqa: F401
from signalpy.services.collector.app import CollectorApp  # noqa: F401
from signalpy.services.collector.entry_points import Collector  # noqa: F401
from signalpy.storage.db import DynamoDB  # noqa: F401
from signalpy.storage.db import MongoDB  # noqa: F401
from signalpy.storage.db import SQLite3  # noqa: F401
from signalpy.storage.local_db import LocalDynamoDB  # noqa: F401
from signalpy.storage.local_db import LocalMongoDB  # noqa: F401
from signalpy.storage.store import AccountStore  # noqa: F401
from signalpy.storage.store import DeviceStore  # noqa: F401
from signalpy.storage.store import ProjectStore  # noqa: F401
from signalpy.storage.store import SignalStore  # noqa: F401
from signalpy.storage.store import SignalEventsStore  # noqa: F401

logger = logging.getLogger(__name__)

fh = logging.FileHandler('signalpy.log')
fh.setLevel(logging.INFO)
logger.addHandler(fh)
