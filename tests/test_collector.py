def test_record_observations(collector, log_server, observations):
    for observation in observations:
        collector.record_observation(observation)
    o = log_server.query('1st-floor-circulator')
    assert len(o) == 7
