# SPDX-FileCopyrightText: 2020 Robert Cohn
#
# SPDX-License-Identifier: MIT

import boto3

import rocohome.db.admin as admin  # noqa: F401
import rocohome.db.local as local  # noqa: F401

client_handle = None
resource_handle = None


def client():
    global client_handle
    if not client_handle:
        client_handle = boto3.client(
            'dynamodb', endpoint_url='http://localhost:8000'
        )
    return client_handle


def resource():
    global resource_handle
    if not resource_handle:
        resource_handle = boto3.resource(
            'dynamodb', endpoint_url='http://localhost:8000'
        )
    return resource_handle
