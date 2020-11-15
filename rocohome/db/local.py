import logging
import os
import signal

from rocohome import cli
from rocohome.util import background

logger = logging.getLogger(__name__)


def up():
    instance = background(
        (
            'java -Djava.library.path=./DynamoDBLocal_lib'
            ' -jar %s/DynamoDBLocal.jar -sharedDb'
        )
        % cli.args.jar_dir
    )
    logger.info('Started local instance with pid: %d' % instance.pid)
    return instance.pid


def down(pid):
    logger.info('Killing local instance with pid: %d' % pid)
    os.kill(pid, signal.SIGKILL)
