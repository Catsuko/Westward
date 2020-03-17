import pyxel
from views.area_media import AreaMedia


# TODO: Rethink how this shader business will work.
class PyxelAreaView(AreaMedia):

    def __init__(self, renderer, tile_shader, effects_shader, actor_shader):
        self.renderer = renderer
        self.tile_shader = tile_shader
        self.effects_shader = effects_shader
        self.actor_shader = actor_shader

    # TODO: What is the difference between render and draw?!?
    def render(self):
        self.renderer = self.renderer.next()

    def with_actor(self, x, y, key):
        self.renderer.queue_actor(x, y, key[0])
        return self

    def with_effect(self, x, y, effect_description):
        self.renderer.queue_effect(x, y, effect_description)
        return self

    def with_open_space(self, x, y):
        self.renderer.queue_tile(x, y, "ground")
        return self

    def with_area(self, area):
        return area.print_to(self)

    def run(self, width, height):
        pyxel.init(width, height, caption='Westward', scale=3, fps=30)
        pyxel.run(self.__update, self.__draw)

    # TODO: Introduce input polling and create input strategy that reads from the pyxel view.
    def __draw(self):
        self.renderer.draw(self.tile_shader, self.effects_shader, self.actor_shader, pyxel.frame_count)

    def __update(self):
        pass
