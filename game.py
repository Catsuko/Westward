import uuid

from actors.actor_target import ActorTarget
from actors.keyboard_driven_action import KeyboardDrivenAction
from actors.projectile_move_action import ProjectileMoveAction
from actors.move_action import MoveAction
from actors.scorpion import Scorpion
from actors.use_action import UseAction
from interactions.return_initiator_interaction import ReturnInitiatorInteraction
from items.gun import Gun
from views.console_view import ConsoleView
from world.area_builder import AreaBuilder
from actors.actor import Actor

# TODO: Actor builder to simplify player\npc creation
# TODO: Area that maintains relative position of its sub-areas so it can move around while actors move inside it.
from world.rendered_area import RenderedArea

player_key = 'p'
input_action = KeyboardDrivenAction({
    'w': MoveAction(0, -1), 's': MoveAction(0, 1), 'a': MoveAction(-1, 0), 'd': MoveAction(1, 0),
    'i': UseAction(0, -1), 'k': UseAction(0, 1), 'j': UseAction(-1, 0), 'l': UseAction(1, 0)
})
scorpion = Scorpion(ActorTarget(player_key), MoveAction())
return_interaction = ReturnInitiatorInteraction()
player = Actor(input_action, return_interaction, player_key)
area = RenderedArea(AreaBuilder().rectangle(16, 8).with_actor(player, 4, 4).with_actor(scorpion, 0, 0).to_area(), ConsoleView())
gun = Gun(lambda aim_dir: Actor(ProjectileMoveAction(aim_dir[0], aim_dir[1]), return_interaction, "*%s" % uuid.uuid1()))
while True:
    area = area.update()
