# SPDX-FileCopyrightText: 2020 Robert Cohn
#
# SPDX-License-Identifier: MIT


def test_project(home_project):
    assert home_project.signal_by_name('oil burner').name == 'oil burner'
