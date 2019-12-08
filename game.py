from spaces.area_builder import AreaBuilder
from actors.actor import Actor
from actors.input_engine import InputEngine
from views.console_view import ConsoleView

input_engine = InputEngine({'w': (0, -1), 's': (0, 1), 'a': (-1, 0), 'd': (1, 0)})
sub_area = AreaBuilder().starting_from(5, 0).rectangle(3, 3).to_area()
new_areas = []
player = Actor(input_engine, '@', lambda a: new_areas.append(a))
area = AreaBuilder().rectangle(5, 5)\
                    .with_actor(player, 2, 0)\
                    .with_door(5, 0, sub_area)\
                    .to_area()

# TODO: Refactor this code outta limbo!
while True:
    area.print_to(ConsoleView())
    area = area.update()
    # TODO: How to handle switching areas nicely?
    if len(new_areas) > 0:
        area = new_areas[0]
        new_areas = []
