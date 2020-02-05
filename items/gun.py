class Gun:

    def __init__(self, bullet_source):
        self.bullet_source = bullet_source

    def use(self, actor, tile, target, root):
        direction = tile.to(target)
        starting_tile = tile.neighbour(*direction, root)
        bullet = self.bullet_source(direction)
        return starting_tile.enter(bullet, starting_tile, root).update_actor(bullet)



