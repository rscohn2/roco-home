# SPDX-FileCopyrightText: 2020 Robert Cohn
#
# SPDX-License-Identifier: MIT

"""Interface between collector front-end and persistent storage.

"""

import logging

import marshmallow as mm

import signalpy as sp

logger = logging.getLogger(__name__)


class EventCollector:
    """Interface between collector front-end and persistent storage."""

    def __init__(self, event_store):
        self.accounts = {}
        self.store = event_store
        self.schema = EventCollector.Schema()

    def record_event(self, device_event):
        """Insert an event into the Event Store.

        Convert from device-generated dict into
        :class:`~signalpy.core.event.Event`. Device input is not
        trusted so it is validated and ignored when there is an error.

        """
        logger.info('recording event: %s' % device_event)

        try:
            d = self.schema.load(device_event)
        except mm.ValidationError as err:
            logger.error(
                'Validation error on device event\n'
                + ' errors: '
                + err.messages
                + '\n  event: '
                + device_event
            )
            return

        device = sp.Device.by_guid[d['device_guid']]
        logger.info(f'device: {device}')
        if d['token'] not in device.tokens:
            # log and ignore when token is not valid
            logger.error(f'Invalid token: {device_event}')
            return

        try:
            sensor = device.sensor_by_name[d['sensor_id']]
            signal = sensor.signal
        except KeyError:
            logger.error(f'Invalid sensor_id\n  {device_event}')
            return

        if d['event'] == 'sensor':
            se = sp.SignalEvent(d['time'], device, signal, d['val'])
        else:
            logger.error(f'Unhandled event type: {device_event}')
            return

        self.store.put(se)

    class Schema(mm.Schema):
        version = mm.fields.Int(validate=mm.validate.Range(min=1, max=1))
        token = mm.fields.Str()
        time = mm.fields.Int()
        device_guid = mm.fields.Str()
        event = mm.fields.Str(validate=mm.validate.OneOf(['sensor']))
        sensor_id = mm.fields.Str(
            validate=mm.validate.OneOf(
                ['bit-1', 'bit-2', 'bit-3', 'bit-4', 'bit-5', 'bit-6', 'bit-7']
            )
        )
        val = mm.fields.Float()
