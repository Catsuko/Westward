class DialogueInteraction:

    def __init__(self, dialogue_media, message):
        self.dialogue_media = dialogue_media
        self.message = message

    def between(self, initiator, origin, receiver, destination, root):
        destination.print_to(self.dialogue_media).with_message(self.message).render()
        return root
