import uuid
from actors.null_action import NullAction
from actors.projectile_move_action import ProjectileMoveAction
from actors.stdin_driven_action import StdinDrivenAction
from actors.move_action import MoveAction
from actors.use_action import UseAction
from interactions.chained_interactions import ChainedInteractions
from interactions.change_interaction import ChangeInteraction
from interactions.destroy_interaction import DestroyInteraction
from interactions.dialogue_interaction import DialogueInteraction
from interactions.dialogue_options_interaction import DialogueOptionsInteraction
from interactions.filtered_interaction import FilteredInteraction
from interactions.null_interaction import NullInteraction
from interactions.pickup_interaction import PickupInteraction
from interactions.return_initiator_interaction import ReturnInitiatorInteraction
from items.gun import Gun
from views.actor_camera import ActorCamera
from views.console_dialogue_view import ConsoleDialogueView
from views.point_camera import PointCamera
from world.area import Area
from world.area_builder import AreaBuilder
from actors.actor import Actor
from views.console_view import ConsoleView
from world.rendered_area import RenderedArea

# TODO: Actor builder to simplify player\npc creation
# TODO: Area that maintains relative position of its sub-areas so it can move around while actors move inside it.
player_key = 'p'
input_action = StdinDrivenAction({
    'w': MoveAction(0, -1), 's': MoveAction(0, 1), 'a': MoveAction(-1, 0), 'd': MoveAction(1, 0),
    'i': UseAction(0, -1), 'k': UseAction(0, 1), 'j': UseAction(-1, 0), 'l': UseAction(1, 0)
})
return_interaction = ReturnInitiatorInteraction()
player = Actor(input_action, return_interaction, player_key)
null_action = NullAction()
dialogue_view = ConsoleDialogueView()
fire_dialogue = DialogueInteraction(dialogue_view, "coals glow faintly, the fire has been dead for a while")
camp_fire = Actor(null_action, ChainedInteractions([return_interaction, fire_dialogue]), "campfire")
belongings_dialogue = DialogueInteraction(dialogue_view, "all of your belongings, there is nothing inside")
empty_box = Actor(null_action, ChainedInteractions([return_interaction, belongings_dialogue, DestroyInteraction()]), "box")
skeleton_dialogue = DialogueInteraction(dialogue_view, "this skeleton lost its' life yet it still clutches a gun")
gun = Gun(lambda aim_dir: Actor(ProjectileMoveAction(aim_dir[0], aim_dir[1]), return_interaction, "*%s" % uuid.uuid1()))
no_gun_dialogue = DialogueInteraction(dialogue_view, "the skeleton looks friendly without a gun")
no_gun_action = ChangeInteraction(ChainedInteractions([FilteredInteraction(no_gun_dialogue, [player_key]), return_interaction]))
skeleton_options = {'yer': ChainedInteractions([PickupInteraction(gun), no_gun_action]), 'naw': NullInteraction()}
skeleton_options_dialogue = DialogueOptionsInteraction(dialogue_view, "take that too?", skeleton_options)
skeleton = Actor(null_action, ChainedInteractions([return_interaction, skeleton_dialogue, skeleton_options_dialogue]), "S")
campsite_area = AreaBuilder().reposition(3, 100).rectangle(1, 2).with_door(0, 0, 2, 84)\
                             .nudge(-1, 2).rectangle(3, 5).with_actor(player, 1, 3).with_actor(camp_fire, 1, 2)\
                             .nudge(3, 2).rectangle(2, 2).with_actor(empty_box, 0, 1)\
                             .nudge(0, -1).rectangle(1, 1)\
                             .to_area()
intersection_area = AreaBuilder().reposition(0, 80).rectangle(5, 5).with_actor(skeleton, 2, 1).to_area()
area = RenderedArea(Area([campsite_area, intersection_area]), ActorCamera(player_key, PointCamera(2, 2, 10, ConsoleView())))

while True:
    area = area.update()
