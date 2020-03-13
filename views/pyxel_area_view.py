import pyxel
from views.area_media import AreaMedia


class PyxelAreaView(AreaMedia):

    # TODO: Extract into smaller components with cohesive responsibilities
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
        self.resolution = range(8)

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

    # TODO: Introduce input polling and create input strategy that reads from the pyxel view.
    def __draw(self):
        pyxel.cls(col=0)
        for tile in self.tiles:
            self.__draw_tile(*tile)
        for effect in self.effects:
            self.__draw_effect(*effect)
        for actor in self.actors:
            self.__draw_actor(*actor)

    # TODO: Calculate offsets and resolution based on window size.
    def __draw_tile(self, x, y, tile):
        for px in self.resolution:
            for py in self.resolution:
                pyxel.pset(12 + px + x * 8, 12 + py + y * 8, self.env.color(tile))

    def __draw_effect(self, x, y, effect):
        if pyxel.frame_count % 8 <= 4:
            for px in self.resolution:
                for py in self.resolution:
                    pyxel.pset(12 + px + x * 8, 12 + py + y * 8, self.env.color(effect))

    def __draw_actor(self, x, y, actor):
        for px in self.resolution:
            for py in self.resolution:
                pyxel.pset(12 + px + x * 8, 12 + py + y * 8, self.env.color(actor[0]))

    def __update(self):
        pass
