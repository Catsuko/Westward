class Gun:

    def __init__(self, bullet_source, reload_counter=0, reload_duration=2):
        self.bullet_source = bullet_source
        self.reload_counter = reload_counter
        self.reload_duration = reload_duration

    def update(self):
        return self if self.reload_counter is 0 else self.__tick_reload_counter()

    def use(self, actor, tile, target, root):
        if self.reload_counter > 0:
            return root, self
        direction = tile.to(target)
        starting_tile = tile.neighbour(*direction, root)
        bullet = self.bullet_source(direction)
        root = starting_tile.enter(bullet, starting_tile, root).update_actor(bullet, self.__update_bullet)
        return root, Gun(self.bullet_source, self.reload_duration, self.reload_duration)

    def __update_bullet(self, bullet, tile, root):
        return bullet.act(tile, root)

    def __tick_reload_counter(self):
        return Gun(self.bullet_source, self.reload_counter - 1, self.reload_duration)
