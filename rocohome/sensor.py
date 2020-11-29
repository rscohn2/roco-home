class Sensor:
    """Representation of a sensor.

    A sensor is connected to a device and contains the state of a
    physical entity like a circulator or an oil burner. States are
    represented with floating pointer numbers. An oil burner state can
    be: 0 (off), 1 (on). A state can also be a temperature in
    celsius.

    """

    def __init__(self, sensor_name, sensor_dict, device):
        self.device = device
        self.name = sensor_name
        self.signal = device.building.lookup_signal(sensor_dict['signal'])
