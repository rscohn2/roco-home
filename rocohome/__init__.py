# SPDX-FileCopyrightText: 2020 Robert Cohn
#
# SPDX-License-Identifier: MIT

"""Manage data for home automation.

"""

import logging

logger = logging.getLogger(__name__)

fh = logging.FileHandler('rocohome.log')
fh.setLevel(logging.INFO)
logger.addHandler(fh)
