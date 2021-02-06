# SPDX-FileCopyrightText: 2020 Robert Cohn
#
# SPDX-License-Identifier: MIT

import signalpy as sp


class Sensor(sp.Object):
    """Representation of a sensor.

    A sensor is connected to a device and contains the state of a
    physical entity like a circulator or an oil burner. States are
    represented with floating pointer numbers. An oil burner state can
    be: 0 (off), 1 (on). A state can also be a temperature in
    celsius.

    """

    def __init__(self, name, device):
        self.name = name
        self.device = device

    def configure(self, info):
        self.signal = self.device.project.signal_by_name(info['signal'])

    def signals(self, data):
        """Generator for signals and values from sensor event."""

        yield (self.signal, data['val'])


class DS18B20Sensor(Sensor):
    """DS18B20 temperature sensor."""

    pass


class BitsSensor(Sensor):
    """Serial bit chain."""

    def __init__(self, name, device):
        super().__init__(name, device)
        self.bits = {}

    def configure(self, info):
        for bit_name, bit_info in info['bits'].items():
            self.bits[bit_name] = self.device.project.signal_by_name(
                bit_info['signal']
            )

    def signals(self, data):
        assert False


def sensor_factory(type, name, device):
    """Return a sensor based on type."""

    assert type
    if type == 'ds18b20':
        return DS18B20Sensor(name, device)
    elif type == 'bits':
        return BitsSensor(name, device)
