import os.path
from os.path import join

import rocohome as rh

# find test config files relative to the directory containing this
# script
config_dir = join(os.path.dirname(os.path.realpath(__file__)), 'configs')


def test_config_load():
    rh.config.load(join(config_dir, 'test1.yaml'))
