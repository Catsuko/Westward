from spaces.area import Area
from spaces.open_tile import OpenTile
from spaces.wall_tile import WallTile
from views.console_view import ConsoleView

area = Area([
    OpenTile(0, 0), OpenTile(1, 0),
    WallTile(0, 1), OpenTile(1, 1)
])
area.print_to(ConsoleView())

# TODO: Methods that check tile positions and also find the neighbours of a tile
#       should not be duplicated amongst all tile subclasses. Avoid inheritance for reuse!
