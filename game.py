from spaces.area_builder import AreaBuilder
from actors.actor import Actor
from actors.input_engine import InputEngine
from actors.random_engine import RandomEngine
from views.console_view import ConsoleView

npc = Actor(RandomEngine(), '$')
player = Actor(InputEngine({
            'w': (0, -1), 's': (0, 1),
            'a': (-1, 0), 'd': (1, 0)
        }))
area = AreaBuilder().rectangle(5, 5)\
                    .with_actor(player, 0, 0)\
                    .with_actor(npc, 4, 0)\
                    .to_area()

while True:
    area.print_to(ConsoleView())
    area = area.update()
