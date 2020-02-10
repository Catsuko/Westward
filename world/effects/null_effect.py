class NullEffect:

    def affect(self, area):
        return area.without_effect(self)
