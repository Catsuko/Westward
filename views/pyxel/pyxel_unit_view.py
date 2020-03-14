class PyxelUnitView:

    def __init__(self, draw_strategy, rendered_units=set()):
        self.draw_strategy = draw_strategy
        self.rendered_units = rendered_units
        self.next_units = set()

    def add(self, x, y, unit_description):
        self.next_units.add((x, y, unit_description))

    def next(self):
        return PyxelUnitView(self.draw_strategy, self.next_units)

    def draw(self, time):
        for unit_description in self.rendered_units:
            self.draw_strategy.draw(*unit_description, time)
