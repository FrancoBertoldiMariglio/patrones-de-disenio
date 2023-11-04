from Television import Television
from TurnOnTVCommand import TurnOnTVCommand
from TurnOffTVCommand import TurnOffTVCommand
from VolumeUpTVCommand import VolumeUpTVCommand
from VolumeDownTVCommand import VolumeDownTVCommand
from RemoteControl import RemoteControl

if __name__ == "__main__":
    television = Television()
    turn_on_command = TurnOnTVCommand(television)
    turn_off_command = TurnOffTVCommand(television)
    volume_up_command = VolumeUpTVCommand(television)
    volume_down_command = VolumeDownTVCommand(television)

    remote_control = RemoteControl()
    remote_control.assign_command("ON", turn_on_command)
    remote_control.assign_command("OFF", turn_off_command)
    remote_control.assign_command("+", volume_up_command)
    remote_control.assign_command("-", volume_down_command)

    remote_control.press_button("ON")
    remote_control.press_button("+")
    remote_control.press_button("+")
    remote_control.press_button("+")
    remote_control.press_button("-")
    remote_control.press_button("change channel")
