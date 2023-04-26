import pygame as pg

class MyJoysitck:
    JOY = None
    def __init__(self, id:int = 0):
        self.id = id
        try:
            self.joy = pg.joystick.Joystick(self.id)
            self.joy.init()
            self.JOY = self.joy
        except:
            self.joy = self.JOY
        print("joystick: " + str(self.get_axis(0)))

    def init(self) -> None:
        try:
            self.joy.init()
        except:
            pass
    def quit(self) -> None: 
        try:
            self.joy.quit()
        except:
            pass
    def get_init(self) -> bool:
        try:
            return self.joy.get_init()
        except:
            return False
    def get_id(self) -> int:
        try:
            return self.joy.get_id()
        except:
            return -1
    def get_instance_id(self) -> int:
        try:
            return self.joy.get_instance_id()
        except:
            return -1
    def get_guid(self) -> str:
        try:
            return self.joy.get_guid()
        except:
            return "nothing"
    def get_power_level(self) -> str:
        try:
            return self.joy.get_power_level()
        except:
            return "0v"
    def get_name(self) -> str:
        try:
            return self.joy.get_name()
        except:
            return "nothing"
    def get_numaxes(self) -> int:
        try:
            return self.joy.get_numaxes()
        except:
            return -1
    def get_axis(self, axis_number: int) -> float:
        try:
            return self.joy.get_axis(axis_number)
        except:
            return 0.0
    def get_numballs(self) -> int:
        try:
            return self.joy.get_numballs()
        except:
            return -1
    def get_numbuttons(self) -> int:
        try:
            return self.joy.get_numbuttons()
        except:
            return 0
    def get_button(self, button: int) -> bool:
        try:
            return self.joy.get_button(button)
        except:
            return False
    def get_numhats(self) -> int:
        try:
            return self.joy.get_numhats()
        except:
            return 0
    def rumble(self, low_frequency: float, high_frequency: float, duration: int) -> bool:
        try:
            return self.joy.rumble(low_frequency, high_frequency, duration)
        except:
            return False
    def stop_rumble(self) -> None: 
        try:
            self.joy.stop_rumble()
        except:
            pass