class DialogueOptionsInteraction:

    def __init__(self, dialogue_media, prompt, options):
        self.dialogue_media = dialogue_media
        self.prompt = prompt
        self.options = options

    def between(self, initiator, origin, receiver, destination, root):
        selected_option = self.dialogue_media.with_message(self.prompt).render_with_choice(self.options)
        return selected_option.between(initiator, origin, receiver, destination, root)

