from os.path import join

import rocohome as rh


def test_db_reset(db_instance, configs_dir):
    rh.db.admin.reset(join(configs_dir, 'test1.yaml'))
