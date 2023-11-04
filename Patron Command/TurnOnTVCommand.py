from Command import Command


class TurnOnTVCommand(Command):
    def __init__(self, television):
        self.television = television

    def execute(self):
        self.television.turn_on()