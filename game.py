from actors.actions.hit_and_run_action import HitAndRunAction
from actors.actions.shoot_at_action import ShootAtAction
from actors.actor_target import ActorTarget
from actors.components.components import Components
from actors.components.health import Health
from actors.components.inventory import Inventory
from actors.actions.keyboard_driven_action import KeyboardDrivenAction
from actors.interactions.null_interaction import NullInteraction
from actors.projectile import Projectile
from actors.actions.move_action import MoveAction
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
gun = Gun(lambda aim_dir: Projectile(aim_dir, "*"))
inventory = Inventory(frozenset([gun]))
player_target = ActorTarget(player_key)
cowboy_components = Components(frozenset([inventory, Health(3, 3)]))
shoot_at_action = ShootAtAction(player_target, UseAction())
hit_and_run_action = HitAndRunAction(player_target, shoot_at_action, 5, 2)
bandit = Actor(hit_and_run_action, NullInteraction(), "b", cowboy_components)
player = Actor(input_action, NullInteraction(), player_key, cowboy_components)
area = RenderedArea(AreaBuilder().rectangle(16, 8)
                    .with_actor(player, 7, 7)
                    .with_actor(bandit, 7, 0)
                    .with_actor(bandit.unique(), 2, 4)
                    .with_actor(bandit.unique(), 6, 4)
                    .to_area(), ConsoleView())
while True:
    area = area.update()
