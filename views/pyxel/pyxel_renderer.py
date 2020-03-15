import pyxel



class PyxelRenderer:

    def __init__(self, h_margin=0, v_margin=0, h_offset=0, v_offset=0):
        self.h_margin = h_margin
        self.v_margin = v_margin
        self.h_offset = h_offset
        self.v_offset = v_offset

    def draw(self, x, y, color):
        pyxel.pset(x + self.h_margin, y + self.v_margin, color)

