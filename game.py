from spaces.area import Area
from spaces.open_space import OpenSpace
from spaces.blocked_space import BlockedSpace
from spaces.tile import Tile
from views.console_view import ConsoleView

# TODO: AreaBuilder
# TODO: Actors and ActorEngines
# TODO: ConsoleView printing in a grid structure

open_space = OpenSpace()
area = Area([
    Tile(0, 0, open_space), Tile(1, 0, open_space),
    Tile(0, 1, open_space), Tile(1, 1, BlockedSpace())
])
area.print_to(ConsoleView())
