from rocohome import config


def test_config(home_config):
    assert (
        config.config.sensor_name('ec:fa:bc:c5:b8:90', 'bit-4') == 'oil-burner'
    )
