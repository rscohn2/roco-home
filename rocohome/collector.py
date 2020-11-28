import logging

logger = logging.getLogger(__name__)


class Collector:
    def __init__(self, observations):
        self.accounts = {}
        self.observations = observations

    def record_observation(self, observation):
        """Insert observation into database."""

        encoded_observation = observation.encode()
        logger.info('recording observation: %s' % encoded_observation)
        self.observations.put_item(Item=observation.encode())
