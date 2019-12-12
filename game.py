from world.area import Area
from world.area_builder import AreaBuilder
from actors.actor import Actor
from actors.input_engine import InputEngine
from views.console_view import ConsoleView

input_engine = InputEngine({'w': (0, -1), 's': (0, 1), 'a': (-1, 0), 'd': (1, 0)})
player = Actor(input_engine, '@')
area_one = AreaBuilder().rectangle(5, 5)\
                    .with_actor(player, 2, 0)\
                    .to_area()
area_two = AreaBuilder().starting_from(10, 0)\
                        .rectangle(5, 5)\
                        .to_area()
area = Area([area_one, area_two])

while True:
    # TODO: How to print only a portion of the world?
    # TODO: Move print back into ConsoleView
    print(area.print_to(ConsoleView()))
    area = area.update(area)
