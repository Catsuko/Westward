from views.console_view import ConsoleView


class DoorTile:

    def __init__(self, x, y, linked_area):
        self.linked_area = linked_area
        self.x = x
        self.y = y

    def enter(self, actor, origin):
        exit_tile = self.linked_area.tile(self.x, self.y)
        result = exit_tile.enter(actor, origin)
        updated_area = self.linked_area.with_tiles([result])
        actor.survey(updated_area)
        return DoorTile(self.x, self.y, updated_area)

    def leave(self, actor):
        return self

    # TODO: Think more about how the doors will work. Ideally all areas will be updated
    #       And only the player's area will be drawn.
    def update(self, area):
        return []

    # TODO: Refactor duplicated position methods
    def same_position_as(self, other_tile):
        return other_tile.at_position(self.x, self.y)

    def at_position(self, x, y):
        return x == self.x and y == self.y

    def neighbour(self, area, x_offset, y_offset):
        return area.tile(self.x, self.y, x_offset, y_offset)

    def print_to(self, media):
        return media.with_character(self.x, self.y, '_')