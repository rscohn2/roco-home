# SPDX-FileCopyrightText: 2020 Robert Cohn
#
# SPDX-License-Identifier: MIT

"""Manage data for home automation.

"""

import logging

from zignalz.base import Object  # noqa: F401
from zignalz.core.account import Account  # noqa: F401
from zignalz.core.auth import make_guid, make_token  # noqa: F401
from zignalz.core.device import Device  # noqa: F401
from zignalz.core.event import SignalEvent  # noqa: F401
from zignalz.core.project import Project  # noqa: F401
from zignalz.core.sensor import Sensor  # noqa: F401
from zignalz.core.sensor import sensor_factory  # noqa: F401
from zignalz.core.signal import Signal  # noqa: F401
from zignalz.core.util import background  # noqa: F401
from zignalz.core.util import shell  # noqa: F401
from zignalz.services.analyzer.entry_points import Analyzer  # noqa: F401
from zignalz.services.collector.app import CollectorApp  # noqa: F401
from zignalz.services.collector.entry_points import Collector  # noqa: F401
from zignalz.storage.db import DynamoDB  # noqa: F401
from zignalz.storage.db import MongoDB  # noqa: F401
from zignalz.storage.db import SQLite3  # noqa: F401
from zignalz.storage.local_db import LocalDynamoDB  # noqa: F401
from zignalz.storage.local_db import LocalMongoDB  # noqa: F401
from zignalz.storage.store import Stores  # noqa: F401

logger = logging.getLogger(__name__)

fh = logging.FileHandler('zignalz.log')
fh.setLevel(logging.INFO)
logger.addHandler(fh)
