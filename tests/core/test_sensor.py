# SPDX-FileCopyrightText: 2020 Robert Cohn
#
# SPDX-License-Identifier: MIT


from zignalz.core import sensor


def test_bits_sensor(test_device, test_signal):
    bits = sensor.sensor_factory('bits', 'bits-sensor', test_device)
    info = {
        'bits': {
            '0': {'signal': test_signal.name},
            '3': {'signal': test_signal.name},
        }
    }
    bits.configure(info)
