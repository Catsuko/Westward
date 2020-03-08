import pyxel

class PyxelInput:

    def __init__(self):
        self.key_template = 'KEY_%s'

    def is_pressed(self, key):
        return pyxel.btn(getattr(pyxel, self.key_template % key.upper()))
