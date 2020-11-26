from boto3.dynamodb.conditions import Key

from rocohome import db
from rocohome.db import recorder


def test_record_observations(short_observations, home_config, reset_db):
    recorder.add(short_observations)
    resp = db.observations.query(
        KeyConditionExpression=Key('sensor_name').eq('1st-floor-circulator')
    )
    assert len(resp['Items']) == 7
