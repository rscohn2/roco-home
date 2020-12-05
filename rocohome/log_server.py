# SPDX-FileCopyrightText: 2020 Robert Cohn
#
# SPDX-License-Identifier: MIT

from boto3.dynamodb.conditions import Key


class LogServer:
    def __init__(self, table, building):
        self.table = table
        self.building = building

    def query(self, signal_name):
        self.building.signals
        response = self.table.query(
            KeyConditionExpression=Key('signal_guid').eq(
                self.building.signals[signal_name].guid
            )
        )
        return response['Items']
