import pyxel
from views.area_media import AreaMedia


class PyxelAreaView(AreaMedia):

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.actors = {}

    def update(self):
        pass

    def render(self):
        pass

    def with_actor(self, x, y, key):
        self.actors[key] = (x, y, key[0])
        return self

    def with_area(self, area):
        self.actors.clear()
        return area.print_to(self)

    def draw(self):
        pyxel.cls(col=1)
        pyxel.text(0, 0, "How the fuck will this\nbe immutable!", pyxel.frame_count % 16)
        for key in self.actors.keys():
            x, y, actor = self.actors[key]
            pyxel.pset(x + 20, y + 20, ord(actor) % 16)

    def run(self):
        pyxel.init(self.width, self.height, caption='Westward', scale=3, fps=30)
        pyxel.run(self.update, self.draw)

