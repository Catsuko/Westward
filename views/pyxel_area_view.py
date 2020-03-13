import pyxel
from views.area_media import AreaMedia


class PyxelAreaView(AreaMedia):

    def __init__(self, width, height, env):
        self.width = width
        self.height = height
        self.env = env
        self.next_actors = set()
        self.next_tiles = set()
        self.next_effects = set()
        self.actors = set()
        self.tiles = set()
        self.effects = set()

    def render(self):
        self.actors = self.next_actors
        self.tiles = self.next_tiles
        self.effects = self.next_effects
        self.next_actors = set()
        self.next_tiles = set()
        self.next_effects = set()

    def with_actor(self, x, y, key):
        self.next_actors.add((x, y, key[0]))
        return self

    def with_effect(self, x, y, effect_description):
        self.next_effects.add((x, y, effect_description))
        return self

    def with_open_space(self, x, y):
        self.next_tiles.add((x, y, "ground"))
        return self

    def with_area(self, area):
        return area.print_to(self)

    def run(self):
        pyxel.init(self.width, self.height, caption='Westward', scale=3, fps=30)
        pyxel.run(self.__update, self.__draw)

    # TODO: Increase size of tiles!
    # TODO: Introduce input polling and create input strategy that reads from the pyxel view.
    def __draw(self):
        pyxel.cls(col=0)
        for tile in self.tiles:
            self.__draw_tile(*tile)
        for effect in self.effects:
            self.__draw_effect(*effect)
        for actor in self.actors:
            self.__draw_actor(*actor)

    def __draw_tile(self, x, y, tile):
        pyxel.pset(x, y, self.env.color(tile))

    def __draw_effect(self, x, y, effect):
        if pyxel.frame_count % 8 <= 4:
            pyxel.pset(x, y, self.env.color(effect))

    def __draw_actor(self, x, y, actor):
        pyxel.pset(x, y, self.env.color(actor[0]))

    def __update(self):
        pass
