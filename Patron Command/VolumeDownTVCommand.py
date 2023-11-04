from Command import Command


class VolumeDownTVCommand(Command):
    def __init__(self, television):
        self.television = television

    def execute(self):
        self.television.volume_down()