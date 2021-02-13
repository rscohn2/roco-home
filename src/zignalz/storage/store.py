# SPDX-FileCopyrightText: 2020 Robert Cohn
#
# SPDX-License-Identifier: MIT

"""Persistent storage for objects.

"""

import logging
from abc import ABC, abstractmethod

import marshmallow as mm

import zignalz as zz

logger = logging.getLogger(__name__)


class Stores:
    def __init__(self, db):
        self.signal_events = SignalEventsStore.create(db)
        self.account = AccountStore.create(db)
        self.project = ProjectStore.create(db)
        self.signal = SignalStore.create(db)
        self.device = DeviceStore.create(db)


class Store(ABC):
    """Base class for persistent storage of objects.

    Parameters
    ----------
    db : :class:`~zignalz.storage.db.DB`
      Handle to DB
    name : str
      Name of store

    """

    def table(self, db, name):
        self.table = db.Table(db, name)

    @abstractmethod
    def create(db):
        """Create the persistent object in the db."""
        pass

    @abstractmethod
    def put(self, object):
        """Save an object.

        Parameters
        ----------
        object : object
          object with to_store method that returns a dict

        """
        pass

    @abstractmethod
    def query(self):
        """Returns list of objects matching filter."""
        pass


class SignalEventsStore(Store):
    """Stores events from devices."""

    table_name = 'SignalEvents'

    table_info = {
        'sqlite': {
            'schema': [
                ('signal_guid', 'text'),
                ('time', 'integer'),
                ('device_guid', 'text'),
                ('val', 'real'),
            ]
        },
        'dynamodb': {
            'KeySchema': [
                {'AttributeName': 'signal_guid', 'KeyType': 'HASH'},
                {'AttributeName': 'time', 'KeyType': 'RANGE'},
            ],
            'AttributeDefinitions': [
                {'AttributeName': 'signal_guid', 'AttributeType': 'S'},
                {'AttributeName': 'time', 'AttributeType': 'N'},
            ],
        },
    }

    class Schema(mm.Schema):
        """Schema for signal events."""

        time = mm.fields.Int()
        signal_guid = mm.fields.UUID()
        device_guid = mm.fields.UUID()
        val = mm.fields.Float()

    def __init__(self, db):
        self.table(db, SignalEventsStore.table_name)
        self.schema = SignalEventsStore.Schema()

    def create(db):
        db.create_table(
            SignalEventsStore.table_name, SignalEventsStore.table_info
        )
        return SignalEventsStore(db)

    def put(self, se):
        so = self.schema.dump(
            {
                'time': se.time,
                'signal_guid': se.signal.guid,
                'device_guid': se.device.guid,
                'val': se.val,
            }
        )
        self.table.put(so)

    def query(self):
        for q in self.table.query():
            d = dict(q)
            logger.info(f'SignalEventStore query result: {d}')
            s_d = self.schema.load(d)
            yield zz.SignalEvent(
                time=s_d['time'],
                device=zz.Device.by_guid(s_d['device_guid']),
                signal=zz.Signal.by_guid(s_d['signal_guid']),
                val=s_d['val'],
            )


class AccountStore(Store):
    """Stores accounts."""

    table_name = 'Accounts'

    table_info = {
        'sqlite': {
            'schema': [
                ('guid', 'text'),
                ('name', 'text'),
                ('token', 'text'),
            ]
        },
        'dynamodb': {
            'KeySchema': [
                {'AttributeName': 'guid', 'KeyType': 'HASH'},
            ],
            'AttributeDefinitions': [
                {'AttributeName': 'guid', 'AttributeType': 'S'},
            ],
        },
    }

    class Schema(mm.Schema):
        """Schema for account store."""

        guid = mm.fields.UUID()
        name = mm.fields.Str()
        token = mm.fields.Str()

        class Meta:
            unknown = mm.EXCLUDE

    def __init__(self, db):
        self.table(db, AccountStore.table_name)
        self.schema = AccountStore.Schema()

    def create(db):
        db.create_table(AccountStore.table_name, AccountStore.table_info)
        return AccountStore(db)

    def put(self, o):
        d = self.schema.dump(
            {
                'guid': o.guid,
                'name': o.name,
                'token': o.token,
            }
        )
        self.table.put(d)

    def query(self):
        for q in self.table.query():
            d = dict(q)
            logger.info(f'AccountStore query result: {d}')
            s_d = self.schema.load(d)
            yield zz.Account(
                guid=s_d['guid'], name=s_d['name'], token=s_d['token']
            )


