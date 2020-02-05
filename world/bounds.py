class Bounds:

    def enclosed_by(self, bounds):
        pass

    def surrounds(self, x, y):
        pass

    def __eq__(self, other):
        return isinstance(other, Bounds) and self.enclosed_by(other) and other.enclosed_by(self)
