# SPDX-FileCopyrightText: 2020 Robert Cohn
#
# SPDX-License-Identifier: MIT


def test_signal_lookup(project):
    assert (
        project.device_by_name['boiler'].sensor_by_name['bit-4'].signal.name
        == 'oil-burner'
    )
