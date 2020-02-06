from world.bounds import Bounds


class RenderedArea(Bounds):

    def __init__(self, area, media):
        self.area = area
        self.media = media

    def update(self, root=None):
        self.media.with_area(self.area).render()
        return RenderedArea(self.area.update(root), self.media)

    def update_actor(self, actor, root):
        return self.area.update_actor(actor, root)

    def replace_actor(self, actor, root):
        return self.area.replace_actor(actor, root)

    def with_area(self, area):
        return RenderedArea(self.area.with_area(area), self.media)

    def tile(self, x, y):
        return self.area.tile(x, y)

    def surrounds(self, x, y):
        return self.area.surrounds(x, y)

    def enclosed_by(self, bounds):
        return self.area.enclosed_by(bounds)

    def print_to(self, media):
        return self.area.print_to(media)
