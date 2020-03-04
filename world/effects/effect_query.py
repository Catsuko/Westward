from views.area_media import AreaMedia


class EffectQuery(AreaMedia):

    def __init__(self, matcher, matches=[]):
        self.matcher = matcher
        self.matches = matches

    def with_area(self, area):
        return area.print_to(self)

    def with_effect(self, x, y, effect_description):
        match = self.matcher(x, y, effect_description)
        return EffectQuery(self.matcher, self.matches + [(x, y, effect_description)]) if match else self

    def match_count(self):
        return len(self.matches)

    def found(self):
        return self.match_count() > 0

    def found_at(self, x, y):
        return any([match_x is x and match_y is y for match_x, match_y, _ in self.matches])
