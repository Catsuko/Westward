from actors.actions.hit_and_run_action import HitAndRunAction
from actors.actions.input_driven_action import InputDrivenAction
from actors.actions.shoot_at_action import ShootAtAction
from actors.actor_target import ActorTarget
from actors.components.components import Components
from actors.components.health import Health
from actors.components.inventory import Inventory
from actors.interactions.null_interaction import NullInteraction
from actors.projectile import Projectile
from actors.actions.move_action import MoveAction
from actors.actions.use_action import UseAction
from input.keyboard_input import KeyboardInput
from items.gun import Gun
from views.json_environment import JsonEnvironment
from views.pyxel_area_view import PyxelAreaView
from world.area_builder import AreaBuilder
from actors.actor import Actor
from world.rendered_area import RenderedArea
from utilities.countdown import Countdown
import threading


player_key = 'p'
input_action = InputDrivenAction({
    'w': MoveAction(0, -1), 's': MoveAction(0, 1), 'a': MoveAction(-1, 0), 'd': MoveAction(1, 0),
    'i': UseAction(0, -1), 'k': UseAction(0, 1), 'j': UseAction(-1, 0), 'l': UseAction(1, 0)
}, KeyboardInput())
gun = Gun(lambda aim_dir: Projectile(aim_dir, "*"))
inventory = Inventory(frozenset([gun]))
player_target = ActorTarget(player_key)
cowboy_components = Components(frozenset([inventory, Health(5, 5)]))
shoot_at_action = ShootAtAction(player_target, UseAction())
hit_and_run_action = HitAndRunAction(player_target, shoot_at_action, MoveAction(), 5, Countdown(4, 0))
bandit = Actor(hit_and_run_action, NullInteraction(), "b", cowboy_components)
player = Actor(input_action, NullInteraction(), player_key, cowboy_components)
pyxel_view = PyxelAreaView(128, 128, JsonEnvironment('config/pyxel_environment.json'))
area = RenderedArea(AreaBuilder().rectangle(16, 8)
                    .with_actor(player, 7, 7)
                    .with_actor(bandit, 7, 0)
                    .with_actor(bandit.unique(), 2, 4)
                    .with_actor(bandit.unique(), 6, 4)
                    .to_area(), pyxel_view)
def update_loop(a):
    while True:
        a = a.update()

thread = threading.Thread(target=lambda: update_loop(area))
thread.start()
pyxel_view.run()
