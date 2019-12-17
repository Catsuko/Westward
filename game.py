from actors.random_engine import RandomEngine
from views.actor_camera import ActorCamera
from views.point_camera import PointCamera
from world.area import Area
from world.area_builder import AreaBuilder
from actors.actor import Actor
from actors.input_engine import InputEngine
from views.console_view import ConsoleView
from world.rendered_area import RenderedArea

player_key = 'p'
player = Actor(InputEngine({'w': (0, -1), 's': (0, 1), 'a': (-1, 0), 'd': (1, 0)}), player_key)
area_one = AreaBuilder().rectangle(5, 5)\
                    .with_actor(player, 2, 0)\
                    .with_door(4, 0, 11, 0)\
                    .with_door(4, 4, 11, 4)\
                    .with_ledge(0, 3).with_ledge(1, 3).with_ledge(2, 3).with_ledge(3, 3).with_ledge(4, 3)\
                    .to_area()
# TODO: How can the builder be extended so you can draw lines of the same tile?
#       Maybe the with_ledge\wall method returns its own builder that provides further options.
area_two = AreaBuilder().starting_from(10, 0)\
                        .rectangle(5, 5)\
                        .with_door(0, 0, 3, 0)\
                        .with_door(0, 4, 3, 4)\
                        .with_wall(0, 2).with_wall(1, 2).with_wall(2, 2).with_wall(3, 2)\
                        .with_actor(Actor(RandomEngine(), "n"), 2, 1)\
                        .to_area()
area = RenderedArea(Area([area_one, area_two]), ActorCamera(player_key, PointCamera(2, 2, 5, ConsoleView())))

while True:
    area = area.update()
