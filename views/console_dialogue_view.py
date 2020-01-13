class ConsoleDialogueView:

    def __init__(self, speaker="", message=""):
        self.speaker = speaker
        self.message = message

    def render(self):
        self.__print_message()
        input()
        return self

    def render_with_choice(self, options):
        if len(options) == 0:
            raise Exception("Selection failed, no options provided")
        self.__print_message()
        [print("\t-> %s" % key) for key in options.keys()]
        selected_key = None
        while selected_key not in options:
            selected_key = input()
        return options[selected_key]

    def with_actor(self, x, y, key):
        return ConsoleDialogueView(key, self.message)

    def with_message(self, message):
        return ConsoleDialogueView(self.speaker, message)

    def __print_message(self):
        print("%s: %s" % (self.speaker, self.message))

