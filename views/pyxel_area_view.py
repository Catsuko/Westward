import pyxel
from views.area_media import AreaMedia

class PyxelAreaView(AreaMedia):

    def __init__(self, width, height):
        pyxel.init(width, height, caption='Westward', scale=3, fps=30)
        pyxel.run(self.update, self.render)

    def update(self):
        pass

    def render(self):
        pyxel.text(0, 0, "How the fuck will this\nbe immutable!", pyxel.frame_count % 16)

