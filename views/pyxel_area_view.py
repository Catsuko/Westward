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
        self.__clear_imprints()
        return area.print_to(self)

    def run(self):
        pyxel.init(self.width, self.height, caption='Westward', scale=3, fps=30)
        pyxel.run(self.__update, self.__draw)

    def __clear_imprints(self):
        self.actors.clear()
        self.effects.clear()
        self.tiles.clear()

    # TODO: Cull outside of viewport, bring back the cameras?
    # TODO: Increase size of tiles!
    # TODO: Introduce input polling and create input strategy that reads from the pyxel view.
    def __draw(self):
        pyxel.cls(col=0)
        for tile in self.tiles.copy():
            self.__draw_tile(*tile)
        for effect in self.effects.copy():
            self.__draw_effect(*effect)
        for actor in self.actors.copy():
            self.__draw_actor(*actor)

    def __draw_tile(self, x, y, tile):
        pyxel.pset(x + 20, y + 20, self.env.color(tile))

    def __draw_effect(self, x, y, effect):
        if pyxel.frame_count % 8 <= 4:
            pyxel.pset(x + 20, y + 20, self.env.color(effect))

    def __draw_actor(self, x, y, actor):
        pyxel.pset(x + 20, y + 20, self.env.color(actor[0]))

    def __update(self):
        pass
