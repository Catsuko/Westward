import uuid
from actors.actor_target import ActorTarget
from actors.components.components import Components
from actors.components.health import Health
from actors.components.inventory import Inventory
from actors.actions.keyboard_driven_action import KeyboardDrivenAction
from actors.projectile import Projectile
from actors.actions.move_action import MoveAction
from actors.scorpion import Scorpion
from actors.actions.use_action import UseAction
from items.gun import Gun
from views.console_view import ConsoleView
from world.area_builder import AreaBuilder
from actors.actor import Actor
from world.rendered_area import RenderedArea

player_key = 'p'
input_action = KeyboardDrivenAction({
    'w': MoveAction(0, -1), 's': MoveAction(0, 1), 'a': MoveAction(-1, 0), 'd': MoveAction(1, 0),
    'i': UseAction(0, -1), 'k': UseAction(0, 1), 'j': UseAction(-1, 0), 'l': UseAction(1, 0)
})
scorpion = Scorpion(ActorTarget(player_key), MoveAction(), Components(frozenset([Health(1, 1)])))
gun = Gun(lambda aim_dir: Projectile(aim_dir, "*%s" % uuid.uuid1()))
inventory = Inventory(frozenset([gun]))
player = Actor(input_action, player_key, Components(frozenset([inventory, Health(3, 3)])))
area = RenderedArea(AreaBuilder().rectangle(16, 8)
                    .with_actor(player, 4, 4)
                    .with_actor(scorpion, 0, 0).to_area(), ConsoleView())
while True:
    area = area.update()
