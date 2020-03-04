from views.area_media import AreaMedia


class DeathTriggerEffect(AreaMedia):

    def __init__(self, effect, actors=[], keys=[]):
        self.effect = effect
        self.actors = actors
        self.keys = keys

    def affect(self, area):
        return area.replace_effect(self, self.effect) if area.print_to(self).all_keys_matched() else area

    def all_keys_matched(self):
        return all([not any([actor.identifies_with(key) for key in self.keys]) for actor in self.actors])

    def watch(self, actor):
        return DeathTriggerEffect(self.effect, self.actors + [actor], self.keys)

    def with_actor(self, x, y, key):
        return DeathTriggerEffect(self.effect, self.actors, self.keys + [key])
