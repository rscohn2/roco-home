# SPDX-FileCopyrightText: 2020 Robert Cohn
#
# SPDX-License-Identifier: MIT

"""Events occur on a device and are recorded in the database.

"""

import logging

import marshmallow as mm

import signalpy as sp


logger = logging.getLogger(__name__)


class Event(sp.Object):
    """Representation of an event.

    """

    pass


class Schema(mm.Schema):
    time = mm.fields.Int()
    val = mm.fields.Float()
    device = sp.Device.Field(data_key='device_guid')

    @mm.post_load
    def make_signal_event(self, data, **kwargs):
        logger.info(f'data: {data}')
        return sp.SignalEvent(**data)

class SignalEvent(Event):

    def __init__(self, time, signal, val, device):
        """Representation of a signal event.

        Parameters
        ----------
        time : int
          UTC timestamp
        signal : :class:`~signalpy.core.signal.Signal`
        val : float
          recorded value
        device : :class:`~signalpy.core.device.Device`
          Device that recorded the event

        """

        self.time = time
        self.signal = signal
        self.val = val
        self.device = device
        
    class DeviceSchema(Schema):
        signal = sp.Signal.DeviceField(data_key='sensor_id')
        
    class StoreSchema(Schema):
        signal = sp.Signal.StoreField(data_key='signal_guid')
