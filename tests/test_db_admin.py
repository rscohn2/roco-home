import rocohome as rh


def test_db_reset(db_instance):
    rh.db.admin.reset()
