class NullEffect:

    def affect(self, area):
        return area.without_effect(self)

    def print_to(self, media):
        return media
