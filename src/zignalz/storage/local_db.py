# SPDX-FileCopyrightText: 2020 Robert Cohn
#
# SPDX-License-Identifier: MIT

import logging
import os
import signal
from abc import ABC, abstractmethod

import zignalz as zz

logger = logging.getLogger(__name__)


class LocalDB(ABC):
    @abstractmethod
    def __init__(self):
        """Starts a local instance."""
        pass

    @abstractmethod
    def down(self):
        """Stops a local instance."""
        pass


class LocalDynamoDB(LocalDB):
    def __init__(self, jar_dir):
        instance = zz.background(
            (
                f'java -Djava.library.path=./DynamoDBLocal_lib'
                f' -jar {jar_dir}/DynamoDBLocal.jar -sharedDb'
            )
        )
        logger.info('Started local instance with pid: %d' % instance.pid)
        self.pid = instance.pid

    def down(self):
        logger.info(f'Killing local instance with pid: {self.pid}')
        os.kill(self.pid, signal.SIGKILL)


class LocalMongoDB(LocalDB):
    def __init__(self, dir):
        zz.shell(f'mongod --dbpath {dir} --fork --logpath {dir}/mongo.log')

    def down(self):
        zz.shell(
            (
                'mongo --nodb --eval '
                '\"connect(\'localhost:27017/admin\').shutdownServer()\"'
            )
        )
