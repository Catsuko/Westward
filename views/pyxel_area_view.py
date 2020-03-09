import pyxel
from views.area_media import AreaMedia


class PyxelAreaView(AreaMedia):

    def __init__(self, width, height, env):
        self.width = width
        self.height = height
        self.env = env
        self.actors = set()
        self.tiles = set()
        self.effects = set()

    def render(self):
        pass

    def with_actor(self, x, y, key):
        self.actors.add((x, y, key[0]))
        return self

    def with_effect(self, x, y, effect_description):
        self.effects.add((x, y, effect_description))
        return self

    def with_open_space(self, x, y):
        self.tiles.add((x, y, "ground"))
        return self

    def with_area(self, area):
        self.actors.clear()
        return area.print_to(self)

    def run(self):
        pyxel.init(self.width, self.height, caption='Westward', scale=3, fps=30)
        pyxel.run(self.__update, self.__draw)

    def __clear_imprints(self):
        self.actors.clear()
        self.effects.clear()
        self.tiles.clear()

    # TODO: Cull outside of viewport, bring back the cameras?
    # TODO: Find out what is going wrong with the dynamite.
    # TODO: Increase size of tiles!
    # TODO: Introduce input polling and create input strategy that reads from the pyxel view.
    def __draw(self):
        pyxel.cls(col=0)
        offset = 20
        for x, y, tile in self.tiles:
            pyxel.pset(x + offset, y + offset, self.env.color(tile))
        for x, y, effect in self.effects:
            pyxel.pset(x + offset, y + offset, self.env.color(effect))
        for x, y, actor in self.actors:
            pyxel.pset(x + offset, y + offset, self.env.color(actor[0]))

    def __update(self):
        pass
