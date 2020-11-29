class Signal:
    """Representation of a signal."""

    def __init__(self, signal_name, signal_dict, building):
        self.building = building
        self.name = signal_name
        self.guid = signal_dict['guid']
