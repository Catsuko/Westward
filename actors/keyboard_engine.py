import keyboard
import time


class KeyboardEngine:

    def __init__(self, key_map, timeout=1):
        self.key_map = key_map
        self.timeout = timeout

    def pick_movement_direction(self, origin, world):
        start = time.time()
        key_pressed = None
        while key_pressed is None and time.time() - start < self.timeout:
            time.sleep(0.001)
            key_pressed = next((key for key in self.key_map.keys() if keyboard.is_pressed(key)), None)
        move_direction = (0,0) if key_pressed is None else self.key_map[key_pressed]
        time.sleep(0.2)
        return move_direction
