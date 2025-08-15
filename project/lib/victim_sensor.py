from PiicoDev_SSD1306 import *
from PiicoDev_Unified import sleep_ms

display = create_PiicoDev_SSD1306()

class Victim_Sensor:
    def __init__(self, display, colour_sensor, debug):
        self.__colour_sensor = colour_sensor
        self.__debug = debug
        self.__display = display

    def SenseVictim(self):
        if self.__debug:
            print("sensing")
        data = self.__colour_sensor.readHSV()

        hue = data['hue']
        if hue > 75 and hue < 85:
            display.text("Victim Sensed",1,20, 1)
            display.show()
            return "green"
        else:
            display.fill(0)
            return "not green"