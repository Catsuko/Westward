import time

from actors.actions.action import Action


class InputDrivenAction(Action):

    def __init__(self, key_map, input_strategy, timeout_seconds=1.0):
        self.key_map = key_map
        self.input_strategy = input_strategy
        self.timeout_seconds = timeout_seconds

    def on(self, actor, tile, root):
        start_time = time.time()
        pressed_keys = []
        released_key = None
        while released_key is None and self.__has_time_remaining(start_time):
            time.sleep(0.001)
            released_key = next((key for key in pressed_keys if not self.__test_key(key)), None)
            pressed_keys = [key for key in self.key_map.keys() if self.__test_key(key)]
        if released_key is not None:
            root, action = self.key_map[released_key].on(actor, tile, root)
        return root, self

    def __test_key(self, key):
        return self.input_strategy.is_pressed(key)

    def __has_time_remaining(self, start_time):
        return time.time() - start_time < self.timeout_seconds
