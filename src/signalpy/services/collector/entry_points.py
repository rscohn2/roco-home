# SPDX-FileCopyrightText: 2020 Robert Cohn
#
# SPDX-License-Identifier: MIT

"""Entry points for Collector service.

"""

import logging

import marshmallow as mm

import signalpy as sp

logger = logging.getLogger(__name__)


class Collector:
    """Interface between collector front-end and persistent storage."""

    class EventError(Exception):
        def __init__(self, message):
            self.message = message

    def __init__(self, stores):
        self.stores = stores
        self.schema = Collector.Schema()

    def _error(self, message):
        logger.error(message)
        raise Collector.EventError(message)

    def record_event(self, device_event):
        """Insert an event into the Event Store.

        Convert from device-generated dict into
        :class:`~signalpy.core.event.Event`. Device input is not
        trusted so it is validated and ignored when there is an error.

        """
        logger.info(f'recording event: {device_event}')

        try:
            d = self.schema.load(device_event)
        except mm.ValidationError as err:
            self._error(
                f'Validation error on device event.'
                f' errors: {err.messages} event:  {device_event}'
            )

        device_guid = d['device_guid']
        try:
            device = sp.Device.by_guid(device_guid)
        except KeyError:
            self._error(f'Unknown device guid: {device_guid}')
        logger.info(f'device: {device}')
        if d['token'] not in device.tokens:
            self._error(f'Invalid token: {device_event}')

        try:
            sensor = device.sensor_by_name[d['sensor_id']]
            signal = sensor.signal
        except KeyError:
            self._error(f'Invalid sensor_id\n  {device_event}')

        if d['event'] == 'sensor':
            se = sp.SignalEvent(d['time'], device, signal, d['val'])
        else:
            self._error(f'Unhandled event type: {device_event}')

        self.stores.signal_events.put(se)

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
