from world.area_builder import AreaBuilder
from actors.actor import Actor
from actors.input_engine import InputEngine
from views.console_view import ConsoleView

input_engine = InputEngine({'w': (0, -1), 's': (0, 1), 'a': (-1, 0), 'd': (1, 0)})
sub_area = AreaBuilder().starting_from(5, 0).rectangle(3, 3).to_area()
player = Actor(input_engine, '@')
area = AreaBuilder().rectangle(5, 5)\
                    .with_actor(player, 2, 0)\
                    .to_area()

# TODO: Refactor this code outta limbo!
while True:
    area.print_to(ConsoleView())
    area = area.with_tiles(area.update())
