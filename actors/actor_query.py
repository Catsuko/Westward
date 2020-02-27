class ActorQuery:

    def __init__(self, matcher, matches=[]):
        self.matcher = matcher
        self.matches = matches

    def with_area(self, area):
        return area.print_to(self)

    def with_open_space(self, x, y):
        return self

    def with_wall(self, x, y):
        return self

    def with_actor(self, x, y, key):
        return ActorQuery(self.matcher, self.matches + [(x, y, key)]) if self.matcher(x, y, key) else self

    def with_ledge(self, x, y):
        return self

    def with_door(self, x, y):
        return self

    def match_count(self):
        return len(self.matches)

    def found(self):
        return self.match_count() > 0

    def found_at(self, x, y):
        return any([match_x is x and match_y is y for match_x, match_y, key in self.matches])

