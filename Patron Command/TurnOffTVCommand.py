from Command import Command


class TurnOffTVCommand(Command):
    def __init__(self, television):
        self.television = television

    def execute(self):
        self.television.turn_off()