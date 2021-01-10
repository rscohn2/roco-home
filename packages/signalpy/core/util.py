# SPDX-FileCopyrightText: 2020 Robert Cohn
#
# SPDX-License-Identifier: MIT

import logging
from subprocess import Popen, run

logger = logging.getLogger(__name__)


def shell(cmd, dry_run=False, check=True):
    logger.info(f'shell: {cmd}')
    if dry_run:
        return
    run(cmd, shell=True, check=check)


def background(cmd, dry_run=False):
    logger.info(f'background: {cmd}')
    if dry_run:
        return
    return Popen(cmd.split(' '))
