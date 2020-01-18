import keyboard
import time


class KeyboardDrivenAction:

    def __init__(self, key_map, timeout_seconds=2.0):
        self.key_map = key_map
        self.timeout_seconds = timeout_seconds

    def on(self, actor, tile, root):
        start_time = time.time()
        pressed_keys = []
        released_key = None
        while released_key is None and self.__has_time_remaining(start_time):
            time.sleep(0.001)
            released_key = next((key for key in pressed_keys if not keyboard.is_pressed(key)), None)
            pressed_keys = [key for key in self.key_map.keys() if keyboard.is_pressed(key)]
        return root if released_key is None else self.key_map[released_key].on(actor, tile, root)

    def __has_time_remaining(self, start_time):
        return time.time() - start_time < self.timeout_seconds
