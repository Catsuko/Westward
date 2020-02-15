class Gun:

    def __init__(self, bullet_source, count=0):
        self.bullet_source = bullet_source
        self.count = count

    def update(self):
        print(self.count)
        return self

    # TODO: Potential fix for bullet collision is to make it so the gun has a 1 turn cooldown?
    def use(self, actor, tile, target, root):
        direction = tile.to(target)
        starting_tile = tile.neighbour(*direction, root)
        bullet = self.bullet_source(direction)
        return starting_tile.enter(bullet, starting_tile, root).update_actor(bullet), Gun(self.bullet_source, self.count + 1)



