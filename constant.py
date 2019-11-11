class Constant(object):
    def __init__(self, name):
        self.name = name

    @property
    def name(self, name):
        self.name = name

    @property
    def value(self, value, name):
        self.value = value
