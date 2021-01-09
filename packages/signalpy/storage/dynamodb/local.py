# SPDX-FileCopyrightText: 2020 Robert Cohn
#
# SPDX-License-Identifier: MIT

import logging
import os
import signal

from signalpy.services import cli
from signalpy.services.cli.util import background

logger = logging.getLogger(__name__)


def up():
    instance = background(
        (
            f'java -Djava.library.path=./DynamoDBLocal_lib'
            f' -jar {cli.args.jar_dir}/DynamoDBLocal.jar -sharedDb'
        )
    )
    logger.info('Started local instance with pid: %d' % instance.pid)
    return instance.pid


def down(pid):
    logger.info('Killing local instance with pid: %d' % pid)
    os.kill(pid, signal.SIGKILL)
