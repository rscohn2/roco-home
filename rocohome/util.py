import logging
from subprocess import Popen, run

from rocohome import cli

logger = logging.getLogger(__name__)


def shell(cmd):
    logger.info('shell: %s' % cmd)
    if cli.args.dry_run:
        return
    run(cmd, shell=True)


def background(cmd):
    logger.info('background: %s' % cmd)
    if cli.args.dry_run:
        return
    return Popen(cmd.split(' '))
