class RenderedArea:

    def __init__(self, area, media):
        self.area = area
        self.media = media

    def update(self, root=None):
        self.media.with_area(self.area).render()
        return RenderedArea(self.area.update(root), self.media)

    def update_actor(self, actor, root):
        return self.area.update_actor(actor, root)

    def with_tile(self, tile):
        return RenderedArea(self.area.with_tile(tile), self.media)

    def tile(self, x, y):
        return RenderedArea(self.area.tile(x, y), self.media)

    def surrounds(self, x, y):
        return self.area.surrounds(x, y)

    def enclosed_by(self, area):
        return self.area.enclosed_by(area)

    def print_to(self, media):
        return self.area.print_to(media)
