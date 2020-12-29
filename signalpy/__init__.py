# SPDX-FileCopyrightText: 2020 Robert Cohn
#
# SPDX-License-Identifier: MIT

"""Manage data for home automation.

"""

import logging
from abc import ABC

#
# Defined here rather than inside core to avoid circular references.
# Otherwise we are dependent on the way isort sorts imports
#
class Object(ABC):
    """Abstract base class for objects."""

    def __str__(self):
        """Generic string formatter."""

        return str(self.__class__) + ": " + str(self.__dict__)

from signalpy.core.account import *
from signalpy.core.device import *
from signalpy.core.project import *
from signalpy.core.sensor import *
from signalpy.core.signal import *
from signalpy.core.event import *

logger = logging.getLogger(__name__)

fh = logging.FileHandler('signalpy.log')
fh.setLevel(logging.INFO)
logger.addHandler(fh)


