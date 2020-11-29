def test_sensor_lookup(building):
    assert (
        building.devices['boiler'].sensors['bit-4'].signal.name == 'oil-burner'
    )
