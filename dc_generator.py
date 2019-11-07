class dc_generator(object):
    def __init__(self):
        self.rotation_speed_in_min = 0
        self.rotation_speed_in_sec = 0
        self.pole = 0
        self.frequency = 0

    def get_frequency(self):
        self.frequency = self.rotation_speed_in_min * self.pole / 120
        return self.frequency

    def get_rotation_speed_in_sec(self):
        self.rotation_speed_in_sec = self.rotation_speed_in_min / 60
        return self.rotation_speed_in_sec

    def get_pole(self):
        self.pole = self.frequency * 120 / self.rotation_speed_in_min
        return self.pole
