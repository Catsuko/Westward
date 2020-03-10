from actors.components.component import Component


class Health(Component):

    def __init__(self, current, total, death_action=None):
        self.current = current
        self.total = total
        self.death_action = death_action

    def damage(self, actor, root, tile):
        health_left = self.__change_health(self.current - 1)
        root = actor.replace(self, health_left, root) if health_left.alive() else tile.leave(actor, root)
        return root if self.death_action is None else self.death_action.on(actor, tile.find_in(root), root)

    def heal(self, actor, root, tile):
        return actor.replace(self, self.__change_health(self.current + 1), root)

    def alive(self):
        return self.current > 0

    def print_to(self, x, y, media):
        return media if self.death_action is None else self.death_action.print_to(x, y, media)

    def __change_health(self, current):
        return Health(current, self.total, self.death_action)

