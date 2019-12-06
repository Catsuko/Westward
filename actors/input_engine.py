class InputEngine:

    def __init__(self, movement_map):
        self.movement_map = movement_map

    def pick_movement_direction(self, area, origin):
        key = None
        while key not in self.movement_map.keys():
            key = input()
        return self.movement_map[key]