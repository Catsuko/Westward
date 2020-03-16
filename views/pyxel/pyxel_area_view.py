import pyxel
from views.area_media import AreaMedia


# TODO: Rethink how this shader business will work.
class PyxelAreaView(AreaMedia):

    def __init__(self, tile_view, actor_view, effect_view):
        self.tile_view = tile_view
        self.actor_view = actor_view
        self.effect_view = effect_view

    # TODO: What is the difference between render and draw?!?
    def render(self):
        self.tile_view = self.tile_view.next()
        self.actor_view = self.actor_view.next()
        self.effect_view = self.effect_view.next()

    def with_actor(self, x, y, key):
        self.actor_view.add(x, y, key[0])
        return self

    def with_effect(self, x, y, effect_description):
        self.effect_view.add(x, y, effect_description)
        return self

    def with_open_space(self, x, y):
        self.tile_view.add(x, y, 'ground')
        return self

    def with_area(self, area):
        return area.print_to(self)

    def run(self, width, height):
        pyxel.init(width, height, caption='Westward', scale=3, fps=30)
        pyxel.run(self.__update, self.__draw)

    # TODO: Introduce input polling and create input strategy that reads from the pyxel view.
    def __draw(self):
        pyxel.cls(col=0)
        time = pyxel.frame_count
        self.tile_view.draw(time)
        self.effect_view.draw(time)
        self.actor_view.draw(time)

    def __update(self):
        pass
