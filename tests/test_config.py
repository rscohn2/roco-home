from os.path import join

import rocohome as rh

# find test config files relative to the directory containing this
# script


def test_config_load(configs_dir):
    rh.config.load(join(configs_dir, 'test1.yaml'))
