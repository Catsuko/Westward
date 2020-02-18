class Gun:

    def __init__(self, bullet_source, count=0):
        self.bullet_source = bullet_source
        self.count = count

    def update(self):
        return self

    # TODO: Potential fix for bullet collision is to make it so the gun has a 1 turn cooldown?
    def use(self, actor, tile, target, root):
        direction = tile.to(target)
        starting_tile = tile.neighbour(*direction, root)
        bullet = self.bullet_source(direction)
        root = starting_tile.enter(bullet, starting_tile, root).update_actor(bullet, self.__update_bullet)
        return root, Gun(self.bullet_source, self.count + 1)

    def __update_bullet(self, bullet, tile, root):
        return bullet.act(tile, root)




