import logging

from rocohome import config, db

logger = logging.getLogger(__name__)


def add(observations):
    with db.observations.batch_writer() as batch:
        for obs in observations:
            obs['time'] = int(obs['time'])
            obs['sensor_name'] = config.config.sensor_name(
                obs['device_id'], obs['sensor_id']
            )
            logger.info('Inserting %s' % obs)
            batch.put_item(Item=obs)
