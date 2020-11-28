from boto3.dynamodb.conditions import Key


class LogServer:
    def __init__(self, table):
        self.table = table

    def query(self, observed=None):
        response = self.table.query(
            KeyConditionExpression=Key('observed_id').eq(observed)
        )
        return response['Items']
