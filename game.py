from spaces.area import Area
from spaces.open_space import OpenSpace
from spaces.occupied_space import OccupiedSpace
from spaces.tile import Tile
from actors.actor import Actor
from actors.input_engine import InputEngine
from actors.random_engine import RandomEngine
from views.console_view import ConsoleView

npc = Actor(RandomEngine(), '$')
player = Actor(InputEngine({
            'w': (0, -1), 's': (0, 1),
            'a': (-1, 0), 'd': (1, 0)
        }))
open_space = OpenSpace()
# TODO: Introduce area builder to clear this up!
area = Area([
    Tile(0, 0, open_space),
    Tile(1, 0, OccupiedSpace(player)),
    Tile(2, 0, open_space),
    Tile(0, 1, open_space),
    Tile(1, 1, open_space),
    Tile(2, 1, OccupiedSpace(npc))
])

while True:
    area.print_to(ConsoleView())
    area = area.update()
