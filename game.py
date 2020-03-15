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
from views.actor_camera import ActorCamera
from views.json_environment import JsonEnvironment
from views.point_camera import PointCamera
from views.pyxel.shaders.color_mapped_shader import ColorMappedShader
from views.pyxel.shaders.scaled_shader import ScaledShader
from views.pyxel.shaders.flicker_shader import FlickerShader
from views.pyxel.pyxel_area_view import PyxelAreaView
from views.pyxel.pyxel_unit_view import PyxelUnitView
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
cowboy_components = Components(frozenset([inventory, Health(99, 99)]))
shoot_at_action = ShootAtAction(player_target, UseAction())
hit_and_run_action = HitAndRunAction(player_target, shoot_at_action, MoveAction(), 3, Countdown(4, 0))
bandit = Actor(hit_and_run_action, NullInteraction(), "b", cowboy_components)
player = Actor(input_action, NullInteraction(), player_key, cowboy_components)
shader = ScaledShader(ColorMappedShader(JsonEnvironment('config/pyxel_environment.json')), range(8))
tile_view = PyxelUnitView(shader)
actor_view = PyxelUnitView(shader)
effect_view = PyxelUnitView(FlickerShader(shader, 4))
pyxel_view = PyxelAreaView(tile_view, actor_view, effect_view)
camera = ActorCamera(player_key, PointCamera(0, 0, 6, pyxel_view))
# TODO: Action that waits for an actor to enter within a certain distance? Make enemies idle about!
area = RenderedArea(AreaBuilder().rectangle(20, 20)
                    .with_actor(player, 10, 10)
                    .with_actor(bandit, 15, 10)
                    .with_actor(bandit.unique(), 5, 10)
                    .with_actor(bandit.unique(), 10, 0)
                    .to_area(), camera)
def update_loop(a):
    while True:
        a = a.update()

thread = threading.Thread(target=lambda: update_loop(area))
thread.start()
pyxel_view.run(128, 128)
