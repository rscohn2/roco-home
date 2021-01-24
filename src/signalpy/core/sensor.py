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

