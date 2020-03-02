class DelayedAction:

    def __init__(self, action, delay_remaining=1):
        self.action = action
        self.delay_remaining = delay_remaining

    def on(self, actor, tile, root):
        delay_remaining = self.delay_remaining - 1
        return root, (DelayedAction(self.action, delay_remaining) if delay_remaining > 0 else self.action)
