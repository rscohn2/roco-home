# SPDX-FileCopyrightText: 2020 Robert Cohn
#
# SPDX-License-Identifier: MIT

"""Manage data for home automation.

"""

import logging

from rocohome.account import Account  # noqa: F401
from rocohome.building import Building  # noqa: F401
from rocohome.device import Device  # noqa: F401
from rocohome.event import SignalEvent  # noqa: F401
from rocohome.event_collector import EventCollector  # noqa: F401
from rocohome.event_log_server import EventLogServer  # noqa: F401
from rocohome.event_store import EventStore  # noqa: F401
from rocohome.sensor import Sensor  # noqa: F401
from rocohome.signal import Signal  # noqa: F401

logger = logging.getLogger(__name__)

fh = logging.FileHandler('rocohome.log')
fh.setLevel(logging.INFO)
logger.addHandler(fh)
