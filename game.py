import uuid

from actors.actions.chase_action import ChaseAction
from actors.actions.staggered_action import StaggeredAction
from actors.actor_target import ActorTarget
from actors.components.components import Components
from actors.components.health import Health
from actors.components.inventory import Inventory
from actors.actions.keyboard_driven_action import KeyboardDrivenAction
from actors.interactions.damage_interaction import DamageInteraction
from actors.interactions.null_interaction import NullInteraction
from actors.projectile import Projectile
from actors.actions.move_action import MoveAction
from actors.actions.use_action import UseAction
from items.gun import Gun
from views.console_view import ConsoleView
from world.area_builder import AreaBuilder
from actors.actor import Actor
from world.effects.spawn_effect import SpawnEffect
from world.rendered_area import RenderedArea

player_key = 'p'
input_action = KeyboardDrivenAction({
    'w': MoveAction(0, -1), 's': MoveAction(0, 1), 'a': MoveAction(-1, 0), 'd': MoveAction(1, 0),
    'i': UseAction(0, -1), 'k': UseAction(0, 1), 'j': UseAction(-1, 0), 'l': UseAction(1, 0)
})
gun = Gun(lambda aim_dir: Projectile(aim_dir, "*%s" % uuid.uuid1()))
inventory = Inventory(frozenset([gun]))
scorpion_action = StaggeredAction(ChaseAction(ActorTarget(player_key), MoveAction()))
scorpion = Actor(scorpion_action, DamageInteraction(), "s", Components(frozenset([Health(1, 1)])))
spawn_effect = SpawnEffect(scorpion, [(0, 0), (5, 0)])
player = Actor(input_action, NullInteraction(), player_key, Components(frozenset([inventory, Health(3, 3)])))
area = RenderedArea(AreaBuilder().rectangle(16, 8)
                    .with_actor(player, 4, 4).to_area(), ConsoleView())
area = spawn_effect.affect(area)
while True:
    area = area.update()
