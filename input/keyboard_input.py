import keyboard


class KeyboardInput:

    def is_pressed(self, key):
        return keyboard.is_pressed(key)
