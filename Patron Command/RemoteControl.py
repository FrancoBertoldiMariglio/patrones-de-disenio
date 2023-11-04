

class RemoteControl():
    def __init__(self):
        self.commands = {}

    def assign_command(self, button, command):
        self.commands[button] = command

    def press_button(self, button):
        if button in self.commands:
            self.commands[button].execute()
        else:
            print(f"El botón {button} no está asignado")