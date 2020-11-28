class Sensor:
    """Representation of a sensor.

    A sensor is connected to a device and contains the state of a
    physical entity like a circulator or an oil burner. States are
    represented with floating pointer numbers. An oil burner state can
    be: 0 (off), 1 (on). A state can also be a temperature in
    celsius.

    Attributes:
       id -- name suitable for lookup, does not change

    """

    def __init__(self, sensor_id, device, sensor_observes):
        self.id = sensor_id
        self.device = device
        self.observed_id = sensor_observes
