import rocohome as rh


def test_record_events(event_table, events, building):
    collector = rh.Collector(event_table)
    for event in events:
        collector.record_event(event)
    log_server = rh.LogServer(event_table, building)
    o = log_server.query('1st-floor-circulator')
    assert len(o) == 7
