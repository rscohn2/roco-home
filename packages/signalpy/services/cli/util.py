# SPDX-FileCopyrightText: 2020 Robert Cohn
#
# SPDX-License-Identifier: MIT

import logging
from subprocess import Popen, run

from signalpy.services import cli

logger = logging.getLogger(__name__)


def shell(cmd):
    logger.info(f'shell: {cmd}')
    if cli.args.dry_run:
        return
    run(cmd, shell=True)


def background(cmd):
    logger.info(f'backgroound: {cmd}')
    if cli.args.dry_run:
        return
    return Popen(cmd.split(' '))
