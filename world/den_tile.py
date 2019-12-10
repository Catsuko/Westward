from functools import reduce


class DenTile:

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    # TODO: Push actor into sub-area
    def enter(self, actor, origin):
        door_pos = self.__door_pos()
        return self if origin.at_position(door_pos[0], door_pos[1] - 1) else origin

    def leave(self, actor):
        return self

    # TODO: Update sub-area then return den with updated sub-area
    def update(self, area):
        return area

    def same_position_as(self, other_tile):
        return any([other_tile.at_position(x + self.x, y + self.y) for y in range(self.height) for x in range(self.width)])

    def at_position(self, x, y):
        return self.x <= x < self.x + self.width and self.y <= y < self.y + self.height

    # TODO: Find the edge position in the direction of the offset and get the neighbour past that
    def neighbour(self, area, x_offset, y_offset):
        return self

    def print_to(self, media):
        door_pos = self.__door_pos()
        positions = [(x + self.x, y + self.y) for x in range(self.width) for y in range(self.height)]
        return reduce(lambda m, pos: m.with_character(pos[0], pos[1], '_' if pos == door_pos else '+'), positions, media)

    # TODO: Pass in door directions and use that to determine door position
    def __door_pos(self):
        return round(self.width / 2) + self.x, self.y
