# SPDX-FileCopyrightText: 2020 Robert Cohn
#
# SPDX-License-Identifier: MIT

"""Entry points for Collector service.

"""

import logging

import marshmallow as mm

import zignalz as zz

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
        :class:`~zignalz.core.event.Event`. Device input is not
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

        token = d['token']
        try:
            device = zz.Device.by_token(token)
        except KeyError:
            self._error(f'Unknown device token')
        logger.info(f'device: {device}')
        try:
            sensor = device.sensor_by_name(d['sensor_id'])
        except KeyError:
            self._error(f'Invalid sensor_id\n  {device_event}')

        # a single sensor reading may generate multiple signal events
        for (signal, val) in sensor.signals(d):
            se = zz.SignalEvent(d['time'], device, signal, val)
            self.stores.signal_events.put(se)

    class Schema(mm.Schema):
        version = mm.fields.Int(validate=mm.validate.Range(min=1, max=1))
        token = mm.fields.Str()
        time = mm.fields.Int()
        device_guid = mm.fields.Str()
        event = mm.fields.Str(validate=mm.validate.OneOf(['sensor']))
        sensor_id = mm.fields.Str()
        val = mm.fields.Str()
        prev_val = mm.fields.Str()