class ProjectStore(Store):
    """Stores projects."""

    table_name = 'Projects'

    table_info = {
        'sqlite': {
            'schema': [
                ('guid', 'text'),
                ('name', 'text'),
                ('account_guid', 'text'),
            ]
        },
        'dynamodb': {
            'KeySchema': [
                {'AttributeName': 'guid', 'KeyType': 'HASH'},
            ],
            'AttributeDefinitions': [
                {'AttributeName': 'guid', 'AttributeType': 'S'},
            ],
        },
    }

    class Schema(mm.Schema):
        """Schema for project store."""

        guid = mm.fields.UUID()
        name = mm.fields.Str()
        account_guid = mm.fields.UUID()
        devices = mm.fields.List(mm.fields.UUID())

        class Meta:
            unknown = mm.EXCLUDE

    def __init__(self, db):
        self.table(db, ProjectStore.table_name)
        self.schema = ProjectStore.Schema()

    def create(db):
        db.create_table(ProjectStore.table_name, ProjectStore.table_info)
        return ProjectStore(db)

    def put(self, o):
        d = self.schema.dump(
            {
                'guid': o.guid,
                'name': o.name,
                'account_guid': o.account.guid,
            }
        )
        self.table.put(d)

    def query(self):
        for q in self.table.query():
            d = dict(q)
            logger.info(f'ProjectStore query result: {d}')
            s_d = self.schema.load(d)
            p = zz.Project.by_guid(s_d['guid'])
            if p is None:
                account = zz.Account.by_guid(s_d['account_guid'])
                p = zz.Project(
                    guid=s_d['guid'], name=s_d['name'], account=account
                )
            yield p


class SignalStore(Store):
    """Stores signals."""

    table_name = 'Signals'

    table_info = {
        'sqlite': {
            'schema': [
                ('guid', 'text'),
                ('name', 'text'),
                ('project_guid', 'text'),
            ]
        },
        'dynamodb': {
            'KeySchema': [
                {'AttributeName': 'guid', 'KeyType': 'HASH'},
            ],
            'AttributeDefinitions': [
                {'AttributeName': 'guid', 'AttributeType': 'S'},
            ],
        },
    }

    class Schema(mm.Schema):
        """Schema for project store."""

        guid = mm.fields.UUID()
        name = mm.fields.Str()
        project_guid = mm.fields.UUID()

        class Meta:
            unknown = mm.EXCLUDE

    def __init__(self, db):
        self.table(db, SignalStore.table_name)
        self.schema = SignalStore.Schema()

    def create(db):
        db.create_table(SignalStore.table_name, SignalStore.table_info)
        return SignalStore(db)

    def put(self, o):
        d = self.schema.dump(
            {
                'guid': o.guid,
                'name': o.name,
                'project_guid': o.project.guid,
            }
        )
        self.table.put(d)

    def query(self):
        for q in self.table.query():
            d = dict(q)
            logger.info(f'SignalStore query result: {d}')
            s_d = self.schema.load(d)
            project = zz.Project.by_guid(s_d['project_guid'])
            yield zz.Signal(
                guid=s_d['guid'], name=s_d['name'], project=project
            )


class DeviceStore(Store):
    """Stores devices."""

    table_name = 'Devices'

    table_info = {
        'sqlite': {
            'schema': [
                ('guid', 'text'),
                ('name', 'text'),
                ('project_guid', 'text'),
            ]
        },
        'dynamodb': {
            'KeySchema': [
                {'AttributeName': 'guid', 'KeyType': 'HASH'},
            ],
            'AttributeDefinitions': [
                {'AttributeName': 'guid', 'AttributeType': 'S'},
            ],
        },
    }

    class Schema(mm.Schema):
        """Schema for project store."""

        guid = mm.fields.UUID()
        name = mm.fields.Str()
        project_guid = mm.fields.UUID()

        class Meta:
            unknown = mm.EXCLUDE

    def __init__(self, db):
        self.table(db, DeviceStore.table_name)
        self.schema = DeviceStore.Schema()

    def create(db):
        db.create_table(DeviceStore.table_name, DeviceStore.table_info)
        return DeviceStore(db)

    def put(self, o):
        d = self.schema.dump(
            {
                'guid': o.guid,
                'name': o.name,
                'project_guid': o.project.guid,
            }
        )
        self.table.put(d)

    def query(self):
        for q in self.table.query():
            d = dict(q)
            logger.info(f'DeviceStore query result: {d}')
            s_d = self.schema.load(d)
            project = zz.Project.by_guid(s_d['project_guid'])
            yield zz.Signal(
                guid=s_d['guid'], name=s_d['name'], project=project
            )
