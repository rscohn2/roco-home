# SPDX-FileCopyrightText: 2020 Robert Cohn
#
# SPDX-License-Identifier: MIT


def test_signal_lookup(building):
    assert (
        building.device_by_name['boiler'].sensor_by_name['bit-4'].signal.name
        == 'oil-burner'
    )
