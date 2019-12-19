import keyboard
import time


class KeyboardEngine:

    def __init__(self, key_map, timeout=0.75, time_step=0.1):
        self.key_map = key_map
        self.timeout = timeout
        self.time_step = time_step

    def pick_movement_direction(self, origin, world):
        key_pressed = None
        remaining_timeout = self.timeout
        time_step = remaining_timeout * max(1.0, self.time_step)
        while key_pressed is None and remaining_timeout > 0:
            time.sleep(time_step)
            remaining_timeout = remaining_timeout - time_step
            key_pressed = next((key for key in self.key_map.keys() if keyboard.is_pressed(key)), None)
        time.sleep(remaining_timeout)
        return (0,0) if key_pressed is None else self.key_map[key_pressed]
